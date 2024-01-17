def multiplication_table(num):
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            print(f'{i} * {j} = {i * j}')
        print(' ')


num = int(input('Введите число: '))
multiplication_table(num)

# Выбрана процедурная парадигма для возможности использования кода в программе
