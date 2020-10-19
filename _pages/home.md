---
title: psyplot
layout: splash
permalink: /
hidden: true
header:
  overlay_color: "#535368"
  overlay_filter: 0.5
  overlay_image: /assets/images/earth.svg
  og_image: /assets/images/earth.png
  actions:
    - label: <i class="fas fa-download"></i> Install now
      url: https://psyplot.readthedocs.io/en/latest/installing.html
tagline: |
    Interactive Data Visualization from Python and GUIs.<br />

    <a href="https://github.com/psyplot/psyplot/releases/latest" title="Latest release on GitHub">
        <img alt="GitHub release (latest SemVer)" src="https://img.shields.io/github/v/release/psyplot/psyplot?label=Latest%20release">
    </a>
excerpt: >
    A cross-platform open source python project that mainly combines the
    plotting utilities of matplotlib and the data management of the xarray
    package and integrates them into a software that can be used via command-line
    and via a GUI.
feature_row:
    - image_path: /assets/images/icon-demo.svg
      alt: ICON grid
      title: Plot unstructured grids
      url: https://psyplot.github.io/examples/maps/example_ugrid.html
      btn_class: "btn--primary btn--outline"
      btn_label: <i class="fas fa-book"></i> Read more
      excerpt: |
          The 2D plotmethods support the visualization of unstructured grids,
          such as the
          <a href="http://www.mpimet.mpg.de/en/science/models/icon-esm.html" title="ICON Earth system model of the Max-Planck-Institute for Meteorology">ICON</a> model
          or the <a href="http://ugrid-conventions.github.io/ugrid-conventions/">UGRID</a> conventions.

    - image_path: /assets/images/example-plots.png
      alt: plot methods
      title: Flexible plotmethods
      url: https://psyplot.github.io/examples/
      btn_class: "btn--primary btn--outline"
      btn_label: <i class="fas fa-book"></i> See examples
      excerpt: |
          We already have many plugins with many many formatoptions in existing
          <a href="https://psyplot.readthedocs.io/en/latest/plugins.html">plugins</a>
          to flexibly visualize your data.

    - image_path: /assets/images/script.png
      alt: python logo
      title: Usage in Scripts
      url: https://psyplot.readthedocs.io/en/latest/getting-started.html
      btn_class: "btn--primary btn--outline"
      btn_label: <i class="fab fa-python"></i> Get started
      excerpt: |
          Our standard is <i>command-line first</i>! psyplot offers a rich,
          flexible and simple framework to generate high-level APIs to be used
          in python scripts.

    - image_path: /assets/images/psy-view.png
      alt: psy-view screenshot
      title: ncview-like Interface
      url: https://mybinder.org/v2/gh/psyplot/examples/main?urlpath=%2Fdesktop
      btn_class: "btn--primary btn--outline"
      btn_label: <i class="fas fa-rocket"></i> Try it here
      excerpt: |
          Inspired by the popular <a href="http://meteora.ucsd.edu/~pierce/ncview_home_page.html">ncview</a>
          software, we designed a simple and intuitive application to open
          netCDF files (and more), <a href="https://psyplot.readthedocs.io/projects/psy-view/en/latest/">psy-view</a>.

    - image_path: /assets/images/psyplot-gui.png
      alt: psyplot GUI
      title: Graphical User Interface
      url: https://mybinder.org/v2/gh/psyplot/examples/main?urlpath=%2Fdesktop
      btn_class: "btn--primary btn--outline"
      btn_label: <i class="fas fa-rocket"></i> Try it here
      excerpt: |
          You cannot only easily use psyplot from scripts, it comes with a
          <a href="https://psyplot.readthedocs.io/projects/psyplot-gui/en/latest/">
            flexible graphical user interface to interactively explore your data
          </a>.

    - image_path: /assets/images/psyplot-framework.png
      alt: psyplot framework
      title: Flexible framework
      url: https://psyplot.readthedocs.io/en/latest/develop/framework.html
      btn_class: "btn--primary btn--outline"
      btn_label: <i class="fas fa-book"></i> Read more
      excerpt: |
          The psyplot framework is built for flexibility to tackle the different
          types of analysis questions that arise in pioneering research, and to
          continuously add more features.

    - image_path: /assets/images/logos.png
      alt: Logos
      title: Open Science
      url: "https://psyplot.readthedocs.io/en/latest/installing.html"
      btn_class: "btn--primary btn--outline"
      btn_label: <i class="fas fa-download"></i> Install now
      excerpt: |
          All packages are open-source, freely available, and developped
          transparently.
          <br>
          Install it via <code>pip</code> or <code>conda</code>,
          or <a href="https://github.com/psyplot" title="The psyplot GitHub organization">get the source code on GitHub</a>.
