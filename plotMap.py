import geopandas as gpd
import matplotlib.pyplot as plt

# get the US states shapefile from the Census Bureau and filter out Alaska, Hawaii, and Puerto Rico
us_states = gpd.read_file("https://www2.census.gov/geo/tiger/GENZ2022/shp/cb_2022_us_state_20m.zip")
us_states = us_states[~us_states["STUSPS"].isin(["AK", "HI", "PR"])]
us_states = us_states.to_crs("EPSG:4326")

# plot the US states map
ax = us_states.plot(figsize=(20, 6), color="white", edgecolor="black", aspect=1.3)
ax.set_xlim(-130, -55)
ax.set_ylim(24, 62)

# add code to plot the coordinates of data points below. Double check coordinate system consistency!