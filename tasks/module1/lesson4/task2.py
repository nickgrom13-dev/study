"""С клавиатуры вводятся N чисел. Составьте программу, которая определяет количество отрицательных,
количество положительных и количество нулей среди введенных чисел. Значение N вводится с клавиатуры.
При вводе нечислового значения вывести сообщение об ошибке и просим ввести повторно именно числовое значение.
Используйте цикл for."""

number_count =  5
negative_count = positive_count = zero_count = 0

for i in range(1, number_count + 1):
    while 1:
        number = input(f"Введите {i}-ое число\n")
        """введем промежуточную переменную number_check, чтобы проверить корректность ввода еще и отрицательного числа,
        так как метод isdigit проверяет, что строка состоит только из цифр, не учитывая знак у отрицательного числа"""
        number_check = number.strip("-") if number.find("-") == 0 and number.count("-") == 1 else number
        if number_check.isdigit():
            if int(number) < 0:
                negative_count += 1
            elif int(number) > 0:
                positive_count += 1
            else:
                zero_count += 1
            break
        print(f"Ошибка при вводе {i}-ого числа. Повторите попытку.")
print(f"Было введено {number_count} чисел. Среди них отрицательных: {negative_count}, "
       f"положительных: {positive_count}, нулей: {zero_count}")
