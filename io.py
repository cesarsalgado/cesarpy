from os.path import isfile, join
from os import listdir
import re

# if ext is specified then pattern is ignored.
def get_all_file_names_from_dir(path_to_dir, ext=None, pattern=".*", sort=False, withpath=False):
  files = []
  if ext:
    pattern = ".*\.%s$" % ext
  for f in listdir(path_to_dir): 
    pathfile = join(path_to_dir, f)
    if isfile(pathfile) and re.match(pattern, f):
      files.append(pathfile if withpath else f)
  if sort:
    files.sort()
  return files
