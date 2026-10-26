#!/usr/bin/env python3


if __name__ == '__main__':
    products = [
        {"name": "Laptop", "price": 89990, "discount": 10},
        {"name": "Mouse", "price": 2490, "discount": 15},
        {"name": "Keyboard", "price": 5490, "discount": 0},
        {"name": "Monitor", "price": 27990, "discount": 25},
    ]

    print("Базовый список товаров загружен.")
    print("Добавьте свой товар (или нажмите Enter, чтобы пропустить).")

    name = input("Название товара: ").strip()
    if name:
        try:
            price = float(input("Цена: ").strip())
            discount = float(input("Скидка (%): ").strip())
            products.append({"name": name, "price": price, "discount": discount})
            print(f"Товар '{name}' добавлен.")
        except ValueError:
            print("Ошибка: цена и скидка должны быть числами.")

    print("\nИтоговый список (с учетом скидки):")

    final_prices = lambda p: {
        **p,
        "final_price": p["price"] * (1 - p["discount"] / 100)
    }

    u_products = list(map(final_prices, products))

    sorted_products = sorted(u_products, key=lambda p: p["final_price"])

    for p in sorted_products:
        print(f"{p['name']}: {p['final_price']:.2f} руб. (Скидка: {p['discount']}%)")
