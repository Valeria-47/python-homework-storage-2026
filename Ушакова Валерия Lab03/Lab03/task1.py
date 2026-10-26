#!/usr/bin/env python3


classify_number = lambda x: (
    "ЭТО СТРОКА, а не числа!!" if not isinstance(x, (int, float))
    else (
        "Нужно ЦЕЛОЕ число" if isinstance(x, float) and not x.is_integer()
        else (
            ("positive even" if x % 2 == 0 else "positive odd") if x > 0
            else ("negative" if x < 0 else "zero")
        )
    )
)

if __name__ == '__main__':
    text = input("Введите числа через пробел:\n").strip()
    parts = text.replace(',', ' ').split()

    print("\nРезультаты:")
    for p in parts:
        try:
            num_f = float(p)
            if num_f.is_integer():
                num = int(num_f)
            else:
                num_f = float(p)
            print(f"{num_f} -> {classify_number(num_f)}")
        except ValueError:
            print(f"'{p}' -> {classify_number(p)}")
