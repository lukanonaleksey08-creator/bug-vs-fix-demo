# fixed_code.py — код БЕЗ ОШИБКИ
# Задача: найти среднее арифметическое чисел в списке

def average(numbers):
    if not numbers:                # ✅ проверка на пустой список
        return 0
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


def get_max(numbers):
    if not numbers:                # ✅ защита от IndexError
        return None
    max_val = numbers[0]
    for n in numbers:
        if n > max_val:
            max_val = n
    return max_val


if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]
    print("Среднее:", average(data))
    print("Максимум:", get_max(data))

    empty = []
    print("Среднее пустого:", average(empty))   # ✅ вернёт 0
    print("Максимум пустого:", get_max(empty))  # ✅ вернёт None
