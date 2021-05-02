"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In
other words, one of the first string's permutations is the substring of the second string.
Example 1:
    Input: s1 = "ab" s2 = "eidbaooo"
    Output: True
    Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
    Input:s1= "ab" s2 = "eidboaoo"
    Output: False

Note:
    The input strings only contain lower case letters.
    The length of both given strings is in range [1, 10,000].
"""
import collections

def checkInclusion(s1: str, s2: str) -> bool:
    count = collections.Counter(s1)
    dict_s1 = count.copy()

    left = right = 0
    while right < len(s2):
        if count[s2[right]]:
            print(s2[right],count[s2[right]], "going right")
            count.subtract(s2[right])
            right += 1
        elif dict_s1.get(s2[right]) and left < right:
            print("re-adding", s2[left])
            count.update(s2[left])
            left += 1
        else:
            print(s2[right], "- pass", end="")
            right += 1
            left = right
            if count != dict_s1:
                print("- resetting")
                count.clear()
                count.update(dict_s1)
            else:
                print("")

        if right - left == len(s1):
            return True
    return False

# For testing:
tests = {"abc": "eidbaooadcoobdaobaodbca",
         "abcd": "egfabccabacbaod",
         "abd": "egfabcdcabacbad",
         "aacd": "egfabccabacbdaadc"}
for a, b in tests.items():
    print(checkInclusion(a, b))
    print("")


"""def tester(s):
    d = {}
    count = collections.Counter(s)
    print(count)
    count.subtract("b")
    print(count)
    count.update("a")
    print(count)
    d = count.copy()
    print(d)

str = "aabbccdd"
tester(str)"""
