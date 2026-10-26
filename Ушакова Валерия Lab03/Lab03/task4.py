#!/usr/bin/env python3


if __name__ == '__main__':
    text = input("Введите слова через пробел:\n")
    words = text.split()

    long_words = list(filter(lambda w: len(w) >= 7, words))
    print("Слова >= 7 символов:", long_words)

    pairs = list(map(lambda w: (w, len(w)), long_words))
    print("Пары (слово, длина):", pairs)

    if long_words:
        longest_w = max(long_words, key=len)
        print("Самое длинное слово:", longest_w)
    else:
        print("Самое длинное слово: (нет слов)")

    total_letters = 0
    for w in long_words:
        total_letters += len(w)
    print("Всего букв в этих словах:", total_letters)
