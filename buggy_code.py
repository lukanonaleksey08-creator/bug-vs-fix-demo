# buggy_code.py — код С ОШИБКОЙ
# Задача: найти среднее арифметическое чисел в списке

def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)   # ❌ ОШИБКА: деление на ноль, если список пустой


def get_max(numbers):
    max_val = numbers[0]          # ❌ ОШИБКА: IndexError при пустом списке
    for n in numbers:
        if n > max_val:
            max_val = n
    return max_val


if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]
    print("Среднее:", average(data))
    print("Максимум:", get_max(data))

    empty = []
    print("Среднее пустого:", average(empty))   # 💥 упадёт здесь
