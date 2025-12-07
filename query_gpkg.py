import sqlite3
from pathlib import Path

# Introspects the GeoPackage and searches for keywords in text columns.

gpkg = Path(r"C:\Users\caetanoronan\OneDrive - UFSC\Área de Trabalho\Trabalho_8\SC_setores_CD2022.gpkg")
if not gpkg.exists():
    raise SystemExit(f"Arquivo não encontrado: {gpkg}")

con = sqlite3.connect(gpkg)
cur = con.cursor()

layers = cur.execute(
    "select table_name, data_type, identifier, description from gpkg_contents"
).fetchall()
print("Camadas encontradas (gpkg_contents):", len(layers))
for tbl, dt, ident, desc in layers:
    print(f"  - {tbl} | {dt} | id={ident} | desc={desc}")

print("\nColunas da camada principal:")
cols_info = cur.execute("PRAGMA table_info('SC_setores_CD2022')").fetchall()
for cid, name, coltype, notnull, dflt, pk in cols_info:
    print(f"  {cid:02d} | {name} | {coltype}")

keywords = ['ingles', 'norte', 'florian']


def text_columns(table: str) -> list[str]:
    cols = cur.execute(f"PRAGMA table_info('{table}')").fetchall()
    text_cols = []
    for cid, name, coltype, notnull, dflt, pk in cols:
        t = (coltype or '').upper()
        if 'CHAR' in t or 'TEXT' in t or 'CLOB' in t or 'VARCHAR' in t or t == '':
            text_cols.append(name)
    return text_cols


matches: list[tuple[str, dict[str, list[tuple[str, int]]]]] = []
for tbl, dt, ident, desc in layers:
    if dt != 'features':
        continue
    tcols = text_columns(tbl)
    if not tcols:
        continue
    tbl_matches = {kw: [] for kw in keywords}
    for kw in keywords:
        pattern = f"%{kw}%"
        for col in tcols:
            q = f"select count(*) from '{tbl}' where lower(" + col + ") like ?"
            try:
                cnt = cur.execute(q, (pattern,)).fetchone()[0]
            except Exception:
                continue
            if cnt:
                tbl_matches[kw].append((col, cnt))
    if any(tbl_matches[kw] for kw in keywords):
        matches.append((tbl, tbl_matches))

print("\nTabelas com ocorrências:")
for tbl, tbl_matches in matches:
    print(f"Tabela: {tbl}")
    for kw in keywords:
        cols = tbl_matches[kw]
        if cols:
            preview_cols = []
            for col, cnt in cols:
                preview_cols.append(f"{col}={cnt}")
            print(f"  kw '{kw}':", ', '.join(preview_cols))
            col = cols[0][0]
            example = cur.execute(
                f"select {col} from '{tbl}' where lower({col}) like ? limit 3",
                (f"%{kw}%",),
            ).fetchall()
            example_vals = [e[0] for e in example]
            print("    exemplos:", example_vals)

# Recortes específicos: Florianópolis + Ingleses / Norte
table = 'SC_setores_CD2022'

def run_query(where: str, params: tuple[str, ...], label: str) -> None:
    rows = cur.execute(
        f"select CD_SETOR, NM_MUN, NM_DIST, NM_BAIRRO, AREA_KM2 from {table} where {where}",
        params,
    ).fetchall()
    if not rows:
        print(f"\n{label}: nenhum registro")
        return
    area_sum = sum(r[4] or 0 for r in rows)
    bairros = sorted({(r[3] or '').strip() for r in rows if r[3]})
    print(f"\n{label}: {len(rows)} setores")
    print(f"  Área total km²: {area_sum}")
    print(f"  Bairros únicos: {bairros}")
    print("  Exemplos CD_SETOR:", [r[0] for r in rows[:5]])

run_query(
    "lower(NM_MUN) like ? and (lower(NM_BAIRRO) like ? or lower(NM_DIST) like ?)",
    ('%florian%', '%ingles%', '%ingles%'),
    "Florianópolis + Ingleses",
)

run_query(
    "lower(NM_MUN) like ? and (lower(NM_BAIRRO) like ? or lower(NM_DIST) like ?)",
    ('%florian%', '%norte%', '%norte%'),
    "Florianópolis + 'norte' em distrito/bairro",
)

run_query(
    "lower(NM_MUN) like ? and lower(NM_BAIRRO) in (?,?,?)",
    ('%florian%', 'ingleses centro', 'ingleses norte', 'ingleses sul'),
    "Florianópolis + Ingleses (Centro/Norte/Sul)",
)

con.close()
