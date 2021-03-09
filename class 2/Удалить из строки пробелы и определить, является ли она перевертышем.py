n = input('Введи предложение')
x = n.replace(' ', '')

print(x)

if n == n[::-1]:
    print('Перевертыш')
