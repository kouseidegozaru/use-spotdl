#1-2 - 5-30 - Wild Honey Pie - Remastered 2009'
#トラック番号を二桁の0埋めの数字にするコード

import os
import re

def all_file_paths(dir_path):
    file_paths = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

def get_file_name(path):
    return os.path.basename(path)

def new_name(path):
    file_name = get_file_name(path)
    number_period_index = first_non_num_hyphen_space_index(file_name)
    number_string = get_first_n_chars(file_name, number_period_index)
    name_string = remove_first_n_chars(file_name, number_period_index)
    padded_number_string = zero_pad_numbers(number_string)
    return padded_number_string + name_string

def rename(path, new_file_name):
    return os.path.join(os.path.dirname(path), new_file_name)

def first_non_num_hyphen_space_index(s):
    for i, c in enumerate(s):
        if not (c.isdigit() or c == '-' or c == ' '):
            return i
    raise ValueError("No non-numeric character found in the string.")

def zero_pad_numbers(s):
    return re.sub(r'\d+', lambda m: m.group().zfill(2), s)

def remove_first_n_chars(s, n):
    return s[n:]

def get_first_n_chars(s, n):
    return s[:n]

if __name__ == "__main__":
    dir_path = input("Enter the directory path: ")
    file_paths = all_file_paths(dir_path)
    for file_path in file_paths:
        new_file_path = rename(file_path, new_name(file_path))
        if file_path != new_file_path:
            os.rename(file_path, new_file_path)