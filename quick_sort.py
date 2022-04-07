import time

l = [3, 1, 2, 5, 10, 9, 0]


def quicksort(list):
    if len(list) == 2:
        if list[0] > list[1]:
            list[0], list[1] = list[1], list[0]
            return list
    if len(list) < 2:
        return list

    pivot = list[0]
    smaller = []
    bigger = []
    for i in list[1:]:
        if i > pivot:
            bigger.append(i)
        else:
            smaller.append(i)
    return quicksort(smaller) + [pivot] + quicksort(bigger)


if __name__ == '__main__':
    start_time = time.time()
    print(quicksort(l))
    print("--- %s seconds ---" % (time.time() - start_time))
