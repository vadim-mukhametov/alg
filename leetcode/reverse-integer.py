def reverse_int(x: int) -> int:
    if -2147483648 > x or x > 2147483647:
        return 0
    result = str(x)[::-1]
    if x < 0:
        result = f'-{result.split("-")[0]}'
    return int(result)


if __name__ == '__main__':
    print(reverse_int(1534236469))
