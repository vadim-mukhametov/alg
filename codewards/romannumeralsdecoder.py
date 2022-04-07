def solution(roman):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    numbers = [roman_numerals.get(item) for item in roman]

    for idx, item in enumerate(numbers):
        for i in numbers[idx:]:
            if item < i:
                numbers[idx] = -item
                continue

    return sum(numbers)


print(solution('MMMCDV'))