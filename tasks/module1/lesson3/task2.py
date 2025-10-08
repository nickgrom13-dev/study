"""Вывести все простые числа от 2 до 100"""
import math

min_number = 2
max_number = 100

print(2)

while min_number <= max_number:
    i = 2
    square_root = math.ceil(math.sqrt(min_number))
    while i <= square_root:
        if not (min_number % i):
            break
        i += 1
        if i > square_root:
            print(min_number)
    min_number += 1
