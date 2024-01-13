def sort_list_imperative(numbers):
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)


numbers_list = [9, 8, 1, 4, 5, 3]
print(sort_list_imperative(numbers_list))
print(sort_list_declarative(numbers_list))