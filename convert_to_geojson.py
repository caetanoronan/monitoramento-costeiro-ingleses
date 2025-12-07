import json, os, shapefile
from pyproj import CRS, Transformer

files = [
    ('Praia_ingleses_geometria', r'c:\Users\caetanoronan\OneDrive - UFSC\Área de Trabalho\Trabalho_8\Praia_ingleses_geometria.shp'),
    ('Dunas_nova', r'c:\Users\caetanoronan\OneDrive - UFSC\Área de Trabalho\Trabalho_8\Dunas_nova.shp')
]

for name, shp_path in files:
    base = os.path.splitext(shp_path)[0]
    prj_path = base + '.prj'
    out_path = os.path.join(os.path.dirname(shp_path), name + '.geojson')
    crs_src = CRS.from_wkt(open(prj_path, 'r', encoding='utf-8').read())
    transformer = Transformer.from_crs(crs_src, CRS.from_epsg(4326), always_xy=True)
    sf = shapefile.Reader(shp_path)
    feats = []
    fields = [f[0] for f in sf.fields if f[0] != 'DeletionFlag']
    for sr in sf.iterShapeRecords():
        shp = sr.shape
        rec = sr.record
        attrs = {fields[i]: rec[i] for i in range(len(fields))}
        parts = list(shp.parts) + [len(shp.points)]
        rings = []
        for i in range(len(parts)-1):
            pts = shp.points[parts[i]:parts[i+1]]
            ring = []
            for x, y in pts:
                lon, lat = transformer.transform(x, y)
                ring.append([lon, lat])
            rings.append(ring)
        if len(rings) == 1:
            geom = {"type": "Polygon", "coordinates": [rings[0]]}
        else:
            geom = {"type": "MultiPolygon", "coordinates": [[r] for r in rings]}
        feats.append({"type": "Feature", "geometry": geom, "properties": attrs})
    fc = {"type": "FeatureCollection", "features": feats, "crs": {"type": "name", "properties": {"name": "EPSG:4326"}}}
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(fc, f)
    print(f" escrito: {out_path} ({len(feats)} features)")
