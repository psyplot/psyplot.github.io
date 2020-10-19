import psyplot.project as psy
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

plt.rcParams["savefig.dpi"] = 100
plt.rcParams["figure.subplot.left"] = 0.12
plt.rcParams["figure.subplot.right"] = 0.92
plt.rcParams["figure.subplot.bottom"] = 0.12
plt.rcParams["figure.subplot.top"] = 0.92
plt.rcParams["figure.figsize"] = (5, 5)

psy.rcParams["plotter.maps.xgrid"] = False
psy.rcParams["plotter.maps.ygrid"] = False

colors = [[1.0, 1.0, 1.0, 0.5]] * 2
psy.rcParams["colors.cmaps"]["mywhite"] = [[1.0, 1.0, 1.0, 0.5]] * 3

maps = psy.plot.mapplot(
    "scripts/icon-test.nc",
    name="t2m",
    cmap="mywhite",
    stock_img=True,
    map_extent="global",
    projection="ortho",
    clon=25,
    clat=45,
    datagrid=dict(color="k", linewidth=1.5),
    cbar="",
)

maps.export("assets/images/icon-demo.svg", transparent=True)
