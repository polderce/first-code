num = int(input('Введите кол-во чисел в послежовательности: '))
one = two = 1
print(one, two, end=' ')

n = 0
while n<num-2:
    one, two = two, one + two
    n += 1
    print(two, end=' ')
