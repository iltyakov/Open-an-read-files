import os
from operator import itemgetter

BASE_PATH = os.getcwd()
files = os.listdir(BASE_PATH)
file_list = [file for file in files if file.endswith('.txt')]
file_list_files = file_list[1:]

def get_total_file(files):
    result1 = {}
    for file in files:
        with open(file, encoding='utf-8') as ex_file:
            len_list = []
            len_file = len(ex_file.readlines())
            len_list.append(len_file)
            result1[file] = len_list[0]
            result1 = dict(sorted(result1.items(), key=itemgetter(1)))
    for file_name, len_file_lines in result1.items():
        with open('final_file.txt', 'a', encoding='utf-8') as f, open(file_name, 'r', encoding='utf-8') as choose_file:
            f.write(f'{file_name}\n{len_file_lines}\n{" ".join(choose_file.readlines())}\n')

    return
get_total_file(file_list_files)