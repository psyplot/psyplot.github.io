# coding: utf-8
import psyplot.project as psy
import xarray as xr
import numpy as np
import matplotlib.tri as mtri
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set_style('white')
plt.rcParams['savefig.dpi'] = 100
plt.rcParams['figure.subplot.left'] = 0.0
plt.rcParams['figure.subplot.right'] = 1.0
plt.rcParams['figure.subplot.bottom'] = 0
plt.rcParams['figure.subplot.top'] = 1.0
plt.rcParams['figure.figsize'] = (5, 5)
psy.rcParams['plotter.simple.ytickprops'] = dict(right=False)
psy.rcParams['plotter.simple.xtickprops'] = dict(top=False)
lines = psy.plot.lineplot(
    'demo.nc',        # netCDF file storing the data
    name='v',         # one plot for each variable
    t=range(5),       # one violin plot for each time step
    z=0, x=0,         # choose latitude and longitude as dimensions
    ylabel="{desc}",  # use the longname and units on the y-axis
    color='coolwarm', legend=False,
    yticks=range(-10, 11, 5)
)
lines.export("lines.svg")
