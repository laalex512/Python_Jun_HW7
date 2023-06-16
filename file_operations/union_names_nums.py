'''Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало.
'''


def read_line(f):
    line = f.readline()
    if line == '':
        f.seek(0)
        return read_line(f)
    return line[:-1]


def union_names_nums(numbers_file: str, names_file: str, result_file: str):
    with (
        open(numbers_file, 'r', encoding='utf-8') as f_nums,
        open(names_file, 'r', encoding='utf-8') as f_names,
        open(result_file, 'w', encoding='utf-8') as res_file
        ):
        len_nums = sum(1 for _ in f_nums)
        len_names = sum(1 for _ in f_names)
        f_nums.seek(0)
        f_names.seek(0)
        for i in range(max(len_names, len_nums)):
            current_name = read_line(f_names)
            current_num = read_line(f_nums)

            current_num = int(current_num.split(" | ")[0]) * float(current_num.split(" | ")[1])
            if current_num >= 0:
                line = f'{current_name.upper()} : {str(round(current_num))}\n'
            else:
                line = f'{current_name.lower()} : {str(abs(current_num))}\n'
            res_file.write(line)
