from os.path import isfile, isdir, join
from os import listdir
import re

def get_all_x_names_from_dir(path_to_dir, x_equals_file=None, pattern=".*", sort=True, withpath=False):
  if x_equals_file != None:
    if x_equals_file:
      node_check = isfile
    else:
      node_check = isdir
  else:
    node_check = lambda x: True
  nodes = []
  for node_name in listdir(path_to_dir): 
    path_node = join(path_to_dir, node_name)
    if node_check(path_node) and re.match(pattern, node_name):
      nodes.append(path_node if withpath else node_name)
  if sort:
    nodes.sort()
  return nodes


# if ext is specified then pattern is ignored.
def get_all_file_names_from_dir(path_to_dir, ext=None, pattern=".*", sort=True, withpath=False):
  if ext:
    pattern = ".*\.%s$" % ext
  return get_all_x_names_from_dir(path_to_dir, True, pattern, sort, withpath)

def get_all_dir_names_from_dir(path_to_dir, pattern=".*", sort=True, withpath=False):
  return get_all_x_names_from_dir(path_to_dir, False, pattern, sort, withpath)
