# psyplot landing page repository

This repository contains the source code for the
[psyplot landing page](https://psyplot.github.io). It is based on the
[Minimal Mistakes Jekyll theme](https://github.com/mmistakes/minimal-mistakes)
and hosted with Github Pages. The static website is build automatically on Github
but you can also build it locally.

## Local installation
As we cannot host multiple versions of this site with GitHub Pages (generated from the
master branch), you should build the website locally and test the implemented
changes (or the reviewer in the pull request does it, this is fine as well).
To build this site locally, you need to use the command line:

1. Install ruby for your platform
2. Install `bundle` via `gem install bundler`
3. `cd` to the clone of this repository
4. Run `bundle install`
5. Serve the site locally via `bundle exec jekyll serve`
6. Visit the site in the browser via http://localhost:4000

## Preview the Site on CircleCI

We use CircleCI to preview the site for pull requests, and this is controlled by the files
in the [.circleci](.circleci) folder. To use CircleCI, you will need to
make sure you are logged in to the service and following the repository. When you select a build
associated with a pull request, click on the "Artifacts" tab, and select a static file to open
and preview in your browser.

## Testing the installation

We use the [html-proofer](https://github.com/gjtorikian/html-proofer/) to test for
broken links, etc. To run the tests locally, you need to install it (see
[Local installation](#local-installation)) and run the tests via executing
`bundle exec rake`

## License

The contents of the psyplot website and its source code repository is published
under the Creative Commons Attribution 4.0 International Public License (CC BY 4.0).
See the [LICENSE](LICENSE) file for more details.

Copyright (c) 2020, Philipp S. Sommer.

The original software for creating this website, the Minimal Mistakes Jekyll
Theme, is distributed under the MIT license, see
https://github.com/mmistakes/minimal-mistakes#license.

The [MIT license](http://opensource.org/licenses/MIT) also applies for the
`_includes` and `_layouts` folder in this repository.
