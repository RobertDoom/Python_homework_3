# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

lst = list(map(int, input('Введите значения списка через пробел ').split()))
result = []
print(lst)
j = -1
for i in range(len(lst)//2):
    result.append(lst[i]*lst[j-i])
if len(lst) % 2 != 0:
    result.append(lst[len(lst)//2]**2)
print(f'Произведение пар чисел = {result}')
