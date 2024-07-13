while True:
    input_string = input("Введіть рядок для перетворення на хештег (або 'quit' для виходу): ")

    if input_string.lower() == 'quit':
        break

    # Видаляємо пунктуацію та розділяємо рядок на слова
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    words = ''.join(char for char in input_string if char not in punctuation).split()

    # Перетворюємо кожне слово, роблячи першу літеру великою
    capitalized_words = [word.capitalize() for word in words]

    # Об'єднуємо слова та додаємо '#' на початку
    hashtag = '#' + ''.join(capitalized_words)

    # Обрізаємо до 140 символів, якщо потрібно
    hashtag = hashtag[:140]

    # Виводимо результат, якщо він не порожній
    if len(hashtag) > 1:
        print(hashtag)
    else:
        print("Неможливо створити хештег з цього рядка")

print("Дякуємо за використання!")