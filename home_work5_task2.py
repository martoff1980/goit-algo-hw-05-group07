def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    mid = 0
    counter = 0
    upper_bound = None

    while low <= high:
        mid = (high + low) // 2
        counter += 1
        cur_value = arr[mid]

        # Якщо знайшли точний елемент, повертаємо його
        if arr[mid] == x:
            return (counter, arr[mid])

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if cur_value < x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif cur_value > x:
            high = mid - 1

    # Після завершення циклу low вказує на перший елемент, який більше x
    if low < len(arr):
        upper_bound = arr[low]

    if upper_bound is None:
        upper_bound = arr[-1]

    return (counter, upper_bound)


arr = [1.1, 1.3, 2.5, 3.8, 4.6, 5.9]
# Test-cases
target = 2
result = binary_search(arr, target)
print(target, result)

target = 3.0
result = binary_search(arr, target)
print(target, result)

target = 4
result = binary_search(arr, target)
print(target, result)

target = 4.6
result = binary_search(arr, target)
print(target, result)

target = 5
result = binary_search(arr, target)
print(target, result)

target = 5.9
result = binary_search(arr, target)
print(target, result)

target = 6
result = binary_search(arr, target)
print(target, result)

target = 20
result = binary_search(arr, target)
print(target, result)

arr = [1, 2, 4, 5, 6, 8, 10]
target = 7
result = binary_search(arr, target)
print(result)
