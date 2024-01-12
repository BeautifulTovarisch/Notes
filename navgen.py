#!/usr/bin/env python3

import os
import os.path
import argparse

import json

from jinja2 import Environment, FileSystemLoader, select_autoescape

"""navgen
   Simple script that recursively walks a directory path and generates a nav
   scaffolding for use in creating a Sphinx Table of Contents.
"""

def dir_tree(root):
  """
  dir_tree produces a directed graph representing the directory
  structure under [root]. The graph is represented as an adjacency list.

  Parameters:
    root (string): The root to the root directory


  Output:
    A dictionary containing an adjacency list correponding to the directory
    structure under [root].

  Example:
    dir_tree("rootDir")
    => {
      "rootDir": ["dirA", "dirB", "fileA"],
      "dirA": ["fileB"],
      "dirB": ["fileC", "dirC"],
      "dirC": [],
    }
  """

  # Basis. I don't need the files themselves in the list of keys
  if not os.path.isdir(root):
    return {}

  tree = {}

  children = os.listdir(root)

  key = os.path.basename(os.path.normpath(root))
  tree[key] = []

  for child in children:
    fullroot = os.path.join(root, child)
    tree[key].append(fullroot)

    tree = {**tree, **dir_tree(fullroot)}

  return tree

# Configure Jinja environment and fetch nav template
def get_template(templatesDir, navTemplate):
  """
  """

  env = Environment(
    loader=FileSystemLoader(templatesDir),
    autoescape=select_autoescape()
  )

  template = env.get_template(navTemplate)

  return template

# TODO: Better doc comments.
def nav_gen(tree, template, dest):
  """
  nav_gen processes a directed graph representing a directory tree and
  writes corresponding navigation files to [dest].

  Parameters:
    tree (dictionary): An adjacency list representing a directory structure.
    dest (path): An adjacency list representing a directory structure.

  Output:
    None

  Example:
    t = {
      "rootDir": ["dirA", "dirB", "fileA"],
      "dirA": ["fileB"],
      "dirB": ["fileC", "dirC"],
      "dirC": [],
    }

    traverse_tree(t)
    => rootDir.md
    => dirA.md
    => dirB.md
    => dirC.md

  where fileX appears in the Table of Contents of the parent nav markdown.
  """

  for key in tree:
    with open(f'{dest}/{key}.md', 'a') as nav:
      nav.write(template.render(title=key, files=tree[key]))

# TODO: Add support for ignoring files (--gitignore, etc.)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Generate navigation files for a directory. ')

  parser.add_argument("root", default=os.getcwd(),
                      help="Path to root directory.")

  parser.add_argument("dest",
                      help="Destination directory of navigation files.")

  args = parser.parse_args()

  root = args.root
  dest = args.dest

  # TODO: Proper error handling
  if not os.path.exists(root):
    raise FileNotFoundError(root)

  if not os.path.exists(dest):
    os.makedirs(dest, exist_ok=True)

  # TODO: Add an arg to specify nav template.
  template = get_template("_templates", "nav.md")

  t = dir_tree(root)

  nav_gen(t, template, dest)
