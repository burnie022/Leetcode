"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is
being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; No extra white spaces, square brackets are
well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits
are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Example 1:
    Input: s = "3[a]2[bc]"
    Output: "aaabcbc"
Example 2:
    Input: s = "3[a2[c]]"
    Output: "accaccacc"
Example 3:
    Input: s = "2[abc]3[cd]ef"
    Output: "abcabccdcdcdef"
Example 4:
    Input: s = "abc3[cd]xyz"
    Output: "abccdcdcdxyz"

Constraints:
    1 <= s.length <= 30
    s consists of lowercase English letters, digits, and square brackets '[]'.
    s is guaranteed to be a valid input.
    All the integers in s are in the range [1, 300].
"""

def decodeString(s: str) -> str:
    stack = []
    curr_multiplier = "1"
    new_multipler = ""
    curr_string = []
    for letter in s:
        if letter == "[":
            stack.append((curr_multiplier, curr_string))
            curr_multiplier, new_multipler = new_multipler, ""
            curr_string = []
        if letter == "]":
            repeated_string = ("".join(curr_string)) * int(curr_multiplier)

            curr_multiplier, curr_string = stack.pop()
            curr_string.append(repeated_string)
            new_multipler = ""

        ascii_val = ord(letter)
        if 97 <= ascii_val <= 122:
            curr_string.append(letter)
        if 48 <= ascii_val <= 57:
            new_multipler += letter

    return "".join(curr_string)

# Test cases

tests = [
    "3[a]2[bc]",
    "10[a]",
    "3[a2[c]]",
    "3[a2[c]]3[a]2[bc]",
    "2[abc]3[cd]ef"
    "3[a2[c2[d2[g]]2[f]]]"
]
for t in tests:
    print(decodeString(t), end="\n\n")

