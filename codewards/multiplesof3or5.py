# Multiples of 3 or 5

from tkinter import N


def solution(number):
    sum = 0
    for i in range(1, number):
        multiple_of_3 = i % 3 == 0
        multiple_of_5 = i % 5 == 0

        if multiple_of_3 or multiple_of_5:
            sum += i
            continue

    return sum



print(solution(5))