#1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными

#Пример:

#67.82 -> 23
#0.56 -> 11

def get_number(input_string):
    while True:
        try:
            num = float(input(input_string))
            return num
        except ValueError:
            print("Вы ввели нге число. Повторите ввод")
number = get_number("Введите вещественное число:")
str_number = str(number)
sum_digit = 0
for i in str_number:
    if i.isdigit():
        sum_digit = sum_digit + int(i)
print(f"Сумма чисел равна {sum_digit}")