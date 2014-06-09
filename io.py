from os.path import isfile, join
from os import listdir
import re

# if ext is specified then pattern is ignored.
def get_all_file_names_from_dir(path_to_dir, ext=None, pattern=".*"):
  files = []
  if ext:
    pattern = ".*\.%s$" % ext
  for f in listdir(path_to_dir): 
    if isfile(join(path_to_dir, f)) and re.match(pattern, f):
      files.append(f)
  return files
