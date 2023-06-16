from pathlib import Path

import file_operations.fill_numbers as fill_numbers
from file_operations.rename_files import rename_files
from file_operations.files_generate import files_generate, files_creater, clear_dir
from file_operations.union_names_nums import union_names_nums
from file_operations.names_gen import names_gen
from file_operations.fill_numbers import fill_numbers

if __name__ == '__main__':
    # task1
    # fill_numbers(5, 'numbers.txt')

    # task2
    # names_gen(3, 'names.txt')

    # task3
    # union_names_nums('numbers.txt', 'names.txt', 'result.txt')

    path = 'dir_for_generation'

    # task4
    # clear_dir(path)
    # files_generate(path, 'txt')

    # task5
    # clear_dir(path)
    # files_creater(path, 11, 'txt', 'pdf', 'doc', 'img')

    # home_task:
    rename_files(path, 'end', 2, 'txt', 'xml', (1, 4))

    print()
