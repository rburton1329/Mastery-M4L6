import argparse
import math
from typing import List, Tuple, Optional

import pandas as pd
import matplotlib.pyplot as plt

import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.io import shapereader as shpreader

BURN_COLS = ["forest", "savannas", "shrublands_grasslands", "croplands", "other"]

def load_aggregate(csv_path: str, year: Optional[int]) -> List[Tuple[str, float]]:
    df = pd.read_csv(csv_path)
    if year is not None:
        df = df[df["year"] == int(year)]
    for col in BURN_COLS:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")
    df["burned_km2"] = df[BURN_COLS].sum(axis=1)
    agg = (df.groupby("country", as_index=False)["burned_km2"].sum()
             .query("burned_km2 > 0")
             .sort_values("burned_km2", ascending=False))
    return list(zip(agg["country"].astype(str), agg["burned_km2"].astype(float)))

def build_country_centroids():
    path = shpreader.natural_earth(resolution="110m", category="cultural", name="admin_0_countries")
    cents = {}
    for rec in shpreader.Reader(path).records():
        name = rec.attributes.get("NAME_EN") or rec.attributes.get("ADMIN") or rec.attributes.get("NAME")
        if not isinstance(name, str):
            continue
        pt = rec.geometry.representative_point()   # inside the polygon
        cents[name.strip().upper()] = (pt.x, pt.y)
    return cents

def map_countries(items: List[Tuple[str, float]], out_png: str, top: int):
    cents = build_country_centroids()
    items = items[:top]
    lons, lats, sizes, labels = [], [], [], []
    for name, km2 in items:
        key = name.strip().upper()
        if key in cents:
            x, y = cents[key]
            lons.append(x); lats.append(y)
            sizes.append(max(15.0, math.sqrt(km2) * 0.8))  # sqrt scale
            labels.append(f"{name}: {km2:.0f} km²")

    proj = ccrs.PlateCarree()
    fig = plt.figure(figsize=(12, 6))
    ax = plt.axes(projection=proj)
    ax.set_global()
    ax.coastlines(linewidth=0.6)
    ax.add_feature(cfeature.BORDERS, linewidth=0.3)
    ax.gridlines(draw_labels=False, linewidth=0.2, alpha=0.5, linestyle="--")

    ax.scatter(lons, lats, s=sizes, alpha=0.6, transform=proj)
    for x, y, t in zip(lons, lats, labels):
        ax.text(x + 1, y + 1, t, fontsize=6, transform=proj)

    ax.set_title("Affected countries (marker size ≈ burned km²)")
    plt.tight_layout()
    plt.savefig(out_png, bbox_inches="tight", dpi=160)
    print(f"Saved: {out_png}")
    try:
        plt.show()
    except Exception:
        pass

def main():
    ap = argparse.ArgumentParser(description="Cartopy map of affected countries from MCD64A1.")
    ap.add_argument("--csv", required=True, help="Path to MCD64A1_burned_area_full_dataset_2002-2023.csv (INSIDE the VM).")
    ap.add_argument("--year", type=int, default=None, help="Filter to a single year (e.g., 2023).")
    ap.add_argument("--top", type=int, default=50, help="Max number of countries to plot/label.")
    ap.add_argument("--out", default="affected_map.png", help="Output PNG filename.")
    args = ap.parse_args()

    items = load_aggregate(args.csv, year=args.year)
    if not items:
        print("No affected countries found (burned area = 0 after filtering).")
        return
    print("Top 10 affected countries:")
    for n, v in items[:10]:
        print(f"{n:30} {v:12.1f} km²")

    map_countries(items, out_png=args.out, top=args.top)

if __name__ == "__main__":
    main()