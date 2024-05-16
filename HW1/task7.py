from collections import Counter


def task7(s: str) -> int:

    letters_num = Counter(s)
    result = ""
    for i in letters_num:
        result += i * (letters_num[i] // 2)
        letters_num[i] -= letters_num[i] // 2 * 2
    result += dict(map(reversed, letters_num.items())).get(1, '') + result[::-1]
    return len(result)


# print(task7("oaoaommm"))
