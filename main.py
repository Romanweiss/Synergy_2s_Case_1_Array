from array import array
import random


TYPE_OPTIONS = {
    "1": "int",
    "2": "float",
    "3": "mixed",
}


def choose_number_type():
    print("Выберите тип чисел в массиве:")
    print("1 - int (целые числа)")
    print("2 - float (вещественные числа)")
    print("3 - mixed (смешанный тип: int и float)")

    while True:
        choice = input("Введите 1, 2 или 3: ").strip()
        if choice in TYPE_OPTIONS:
            return TYPE_OPTIONS[choice]
        print("Некорректный выбор. Пожалуйста, введите 1, 2 или 3.")


def random_int():
    return random.randint(-1000, 1000)


def random_float():
    return round(random.uniform(-1000, 1000), 2)


def random_mixed_number():
    if random.choice((True, False)):
        return random_int()
    return random_float()


def generate_array(size, number_type):
    if number_type == "int":
        return array("i", (random_int() for _ in range(size)))
    if number_type == "float":
        return array("d", (random_float() for _ in range(size)))
    return [random_mixed_number() for _ in range(size)]


def as_list(values):
    if isinstance(values, array):
        return values.tolist()
    return values


def calculate_negative_sum_between_extremes(values):
    min_value = min(values)
    max_value = max(values)

    min_index = values.index(min_value)
    max_index = values.index(max_value)

    start = min(min_index, max_index) + 1
    end = max(min_index, max_index)

    negative_sum = sum(x for x in values[start:end] if x < 0)
    return min_value, max_value, negative_sum


def format_number(value):
    if isinstance(value, float):
        return f"{value:.2f}"
    return str(value)


def format_array(values):
    return "[" + ", ".join(format_number(value) for value in values) + "]"


def main():
    number_type = choose_number_type()

    # Размерность массива (от 10 до 30)
    size = random.randint(10, 30)
    values = as_list(generate_array(size, number_type))

    min_value, max_value, negative_sum = calculate_negative_sum_between_extremes(values)

    print()
    print(f"Выбранный тип: {number_type}")
    print(f"Размерность массива: {size}")
    print("Массив:", format_array(values))
    print("Минимальный элемент:", format_number(min_value))
    print("Максимальный элемент:", format_number(max_value))
    print("Сумма отрицательных элементов между ними:", format_number(negative_sum))


if __name__ == "__main__":
    main()
