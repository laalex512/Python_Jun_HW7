'''Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.
'''
import os
import random
import secrets
import shutil
import string
from pathlib import Path


def clear_dir(path):
    shutil.rmtree(path)
    Path(path).mkdir()


def files_generate(path, ext: str, len_min=6, len_max=30, bytes_min=256, bytes_max=4096, count=42):
    if path not in os.listdir('.'):
        Path(path).mkdir(parents=True)
    for _ in range(count):
        file_name = path + '/'
        for _ in range(random.randint(len_min, len_max + 1)):
            file_name += random.choice(string.ascii_lowercase)
        file_name += f'.{ext}'

        with open(file_name, 'wb') as f:
            f.write(secrets.token_bytes(random.choice(range(bytes_min, bytes_max))))


'''Задание №5
✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.'''


def files_creater(path, total_count: int, *args):
    extensions = args
    len_args = len(extensions)
    if (len_args * (len_args + 1) // 2) > total_count:
        print('количество файлов слишком мало для такого количества расширений')
    else:
        counts = [i + 1 for i in range(total_count - 1)]
        files_extensions = dict()
        '''Максимум, что придумал по уникальности количества файлов для каждого расширения. Единственный момент 
        совпадения может случаться при последнем расширении, которое не в цикле. Как это устранить - фантазии не 
        хватает) Это условие, конечно, - нет слов))'''
        remaining_count = total_count
        for extension in extensions[:-1]:
            while True:
                count = random.randint(1, remaining_count // 2)
                if count in files_extensions.values() or remaining_count - count < 2:
                    continue
                else:
                    break
            files_extensions[extension] = count
            remaining_count -= count
        files_extensions[extensions[-1]] = remaining_count

        for extension, count in files_extensions.items():
            files_generate(path, extension, len_max=8, count=count)
