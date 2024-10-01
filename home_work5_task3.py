import timeit
import os


def boyer_moore_function(input_text, input_pattern):
    def build_shift_table(pattern):
        """Створити таблицю зсувів для алгоритму Боєра-Мура."""
        table = {}
        length = len(pattern)
        # Для кожного символу в підрядку встановлюємо зсув рівний довжині підрядка
        for index, char in enumerate(pattern[:-1]):
            table[char] = length - index - 1
        # Якщо символу немає в таблиці, зсув буде дорівнювати довжині підрядка
        table.setdefault(pattern[-1], length)
        return table

    def boyer_moore_search(text, pattern):
        # Створюємо таблицю зсувів для патерну (підрядка)
        shift_table = build_shift_table(pattern)
        i = 0  # Ініціалізуємо початковий індекс для основного тексту

        # Проходимо по основному тексту, порівнюючи з підрядком
        while i <= len(text) - len(pattern):
            j = len(pattern) - 1  # Починаємо з кінця підрядка

            # Порівнюємо символи від кінця підрядка до його початку
            while j >= 0 and text[i + j] == pattern[j]:
                j -= 1  # Зсуваємось до початку підрядка

            # Якщо весь підрядок збігається, повертаємо його позицію в тексті
            if j < 0:
                return i  # Підрядок знайдено

            # Зсуваємо індекс i на основі таблиці зсувів
            # Це дозволяє "перестрибувати" над неспівпадаючими частинами тексту
            i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

        # Якщо підрядок не знайдено, повертаємо -1
        return -1

    position = boyer_moore_search(input_text, input_pattern)
    return position


def rabin_karp_function(input_text, input_pattern):
    def polynomial_hash(s, base=256, modulus=101):
        """Повертає поліноміальний хеш рядка s."""
        n = len(s)
        hash_value = 0
        for i, char in enumerate(s):
            power_of_base = pow(base, n - i - 1) % modulus
            hash_value = (hash_value + ord(char) * power_of_base) % modulus
        return hash_value

    def rabin_karp_search(main_string, substring):
        # Довжини основного рядка та підрядка пошуку
        substring_length = len(substring)
        main_string_length = len(main_string)

        # Базове число для хешування та модуль
        base = 256
        modulus = 101

        # Хеш-значення для підрядка пошуку та поточного відрізка в основному рядку
        substring_hash = polynomial_hash(substring, base, modulus)
        current_slice_hash = polynomial_hash(
            main_string[:substring_length], base, modulus)

        # Попереднє значення для перерахунку хешу
        h_multiplier = pow(base, substring_length - 1) % modulus

        # Проходимо крізь основний рядок
        for i in range(main_string_length - substring_length + 1):
            if substring_hash == current_slice_hash:
                if main_string[i:i+substring_length] == substring:
                    return i

            if i < main_string_length - substring_length:
                current_slice_hash = (current_slice_hash -
                                      ord(main_string[i]) * h_multiplier) % modulus
                current_slice_hash = (
                    current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
                if current_slice_hash < 0:
                    current_slice_hash += modulus

        return -1

    position = rabin_karp_search(input_text, input_pattern)
    return position


def knut_morris_pratt_function(input_text, input_pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps

    def kmp_search(main_string, pattern):
        M = len(pattern)
        N = len(main_string)
        lps = compute_lps(pattern)
        i = j = 0
        while i < N:
            if pattern[j] == main_string[i]:
                i += 1
                j += 1
            elif j != 0:
                j = lps[j - 1]
            else:
                i += 1

            if j == M:
                return i - j

        return -1  # якщо підрядок не знайдено

    postion = kmp_search(input_text, input_pattern)
    return postion


def r(func):
    return round(func, 6)


times = {}
times_2 = {}
file1 = open("стаття 1.txt", "r")
original_text = file1.read()
search_pattern = "жадібні алгоритми"
# boyer_moore
time_boyer_moore_fined = timeit.timeit(
    f"output={boyer_moore_function(original_text, search_pattern)}")
times["time_boyer_moore_fined"] = r(time_boyer_moore_fined)

# rabin_karp
time_rabin_karp_fined = timeit.timeit(
    f"output={rabin_karp_function(original_text, search_pattern)}")
times["time_rabin_karp_fined"] = r(time_rabin_karp_fined)

# knut_morris_pratt
time_knut_morris_pratt_fined = timeit.timeit(
    f"output={knut_morris_pratt_function(original_text, search_pattern)}")
times["time_knut_morris_pratt_fined"] = r(time_knut_morris_pratt_fined)


search_pattern = "test fabulas"
# boyer_moore
time_boyer_moore_not_fined = timeit.timeit(
    f"output={boyer_moore_function(original_text, search_pattern)}")
times["time_boyer_moore_not_fined"] = r(time_boyer_moore_not_fined)

# rabin_karp
time_rabin_karp_not_fined = timeit.timeit(
    f"output={rabin_karp_function(original_text, search_pattern)}")
times["time_rabin_karp_not_fined"] = r(time_rabin_karp_not_fined)

# knut_morris_pratt
time_knut_morris_pratt_not_fined = timeit.timeit(
    f"output={knut_morris_pratt_function(original_text, search_pattern)}")
times["time_knut_morris_pratt_not_fined"] = r(time_knut_morris_pratt_not_fined)

print(f"Для {file1.name}:")
for key, values in times.items():
    print(key, values)

min_1 = min(times.values())
print(f"Швидкий алгорітм для {file1.name}:", min_1)


file2 = open("стаття 2.txt", "r")
original_text_2 = file2.read()
search_pattern_2 = "Структура розгорнутого списку"
# boyer_moore
time_boyer_moore_fined_2 = timeit.timeit(
    f"output={boyer_moore_function(original_text_2, search_pattern_2)}")
times_2["time_boyer_moore_fined_2"] = r(time_boyer_moore_fined_2)

# rabin_karp
time_rabin_karp_fined_2 = timeit.timeit(
    f"output={rabin_karp_function(original_text_2, search_pattern_2)}")
times_2["time_rabin_karp_fined_2"] = r(time_rabin_karp_fined_2)

# knut_morris_pratt
time_knut_morris_pratt_fined_2 = timeit.timeit(
    f"output={knut_morris_pratt_function(original_text_2, search_pattern_2)}")
times_2["time_knut_morris_pratt_fined_2"] = r(time_knut_morris_pratt_fined_2)


search_pattern_2 = "test fabulas"
# boyer_moore
time_boyer_moore_not_fined_2 = timeit.timeit(
    f"output={boyer_moore_function(original_text_2, search_pattern_2)}")
times_2["time_boyer_moore_not_fined_2"] = r(time_boyer_moore_not_fined_2)

# rabin_karp
time_rabin_karp_not_fined_2 = timeit.timeit(
    f"output={rabin_karp_function(original_text_2, search_pattern_2)}")
times_2["time_rabin_karp_not_fined_2"] = r(time_rabin_karp_not_fined_2)

# knut_morris_pratt
time_knut_morris_pratt_not_fined_2 = timeit.timeit(
    f"output={knut_morris_pratt_function(original_text_2, search_pattern_2)}")
times_2["time_knut_morris_pratt_not_fined_2"] = r(
    time_knut_morris_pratt_not_fined_2)

print(f"Для {file2.name}:")
for key, values in times_2.items():
    print(key, values)

min_2 = min(times_2.values())
print(f"Швидкий алгорітм {file2.name}:", min_2)
print(f"Найшвидший алгорітм", min(min_1, min_2))
