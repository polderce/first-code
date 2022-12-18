num=int(input('Введите положительное число: '))
if num>0:
   fact=1
else:
    print('Число должно быть положительным!')
    raise SystemExit
while num>1:
    fact=fact*num
    num=num-1
print('Факториал равен', fact)

