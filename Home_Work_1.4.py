#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
def bin_of_numbers_1(number: int) -> str:
    if type(number) in [int]:
        empty_string = ''
        while number > 0:
            empty_string+= str(number % 2)
            number //= 2
        return empty_string[::-1]
    return -1

bin_of_numbers_1(3)


assert bin_of_numbers_1(3) == '11'
assert bin_of_numbers_1(45) == '101101'
assert bin_of_numbers_1(2) == '10'
assert bin_of_numbers_1('3') == -1
assert bin_of_numbers_1([45]) == -1
assert bin_of_numbers_1((45,)) == -1
assert bin_of_numbers_1({45}) == -1

# 2 Вариант
def bin_of_numbers_2(number: int) -> str:
    if type(number) in [int]:
        return (bin(number))[2:]
    return -1

bin_of_numbers_2(45)

assert bin_of_numbers_2(3) == '11'
assert bin_of_numbers_2(45) == '101101'
assert bin_of_numbers_2(2) == '10'
assert bin_of_numbers_2('3') == -1
assert bin_of_numbers_2([45]) == -1
assert bin_of_numbers_2((45,)) == -1
assert bin_of_numbers_2({45}) == -1