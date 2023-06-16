'''Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
'''

from pathlib import Path
import random as rnd

MIN_NUMBER = -1000
MAX_NUMBER = 1000


def fill_numbers(count_lines: int, file_name: str | Path):
    with open(file_name, 'w', encoding="utf-8") as f:
        for _ in range(count_lines):
            f.write(f'{rnd.randint(MIN_NUMBER, MAX_NUMBER + 1)} | {rnd.uniform(MIN_NUMBER, MAX_NUMBER)}\n')
