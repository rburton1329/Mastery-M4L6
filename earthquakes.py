import matplotlib.pyplot as plt
from datetime import datetime, timezone

data = {"type":"FeatureCollection","metadata":{"generated":1755299900000,"url":"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson","title":"USGS All Earthquakes, Past Hour","status":200,"api":"1.14.1","count":5},"features":[{"type":"Feature","properties":{"mag":1.81,"place":"11 km SSE of Volcano, Hawaii","time":1755299541200,"updated":1755299794840,"tz":None,"url":"https://earthquake.usgs.gov/earthquakes/eventpage/hv74753377","detail":"https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/hv74753377.geojson","felt":None,"cdi":None,"mmi":None,"alert":None,"status":"automatic","tsunami":0,"sig":50,"net":"hv","code":"74753377","ids":",hv74753377,","sources":",hv,","types":",origin,phase-data,","nst":53,"dmin":0.03466,"rms":0.230000004,"gap":70,"magType":"ml","type":"earthquake","title":"M 1.8 - 11 km SSE of Volcano, Hawaii"},"geometry":{"type":"Point","coordinates":[-155.210006713867,19.3393325805664,3.98000001907349]},"id":"hv74753377"},
{"type":"Feature","properties":{"mag":1.3,"place":"8 km NNW of The Geysers, CA","time":1755299183960,"updated":1755299278983,"tz":None,"url":"https://earthquake.usgs.gov/earthquakes/eventpage/nc75224297","detail":"https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/nc75224297.geojson","felt":None,"cdi":None,"mmi":None,"alert":None,"status":"automatic","tsunami":0,"sig":26,"net":"nc","code":"75224297","ids":",nc75224297,","sources":",nc,","types":",nearby-cities,origin,phase-data,","nst":20,"dmin":0.005964,"rms":0.02,"gap":60,"magType":"md","type":"earthquake","title":"M 1.3 - 8 km NNW of The Geysers, CA"},"geometry":{"type":"Point","coordinates":[-122.814666748047,38.8281669616699,2.10999989509583]},"id":"nc75224297"},
{"type":"Feature","properties":{"mag":1.08,"place":"8 km NNW of The Geysers, CA","time":1755298835490,"updated":1755298933845,"tz":None,"url":"https://earthquake.usgs.gov/earthquakes/eventpage/nc75224292","detail":"https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/nc75224292.geojson","felt":None,"cdi":None,"mmi":None,"alert":None,"status":"automatic","tsunami":0,"sig":18,"net":"nc","code":"75224292","ids":",nc75224292,","sources":",nc,","types":",nearby-cities,origin,phase-data,","nst":14,"dmin":0.008636,"rms":0.02,"gap":66,"magType":"md","type":"earthquake","title":"M 1.1 - 8 km NNW of The Geysers, CA"},"geometry":{"type":"Point","coordinates":[-122.819000244141,38.828498840332,1.27999997138977]},"id":"nc75224292"},
{"type":"Feature","properties":{"mag":0.8,"place":"8 km NNW of The Geysers, CA","time":1755298438830,"updated":1755298533684,"tz":None,"url":"https://earthquake.usgs.gov/earthquakes/eventpage/nc75224277","detail":"https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/nc75224277.geojson","felt":None,"cdi":None,"mmi":None,"alert":None,"status":"automatic","tsunami":0,"sig":10,"net":"nc","code":"75224277","ids":",nc75224277,","sources":",nc,","types":",nearby-cities,origin,phase-data,","nst":11,"dmin":0.009804,"rms":0.02,"gap":112,"magType":"md","type":"earthquake","title":"M 0.8 - 8 km NNW of The Geysers, CA"},"geometry":{"type":"Point","coordinates":[-122.820663452148,38.8286666870117,1.67999994754791]},"id":"nc75224277"},
{"type":"Feature","properties":{"mag":1.4,"place":"22 km W of Anchorage, Alaska","time":1755296403653,"updated":1755296495344,"tz":None,"url":"https://earthquake.usgs.gov/earthquakes/eventpage/ak025afs7m0d","detail":"https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak025afs7m0d.geojson","felt":None,"cdi":None,"mmi":None,"alert":None,"status":"automatic","tsunami":0,"sig":30,"net":"ak","code":"025afs7m0d","ids":",ak025afs7m0d,","sources":",ak,","types":",origin,phase-data,","nst":None,"dmin":None,"rms":0.38,"gap":None,"magType":"ml","type":"earthquake","title":"M 1.4 - 22 km W of Anchorage, Alaska"},"geometry":{"type":"Point","coordinates":[-150.3144,61.2356,38.9]},"id":"ak025afs7m0d"}],"bbox":[-155.21000671387,19.339332580566,1.2799999713898,-122.81466674805,61.2356,38.9]}


quakes = []
for f in data.get("features", []):
    props = f.get("properties", {}) or {}
    geom  = f.get("geometry", {}) or {}
    coords = geom.get("coordinates", [None, None, None])
    if not isinstance(coords, (list, tuple)) or len(coords) < 2:
        continue
    lon, lat = coords[0], coords[1]
    if not isinstance(lon, (int, float)) or not isinstance(lat, (int, float)):
        continue
    t_ms = props.get("time")
    time_str = (
        datetime.fromtimestamp(t_ms/1000, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        if isinstance(t_ms, (int, float)) else "Time N/A"
    )
    quakes.append({
        "lon": lon,
        "lat": lat,
        "mag": props.get("mag"),
        "place": props.get("place") or "(unknown)",
        "time_str": time_str,
    })


print(f"{'Time (UTC)':19}  {'Mag':>4}  {'Lat':>9}  {'Lon':>10}  Place")
print("-"*70)
for q in quakes:
    mag = "—" if q["mag"] is None else f"{q['mag']:.2f}"
    print(f"{q['time_str']:19}  {mag:>4}  {q['lat']:>9.4f}  {q['lon']:>10.4f}  {q['place']}")


lons  = [q["lon"] for q in quakes]
lats  = [q["lat"] for q in quakes]
mags  = [0.0 if not isinstance(q["mag"], (int, float)) else float(q["mag"]) for q in quakes]
sizes = [max(25.0, (m + 0.1) * 60.0) for m in mags]
labels = [f"{'M?' if q['mag'] is None else f'M{q['mag']:.1f}'} | {q['place']}\n{q['time_str']}" for q in quakes]

plt.figure(figsize=(12, 6))
plt.scatter(lons, lats, s=sizes, alpha=0.7, edgecolors="none")


for x, y, txt in zip(lons, lats, labels):
    plt.text(x + 0.3, y + 0.3, txt, fontsize=6, ha="left", va="bottom")

plt.title(f"USGS Earthquakes — Past Hour (labels: magnitude, place, UTC time) — {len(quakes)} events")
plt.xlabel("Longitude"); plt.ylabel("Latitude")
plt.xlim(-180, 180); plt.ylim(-90, 90)
plt.grid(True, linestyle="--", linewidth=0.5, alpha=0.6)
plt.tight_layout()


plt.savefig("earthquakes_q1.svg", bbox_inches="tight")
plt.savefig("earthquakes_q1.png", bbox_inches="tight", dpi=160)
print("Saved: earthquakes_q1.svg and earthquakes_q1.png")

try:
    plt.show()
except Exception:
    pass