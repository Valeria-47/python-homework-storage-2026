#!/usr/bin/env python3


def repeat(n:int):
    """
    Декоратор, который выполяет функцию n
    :param n: Количество повторений
    :return: Декоратор
    :rtype: function
    """
    def decorator(func):
        """
        Слой, принимающий функцию, которую нужно повторять
        :param func: Исходная функция-в данном случае 'add'
        :return: Функция-обертка, заменяющая исходную
        :rtype: function
        """

        def wrapper(*args, **kwargs):
            """
                   Функция, которая выполяет функцию n раз и собирает результат
                   :param args: Позиционные аргументы для исходной функции
                   :param kwargs: Именованные аргументы для исходной функции
                   :return: Список результатов выполнения функции
                   rtype: list
                   """
            results = []
            for i in range(n):
                print(f"Считаю овец (овца {i+1})")
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator

@repeat(3)
def add(a, b):
    """
                       Функция, которая складывает два числа
                       :param a: Первое число пользователя
                       :param b: Второе число пользователя
                       :return: Сумма двух чисел
                       rtype: int
                       """
    return a + b


if __name__ == '__main__':
    final_results = add(2, 3)
    print("\nСписок результатов:", final_results)
