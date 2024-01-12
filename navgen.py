#!/usr/bin/env python3

import os.path

import json

"""navgen
   Simple script that recursively walks a directory path and generates an MD
   scaffolding that enables nested TOC generation in Sphinx.

   USAGE
"""

def dir_tree(path):
  """
  dir_tree produces a directed graph representing the directory
  structure under [path]. The graph is represented as an adjacency list.

  Parameters:
    path (string): The path to the root directory


  Output:
    A dictionary containing an adjacency list correponding to the directory
    structure under [path].

  Example:
    dir_tree("rootDir")
    => {
      "rootDir": ["dirA", "dirB", "fileA"],
      "dirA": ["fileB"],
      "dirB": ["fileC", "dirC"],
      "dirC": [],
    }
  """

  # Check if path exists. Throw appropriate exception
  # Recursively build dictionary by appending files to list, recursing through
  # directories

  if not os.path.exists(path):
    raise FileNotFoundError(path)

  # Consider whether I can support a lone file
  if not os.path.isdir(path):
    return {}

  tree = {}

  children = os.listdir(path)

  tree[os.path.basename(path)] = children

  for child in children:
    fullpath = os.path.join(path, child)

    tree = {**tree, **dir_tree(fullpath)}

    # print(f'dir_tree({child}) => {ret}')


  return tree

def format_title(directory):
  """
  """

  return ""

def write_navfile(filename):
  """
  """

  return ""

if __name__ == "__main__":
  t = dir_tree("./site/Notes/Mathematics/Foundations")

  print(json.dumps(t, indent=2))
