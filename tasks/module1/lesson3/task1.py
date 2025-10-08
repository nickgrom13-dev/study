"""Напечатать таблицу умножения от 2 до 5"""

min_number = 2
max_number = 5

row_number = min_number
while row_number <= 9:
    column_number = min_number
    while column_number <= max_number:
        print(f"{column_number} x {row_number} = {column_number * row_number} \t\t", end='')
        column_number += 1
    print()
    row_number += 1