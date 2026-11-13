#Nitrogen for nine sites


import pandas as pd
import matplotlib.pyplot as plt

fert = pd.read_csv("~/Desktop/fertManure.csv")
wwtp = pd.read_csv("~/Desktop/ptSource_WWTP_CSO.csv")

# nine stations
stations = {
    "01491000": "Choptank River",
    "01578310": "Susquehanna River",
    "01594440": "Patuxent River",
    "01646580": "Potomac River",
    "01668000": "Rappahannock River",
    "01673000": "Pamunkey River",
    "01674500": "Mattaponi River",
    "02035000": "James River",
    "02041650": "Appomattox River"
}

# format station ids
fert["staid"] = fert["staid"].astype(str).str.zfill(8)
wwtp["staid"] = wwtp["staid"].astype(str).str.zfill(8)

# datasets by station and year
data = pd.merge(fert, wwtp, on=["staid", "year"], how="inner")

# create graphs
fig, axes = plt.subplots(3, 3, figsize=(24, 18), dpi=150)
axes = axes.flatten()

# plot stations
for ax, (station_id, station_name) in zip(axes, stations.items()):

    # filter data for stations
    station_data = data[data["staid"] == station_id]
    station_data = station_data.sort_values("year")

    # plot four nitrogen sources
    ax.plot(station_data["year"], station_data["fertTN"], label="Fertilizer N", color="green")
    ax.plot(station_data["year"], station_data["manureTN"], label="Manure N", color="orange")
    ax.plot(station_data["year"], station_data["ptsourcetn"], label="Point Source N", color="blue")
    ax.plot(station_data["year"], station_data["csotn"], label="CSO N", color="red")

    # formatting
    ax.set_title(f"{station_name}\nUSGS {station_id}")
    ax.set_xlabel("Year")
    ax.set_ylabel("Total Nitrogen Load")
    ax.grid(True, alpha=0.3)
    ax.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
    ax.legend(fontsize=8)

# title
fig.suptitle("Nitrogen Sources at Nine Chesapeake Bay Stations", fontsize=16)

plt.tight_layout()

# save
plt.savefig("nitrogen_9stations.png", dpi=300, bbox_inches="tight")

plt.show()
