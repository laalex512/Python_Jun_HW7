'''Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
'''
from pathlib import Path
import string
import random as rnd

MIN_LENGTH = 4
MAX_LENGTH = 7
VOWELS = set('aeiou')
CONSONANT = set(string.ascii_lowercase) - VOWELS


def names_gen(count: int, file_name: str | Path):
    with open(file_name, 'w') as f:
        f.write("")
    for _ in range(count):
        current_name = ''
        for _ in range(rnd.randint(MIN_LENGTH, MAX_LENGTH) // 2):
            current_name += rnd.choice(list(CONSONANT))
            current_name += rnd.choice(list(VOWELS))
        current_name = current_name.capitalize()
        with open(file_name, 'a', encoding="utf-8") as f:
            f.write(current_name + '\n')
