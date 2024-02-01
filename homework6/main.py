from typing import List


def binary_search(arr: List[int], number: int) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == number:
            return mid
        elif arr[mid] < number:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(f"Исходный массив: {arr}")
    number = int(input("Введите искомый элемент: "))
    result = binary_search(arr, number)

    if result == -1:
        print("Искомый элемент не найден")
    else:
        print(f"Искомый элемент: {number} найден по индексу: {result}")
