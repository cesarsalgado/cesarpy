from os.path import isfile, isdir, join
from os import listdir
import re
import json

def get_all_x_names_from_dir(path_to_dir, x_equals_file=None, pattern=".*", sort=True, withpath=False, numerical_sort=False):
    if x_equals_file != None:
        if x_equals_file:
            node_check = isfile
        else:
            node_check = isdir
    else:
        node_check = lambda x: True
    nodes = []
    node_name_list = listdir(path_to_dir)
    for node_name in node_name_list:
        path_node = join(path_to_dir, node_name)
        if node_check(path_node) and re.match(pattern, node_name):
            nodes.append(path_node if withpath else node_name)
    if sort:
        if numerical_sort:
            non_digit = re.compile(r'[^\d]+')
            nodes.sort(key=lambda s: int(non_digit.sub('', s)))
        else:
            nodes.sort()
    return nodes


# if ext is specified then pattern is ignored.
def get_all_file_names_from_dir(path_to_dir, ext=None, pattern=".*", sort=True, withpath=False, numerical_sort=False):
    if ext:
        pattern = ".*\.%s$" % ext
    return get_all_x_names_from_dir(path_to_dir, True, pattern, sort, withpath, numerical_sort)

def get_all_dir_names_from_dir(path_to_dir, pattern=".*", sort=True, withpath=False, numerical_sort=False):
    return get_all_x_names_from_dir(path_to_dir, False, pattern, sort, withpath, numerical_sort)

def save_dict_as_json(dict_, filename):
    with open(filename, 'w') as outfile:
        json.dump(dict_, outfile)

def load_dict_from_json(filename):
    with open(filename, 'r') as infile:
        dict_ = json.loads(infile.read())
        return dict_

def read_lines(path):
    with open(path, 'r') as f:
        return f.read().split('\n')