project_row:
    - title: psyplot
      image_path: /assets/images/logo.png
      alt: psyplot logo
      url: "https://psyplot.readthedocs.io"
      btn_class: "btn--primary btn--outline"
      btn_label: <i class="fas fa-book"></i> Documentation
      excerpt: |
          psyplot is the core package that defines the framework and data
          management. It provides the functionalities to decode CF- and UGRID-
          Conventions, the main API in the <code>psyplot.project</code> module.

    - title: psy-simple
      image_path: /assets/images/lines.svg
      alt: lines
      url: "https://psyplot.readthedocs.io/projects/psy-simple"
      btn_class: "btn--primary btn--outline"
      btn_label: <i class="fas fa-book"></i> Documentation
      excerpt: |
          psy-simple is a plugin for psyplot that defines various
          <a href="https://psyplot.readthedocs.io/projects/psy-simple/en/latest/plot_methods.html">plot methods</a>
          for the visualization of 1D- and 2D-data. It is the basis for more
          specialized plugins, such as psy-maps and psy-reg.

    - title: psy-maps
      image_path: /assets/images/map.svg
      alt: map
      url: "https://psyplot.readthedocs.io/projects/psy-maps"
      btn_class: "btn--primary btn--outline"
      btn_label: <i class="fas fa-book"></i> Documentation
      excerpt: |
          psy-maps is extends the functionalities of psy-simple using
          <a href="https://scitools.org.uk/cartopy/docs/latest/">cartopy</a>.
          With psy-maps, you can use
          <a href="https://psyplot.readthedocs.io/projects/psy-maps/en/latest/plot_methods.html">plot methods</a>
          to visualize regular and unstructured data on a map.

    - title: psyplot-gui
      image_path: /assets/images/psyplot-gui.png
      alt: psyplot GUI
      url: "https://psyplot.readthedocs.io/projects/psyplot-gui"
      btn_class: "btn--primary btn--outline"
      btn_label: <i class="fas fa-book"></i> Documentation
      excerpt: |
          psyplot-gui is building a GUI upon the psyplot framework for interactive
          analysis. Among many other features, it contains an in-process terminal,
          a help-explorer and tools to change the plots and project contents.

    - title: psy-view
      image_path: /assets/images/psy-view.png
      alt: psy-view widget
      url: "https://psyplot.readthedocs.io/projects/psy-view"
      btn_class: "btn--primary btn--outline"
      btn_label: <i class="fas fa-book"></i> Documentation
      excerpt: |
          psy-view provides a standalone widget for a simple investigation of
          netCDF file contents. Just like
          <a href="http://meteora.ucsd.edu/~pierce/ncview_home_page.html">ncview</a>
          it can be started as a standalone application, but is also embedded in
          the general psyplot GUI. It extends the functionalities of ncview
          with nicer, and more functional plotting methods.

    - title: psy-reg
      image_path: /assets/images/regression.svg
      alt: regression fits
      url: "https://psyplot.readthedocs.io/projects/psy-reg"
      btn_class: "btn--primary btn--outline"
      btn_label: <i class="fas fa-book"></i> Documentation
      excerpt: |
          psy-reg is a plugin built-upon psy-simple,
          <a href="https://www.statsmodels.org/stable/index.html">statsmodels</a>
          and <a href="https://www.scipy.org/scipylib/index.html">scipy</a> to
          fit regression models to your data.


---
## Key Features
{% include feature_row %}

## Projects

{% include feature_row id="project_row" type="center"%}

## Contribute
We are always looking for contributors providing new plugins, formatoptions,
code snippets, etc.! The [developers guide][devguide] provide some general
background on the framework. We are looking forward to your PR in one of our
[repositories on Github](github), or transform your code-snippets into
formatoptions if you post them in a new [issue][issues].

If you're just looking for a specific feature, please, do not hessitate to get
in touch with the psyplot developers via one of the following channels:

- Create an issue at the [bug tracker][issues]
- Chat with the developers [on gitter][gitter]
- Subscribe to the [mailing list][mailing list] and ask for support

We kindly ask you to adhere to the [code of conduct][coc]. Feel free to
checkout our [contribution guide][contrib] for more information, and a guide
about good bug reports.


[github]: https://github.com/psyplot
[devguide]: https://psyplot.readthedocs.io/en/latest/develop/index.html
[issues]: https://github.com/psyplot/psyplot/issues
[gitter]: https://gitter.im/psyplot/community
[mailing list]: https://www.listserv.dfn.de/sympa/subscribe/psyplot
[coc]: https://github.com/psyplot/psyplot/blob/master/CODE_OF_CONDUCT.md
[contrib]: https://github.com/psyplot/psyplot/blob/master/CONTRIBUTING.md
