'''Напишите функцию группового переименования файлов. Она должна:
✔ принимать параметр желаемое конечное имя файлов.
При переименовании в конце имени добавляется порядковый номер.
✔ принимать параметр количество цифр в порядковом номере.
✔ принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
✔ принимать параметр расширение конечного файла.
✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
[3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
'''
import os


def rename_files(
        path: str, new_name: str, count_digits: int, orig_ext: str,
        new_ext: str, orig_save_symbols: tuple[int, int]
        ):
    files_to_rename = [i for i in os.listdir(path) if i[-3:] == orig_ext]
    counter = 1
    for file in files_to_rename:
        new_filename = ''
        for i in range(min(orig_save_symbols) - 1, max(orig_save_symbols)):
            new_filename += file[i]
        new_filename += new_name
        name_counter = str(counter)
        for _ in range(len(str(counter)), count_digits):
            name_counter = '0' + name_counter
        counter += 1
        new_filename += f'{name_counter}.{new_ext}'
        os.rename(f'{path}/{file}', f'{path}/{new_filename}')
