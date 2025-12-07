# Monitoramento Costeiro - Praia dos Ingleses

Projeto IFSC (Campus Florianópolis) para monitorar o alargamento artificial da orla e a dinâmica das dunas urbanas na Praia dos Ingleses usando aerofotogrametria e análise espacial.

## Conteúdo principal
- `apresentacao.html`: apresentação com abas e tema escuro, inclui mapa embutido da área de estudo.
- `mapa_estudo.html`: mapa interativo Leaflet com camadas da área alargada, dunas e buffer de 100 m (Turf.js).
- `query_gpkg.py`: script para inspecionar o GeoPackage de setores (`SC_setores_CD2022.gpkg`).

## Como visualizar
- GitHub Pages (online): https://caetanoronan.github.io/monitoramento-costeiro-ingleses/
- Mapa direto: https://caetanoronan.github.io/monitoramento-costeiro-ingleses/mapa_estudo.html
- Local: abra `apresentacao.html` no navegador; use o link “Abrir mapa em nova aba” ou acesse `mapa_estudo.html`.

## Requisitos locais
- Python 3.14 (ambiente `.venv` já configurado).
- Bibliotecas usadas: `pyshp` no script de consulta.

## Repositório remoto
URL: https://github.com/caetanoronan/monitoramento-costeiro-ingleses.git
