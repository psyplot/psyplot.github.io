# coding: utf-8
import psyplot.project as psy
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.feature as cf
get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['savefig.dpi'] = 100
plt.rcParams['figure.subplot.left'] = 0
plt.rcParams['figure.subplot.right'] = 1
plt.rcParams['figure.subplot.bottom'] = 0
plt.rcParams['figure.subplot.top'] = 1
plt.rcParams['figure.figsize'] = (5, 5)
psy.rcParams['plotter.maps.xgrid'] = False
psy.rcParams['plotter.maps.ygrid'] = False
maps = psy.plot.mapplot('psy-maps-demo.nc', name='t2m', clabel='{desc}', cmap='RdBu_r', 
                        map_extent=(-37, 74, -27, 84), cbar='')
maps.export("map.svg")
