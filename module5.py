num=int(input('Введите размер списка: '))
nums=[5*k + 3 for k in range(1,num+1)]
print('Список в прямом порядке:', list(nums))
print('Список в обратном порядке:', list(reversed(nums)))