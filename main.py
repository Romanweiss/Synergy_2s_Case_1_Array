from array import array
import random


def main():
    # генерация размерности массива (от 10 до 30)
    N = random.randint(10, 30)

    # генерация одномерного массива A
    A = array('i', (random.randint(-1000, 1000) for _ in range(N)))

    min_value = min(A)
    max_value = max(A)

    min_index = A.index(min_value)
    max_index = A.index(max_value)

    start = min(min_index, max_index) + 1
    end = max(min_index, max_index)

    negative_sum = sum(x for x in A[start:end] if x < 0)

    print(f"Размерность массива: {N}")
    print("Массив:", A.tolist())
    print("Минимальный элемент:", min_value)
    print("Максимальный элемент:", max_value)
    print("Сумма отрицательных элементов между ними:", negative_sum)


if __name__ == "__main__":
    main()