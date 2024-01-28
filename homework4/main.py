import math


def correlation(array1, array2):
    n = len(array1)
    if n != len(array2):
        ValueError('Массивы должны быть одинаковой длины!')

    mean1 = sum(array1) / n
    mean2 = sum(array2) / n

    numerator = sum([(x - mean1) * (y - mean2) for x, y in zip(array1, array2)])
    denominator = math.sqrt(sum([((x - mean1) ** 2) * ((y - mean1) ** 2) for x, y in zip(array1, array2)]))

    corr = numerator / denominator

    return corr


array1 = [1, 2, 3, 4, 5]
array2 = [2, 3, 6, 8, 10]
print(correlation(array1, array2))
