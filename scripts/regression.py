# coding: utf-8
import psyplot.project as psy
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['figure.subplot.left'] = 0
plt.rcParams['figure.subplot.right'] = 1
plt.rcParams['figure.subplot.bottom'] = 0
plt.rcParams['figure.subplot.top'] = 1
plt.rcParams['figure.figsize'] = (5, 5)
all_x = []
all_y = []
for i in range(3):
    deviation = np.abs(np.random.normal())
    all_x.append(np.linspace(-np.pi - deviation, np.pi + deviation))
    all_x[-1] += 3 * np.random.random_sample(size=all_x[-1].size)
    all_y.append(np.sin(all_x[-1]) + np.random.normal(scale=0.5, size=all_x[-1].size))
x = np.concatenate(all_x)
y = np.concatenate(all_y)
ds = xr.Dataset({'x': xr.Variable(('experiment', ), x),
                 'y': xr.Variable(('experiment', ), y)})
ds

p = psy.plot.densityreg(
    ds, name='y', coord='x', cmap='Blues', bins=50, density='kde',
    clabel='Kernel density', xlim='minmax', ylim='minmax',
    color=plt.rcParams['axes.prop_cycle'].by_key()['color'][1], 
    fit=lambda x, a: np.sin(a * x), cbar='', erroralpha=0.6,
    legend=False)
p.export("regression.svg")
