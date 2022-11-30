# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
def dif_between_the_max_and_min_value(list_a) -> float:
    if type(list_a) in [list] and all(type(x) for x in list_a):
        temp = list(map(lambda x: round((float(x) - int(x)), 2), list_a))
        return max(temp)-min(temp)
    return -1

dif_between_the_max_and_min_value([1.1, 1.2, 3.1, 10.01])