# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number


def is_palindrome(x: int, use_converting_to_string: bool) -> bool:
    if use_converting_to_string:
        s = str(x)
        return s == s[::-1]
