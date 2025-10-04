import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from io import StringIO
import warnings
import numpy as np
import sys

# Suppress potential future warnings from geopandas
warnings.filterwarnings("ignore", category=FutureWarning)

# 1. Load the provided AI exposure data
csv_data = """region_id,geo_name,geo_type,region_code,population,ai_exposure_pct,source_url,source_date
R001,"Canada",country,CA,36991981,60,https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm,2024-09-03
R002,"Ontario",province,ON,14223942,60,https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm,2024-09-03
R003,"Quebec",province,QC,8501833,60,https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm,2024-09-03
R004,"British Columbia",province,BC,5000879,60,https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm,2024-09-03
R005,"Alberta",province,AB,4262635,60,https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm,2024-09-03
R006,"Manitoba",province,MB,1342153,60,https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm,2024-09-03
R007,"Saskatchewan",province,SK,1132505,60,https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm,2024-09-03
R008,"Nova Scotia",province,NS,969383,60,https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm,2024-09-03
R009,"New Brunswick",province,NB,775610,60,https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm,2024-09-03
R010,"Newfoundland and Labrador",province,NL,510550,60,https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm,2024-09-03
R011,"Prince Edward Island",province,PE,154331,60,https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm,2024-09-03
R012,"Northwest Territories",territory,NT,41070,60,https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm,2024-09-03
R013,"Yukon",territory,YT,40232,60,https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm,2024-09-03
R014,"Nunavut",territory,NU,36858,60,https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm,2024-09-03
R015,"Toronto",CMA,535,6202225,68,https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm,2024-09-03
R016,"Montreal",CMA,462,4291732,65,https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm,2024-09-03
R017,"Vancouver",CMA,933,2642825,64,https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm,2024-09-03
R018,"Calgary",CMA,825,1481806,63,https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm,2024-09-03
R019,"Edmonton",CMA,835,1418118,58,https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm,2024-09-03
R020,"Ottawa-Gatineau",CMA,505,1488307,73,https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm,2024-09-03
R021,"Winnipeg",CMA,602,834678,59,https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm,2024-09-03
R022,"Quebec",CMA,421,839311,65,https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm,2024-09-03
R023,"Hamilton",CMA,537,785184,62,https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm,2024-09-03
R024,"Kitchener-Cambridge-Waterloo",CMA,541,575847,59,https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm,2024-09-03
R025,"London",CMA,555,543551,59,https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm,2024-09-03
R026,"Halifax",CMA,205,465703,65,https://www150.statcan.gc.ca/n1/pub/11f0019m/11f0019m2024005-eng.htm,2024-09-03
"""
ai_exposure_df = pd.read_csv(StringIO(csv_data))
ai_exposure_df['region_code'] = ai_exposure_df['region_code'].astype(str)

# 2. Load Official Geospatial Data
try:
    provinces_gdf = gpd.read_file("zip://./lpr_000b21a_e.zip")
    provinces_gdf = provinces_gdf.rename(columns={'PREABBR': 'region_code'})
except Exception:
    print("--- MAP GENERATION FAILED: GEOSPATIAL DATA MISSING ---")
    print("\nThis script requires the official Statistics Canada boundary file to create an accurate map.")
    print("\nINSTRUCTIONS:")
    print("1. Download the 'Cartographic Boundary File' for 'Provinces and Territories 2021' (Shapefile format).")
    print("   Direct URL: https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/details/page.cfm?LANG=E&GENDER=1&STAT=1&DATA=1&GEO=0")
    print("2. The downloaded file will be a zip file named 'lpr_000b21a_e.zip'.")
    print("3. Place this entire zip file in the SAME FOLDER as this Python script.")
    print("4. Re-run the script.")
    sys.exit()

# FIX: Create a mapping to translate shapefile codes to the CSV's standard 2-letter codes.
code_map = {
    'Alta.': 'AB', 'B.C.': 'BC', 'Man.': 'MB', 'N.B.': 'NB',
    'N.L.': 'NL', 'N.S.': 'NS', 'N.W.T.': 'NT', 'Nvt.': 'NU',
    'Ont.': 'ON', 'P.E.I.': 'PE', 'Que.': 'QC', 'Sask.': 'SK', 'Y.T.': 'YT'
}
provinces_gdf['region_code'] = provinces_gdf['region_code'].map(code_map)

# 3. Calculate Population-Weighted Provincial Exposure Scores
prov_data = ai_exposure_df[ai_exposure_df['geo_type'].isin(['province', 'territory'])].copy()
cma_data = ai_exposure_df[ai_exposure_df['geo_type'] == 'CMA'].copy()

