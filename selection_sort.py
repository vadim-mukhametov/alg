l = [3, 1, 2, 5, 10, 9, 0]


def selected_sort(list):
    def _min(list):
        index = 0
        min = list[index]
        for key, item in enumerate(list[index:]):
            if item < min:
                min = item
                index = key
        return index

    return [list.pop(_min(list)) for _ in range(len(list))]
