# https://leetcode.com/problems/longest-substring-without-repeating-characters/


s = "abcabcbb"


def till(index: int, search, base_str: str):
    count = 0
    for i in base_str[index:]:
        if count != 0 and i == search:
            return count
        count += 1
    return count


def len_if_longest(s: str) -> int:
    result = []
    for index, val in enumerate(s):
        result.append(till(index, val, s))

    return result

# def len_of_longest(s: str):
#     if not s:
#         return 0
#     if len(s) == 1:
#         return 1
#
#     result = []
#     substring = []
#     for i in s:
#         if i in substring:
#             result.append(substring)
#             substring = []
#         substring.append(i)
#     else:
#         result.append(substring)
#
#     return max(len(i) for i in result)


if __name__ == '__main__':
    print(len_if_longest(s))
