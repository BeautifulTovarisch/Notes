#!/usr/bin/env python3

import os
import os.path
import argparse

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
  tree[key] = children

  for child in children:
    fullroot = os.path.join(root, child)

    tree = {**tree, **dir_tree(fullroot)}

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
  parser = argparse.ArgumentParser(description='Generate navigation files for a directory. ')

  parser.add_argument("root", default=os.getcwd(),
                      help="Path to root directory.")

  args = parser.parse_args()
  root = args.root

  if not os.path.exists(root):
    raise FileNotFoundError(root)

 # TODO: Proper error reporting.
  t = dir_tree(root)

  print(t)

