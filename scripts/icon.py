# coding: utf-8
"""Create the psyplot icon

This script creates the psyplot icon with a dpi of 128 and a width and height
of 8 inches. The file is saved it to ``'icon1024.pkl'``"""

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cf
from matplotlib.text import FontProperties

# The path to the font
fontpath = "/usr/share/fonts/truetype/freefont/FreeSansBoldOblique.ttf"

fig = plt.figure(figsize=(10, 10), dpi=128)

ax = fig.add_axes(
    [0.0, 0.0, 1.0, 1.0],
    projection=ccrs.Orthographic(central_latitude=45, central_longitude=20),
)

url = "https://map1c.vis.earthdata.nasa.gov/wmts-geo/wmts.cgi"
layer = "VIIRS_CityLights_2012"

land = ax.add_feature(cf.LAND, facecolor="0.975")
ocean = ax.add_feature(cf.OCEAN, facecolor=plt.get_cmap("Blues")(0.5))

try:
    ax.spines["geo"].set_linewidth(0)
except KeyError:  # cartopy <= 0.18
    ax.outline_patch.set_edgecolor("none")

plt.savefig("assets/images/earth.png", transparent=True)
plt.savefig("assets/images/earth.svg", transparent=True)
