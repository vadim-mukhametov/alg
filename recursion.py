l = [3, 1, 2, 5, 10, 9, 0]


def sum(arr):
    if not arr:
        return 0
    return arr.pop(0) + sum(arr)


def count(arr):
    if not arr:
        return 0
    return 1 + count(arr[1:])


def max(arr):
    max = arr[0]
    for i in arr:
        for j in arr:
            if i > j:
                max = i
    return max


def recursion_max(arr):
    if len(arr) == 2:
        return arr[0] + arr[1]
    return arr[0] + recursion_max(arr[1:])


if __name__ == '__main__':
    print(count(l))
    print(recursion_max([1, 2, 3]))
