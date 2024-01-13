# Notes

This repository is the source used to build my notes site:

https://beautifultovarisch.github.io/Notes

which contains notes on various topics in Mathematics and Computer Science.

## Overview

The site content is written with [Obsidian](https://obsidian.md/). I run a few
scripts to generate navigation files and generate the HTML using [Sphinx](https://www.sphinx-doc.org/en/master/).

## Notes Content

I am currently investigating a working relationship between the [MyST](https://myst-parser.readthedocs.io/en/latest/) dialect of markdown and Obsidian's.
For the most part, the two get along nicely, but certain features like Obsidian
backlinks need to be parsed and translated.

## Getting Started

Install the required software before continuing:

|Software|Version|
|--------|-------|
|Python  |3.8.X  |
|Pip     |23.3.2 |
|Obsidian|1.5.3  |

Next, use pip to install dependencies:

```bash
pip install -r requirements.txt
```

This should be all that is required to manually build the site locally.

### Building the Sphinx Site

1. Generate the site navigation with `navgen.py`:

```bash
./navgen.py site/Notes site/nav
```

2. Run `sphinx-build` to generate the website assets:

```bash
make html
```

## TODO

- [ ] Cleanup `navgen.py`
  - [ ] Better support for regex ignore patterns
  - [ ] Better documentation
  - [ ] Dry-run Behavior
  - [ ] Debug mode, logging etc.
- [ ] Obsidian to MyST
  - [ ] Backlinks
  - [ ] Admonitions
  - [ ] Mermaid (or replace mermaid with other diagrams)
- [ ] Authoring Content
  - [ ] Better support for "live-reloading" or auto-building sphinx site on changes
  - [ ] Simple web server to shorten development feedback loop
