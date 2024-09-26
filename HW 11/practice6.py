def frequency_histogram():
    text_input = input("Введите текст: ")
    book_histogram = dict()

    for item in text_input:
        if item not in book_histogram.keys():
            book_histogram[item] = text_input.count(item)

    print(book_histogram)

frequency_histogram()
