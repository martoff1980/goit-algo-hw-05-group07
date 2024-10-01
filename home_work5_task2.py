def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    counter = 0
    while low <= high:
        mid = int((high + low) // 2)
        counter += 1
        cur_value = arr[mid]
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if cur_value < x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif cur_value > x:
            high = mid - 1

        # інакше x присутній на позиції і повертаємо його
        else:
            return (counter, arr[mid+1])

    # якщо елемент не знайдений
    if mid == len(arr)-1:
        mid -= 1
    return (counter, arr[mid+1])


arr = [1.1, 1.3, 2.5, 3.8, 4.6, 5.9]

result = binary_search(arr, 6)
print(result)
