from typing import List


def task3(l: List[int]) -> bool:
    for i in range(1, len(l)):
        if l[i] <= l[i - 1]:
            return False
    return True


# print(task3([1, 2, 3, 4]))
# print(task3([-1, -2, 4, -3, 4]))
# print(task3([2, 2, 2]))
