if __name__ == '__main__':
    while True:
        text = input("Введите 20 чисел через пробел:\n").strip()
        parts = text.replace(',', ' ').split()

        numbers = []
        has_error = False

        for p in parts:
            try:
                numbers.append(float(p))
            except ValueError:
                print(f"'{p}' — это не числа!!")
                has_error = True
        if not has_error and len(numbers) == 20:
            break
        else:
            print("Попробуйте еще раз (нужно ровно 20 чисел, без букв и лишних символов).\n")

    print("\nУра! Все верно")

    task1 = list(filter(lambda x: x % 3 == 0 and x % 9 != 0, numbers))
    print("\n1. Делятся на 3, но не на 9:", task1 , "Длина:", len(task1))
    task2 = list(filter(lambda x: abs(x) > 20, numbers))
    print("\n2. Модуль больше 20:", task2 , "Длина:", len(task2))

    task3 = list(filter(lambda x: (x % 3 == 0 and x % 9 != 0) and abs(x) > 20, numbers))
    print("\n3. Оба условия:", task3, "Длина:", len(task3))