cma_to_prov = {
    'Toronto': 'ON', 'Ottawa-Gatineau': 'ON', 'Hamilton': 'ON', 'Kitchener-Cambridge-Waterloo': 'ON', 'London': 'ON',
    'Montreal': 'QC', 'Quebec': 'QC',
    'Vancouver': 'BC',
    'Calgary': 'AB', 'Edmonton': 'AB',
    'Winnipeg': 'MB',
    'Halifax': 'NS'
}
cma_data['prov_code'] = cma_data['geo_name'].map(cma_to_prov)

weighted_scores = {}
for code, group in cma_data.groupby('prov_code'):
    prov_info = prov_data[prov_data['region_code'] == code]
    if prov_info.empty: continue
    total_prov_pop = prov_info['population'].iloc[0]
    base_prov_exp = prov_info['ai_exposure_pct'].iloc[0]
    cma_pop = group['population'].sum()
    non_cma_pop = total_prov_pop - cma_pop
    weighted_cma_exposure = np.sum(group['population'] * group['ai_exposure_pct'])
    total_weighted_exposure = weighted_cma_exposure + (non_cma_pop * base_prov_exp)
    final_score = total_weighted_exposure / total_prov_pop
    weighted_scores[code] = final_score

prov_data['calculated_exposure'] = prov_data['region_code'].map(weighted_scores)
prov_data['calculated_exposure'].fillna(prov_data['ai_exposure_pct'], inplace=True)

provinces_merged = provinces_gdf.merge(prov_data, on='region_code', how='inner')

if provinces_merged.empty:
    print("--- MAP GENERATION FAILED: DATA MERGE FAILED ---")
    print("\nCould not match the 'region_code' between the shapefile and the CSV data.")
    print("This usually means the abbreviations in the shapefile's 'PREABBR' column don't match the CSV.")
    print("\nCodes found in shapefile:", sorted(provinces_gdf['region_code'].unique()))
    print("Codes to match from CSV:", sorted(prov_data['region_code'].unique()))
    sys.exit()

# 4. Set up and Plot the Map
fig, ax = plt.subplots(1, 1, figsize=(16, 12))
ax.set_facecolor('aliceblue')

lambert_proj = '+proj=lcc +lat_1=49 +lat_2=77 +lat_0=63.39 +lon_0=-91.86 +x_0=6200000 +y_0=3000000 +ellps=GRS80 +datum=NAD83 +units=m +no_defs'
provinces_merged = provinces_merged.to_crs(lambert_proj)

ax.set_xlim(provinces_merged.total_bounds[0] * 0.95, provinces_merged.total_bounds[2] * 1.05)
ax.set_ylim(provinces_merged.total_bounds[1] * 0.95, provinces_merged.total_bounds[3] * 1.05)

vmin = prov_data['calculated_exposure'].min()
vmax = prov_data['calculated_exposure'].max()
cmap = plt.get_cmap('YlOrRd')

provinces_merged.plot(column='calculated_exposure', cmap=cmap, linewidth=0.8, ax=ax, edgecolor='0.4', vmin=vmin, vmax=vmax)

provinces_merged['coords'] = provinces_merged['geometry'].apply(lambda x: x.representative_point().coords[:])
provinces_merged['coords'] = [coords[0] for coords in provinces_merged['coords']]
for idx, row in provinces_merged.iterrows():
    x, y = row['coords']
    if row['region_code'] == 'PE': y += 100000
    if row['region_code'] == 'NS': y -= 100000; x += 150000
    if row['region_code'] == 'NB': y += 50000; x -= 100000
    if row['region_code'] == 'BC': x -= 200000
    ax.text(x, y, row['region_code'], ha='center', va='center',
            fontsize=10, fontweight='bold', path_effects=[pe.withStroke(linewidth=2, foreground='white')])

ax.axis('off')

# 5. Add Map Elements and Save
ax.set_title('Canadian Provincial AI Job Exposure (Population-Weighted)', fontdict={'fontsize': '20', 'fontweight': 'bold'})

sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=vmin, vmax=vmax))
cbar = fig.colorbar(sm, ax=ax, orientation='vertical', fraction=0.03, pad=0.02)
cbar.set_label('Weighted AI Exposure Percentage (%)', fontdict={'fontsize': '12'})

caption = """
This choropleth map displays a population-weighted AI occupational exposure score for each Canadian province and territory.
The score is calculated by combining the AI exposure rates of major cities (CMAs) with the baseline rate for the rest of the province.
This method highlights provinces with large urban centers that have higher overall exposure to AI transformation in the workforce.
Data is derived from Statistics Canada (2024), based on the 2021 Census.
"""
fig.subplots_adjust(bottom=0.1, top=0.92)
fig.text(0.5, 0.02, caption, ha='center', fontsize=10, style='italic', wrap=True)

svg_filename = "canada_ai_exposure_map.svg"

fig.savefig(svg_filename, format='svg', bbox_inches='tight')

print(f"\nMap successfully saved as {svg_filename}")

