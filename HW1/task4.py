def task4(s: str) -> int:
    letters_ = ['а', 'у', 'о', 'ы', 'э', 'я', 'ю', 'ё', 'и', 'е']
    count = 0
    for i in letters_:
        if i in s:
            count += 1
    return count


# print(task4("ауеив"))
# print(task4("ааааа"))
