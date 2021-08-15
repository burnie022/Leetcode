"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every
character in t (including duplicates) is included in the window. If there is no such substring, return the empty
string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

Example 1:
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
    Input: s = "a", t = "a"
    Output: "a"
    Explanation: The entire string s is the minimum window.

Example 3:
    Input: s = "a", t = "aa"
    Output: ""
    Explanation: Both 'a's from t must be included in the window.
    Since the largest window of s only has one 'a', return empty string.

Constraints:
    m == s.length
    n == t.length
    1 <= m, n <= 10^5
    s and t consist of uppercase and lowercase English letters.


Follow up: Could you find an algorithm that runs in O(m + n) time?
   Hide Hint #1
Use two pointers to create a window of letters in S, which would have all the characters from T.
   Hide Hint #2
Since you have to find the minimum window in S which has all the characters from T, you need to expand and contract the window using the two pointers and keep checking the window for all the characters. This approach is also called Sliding Window Approach.

L ------------------------ R , Suppose this is the window that contains all characters of T

        L----------------- R , this is the contracted window. We found a smaller window that still contains all the characters in T

When the window is no longer valid, start expanding again using the right pointer.
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        asc, count = [0 for _ in range(58)], {}
        window, start = len(s) + 1, 0
        for c in t:
            asc[ord(c) - 65] -= 1
            count[c] = count.get(c, 0) + 1

        for i in range(len(asc)):
            if asc[i] == 0:
                asc[i] += 100000

        right = 0
        while right < len(s) and count:
            asc[ord(s[right]) - 65] += 1

            if count.get(s[right]):
                count[s[right]] -= 1
                if count[s[right]] == 0:
                    count.pop(s[right])
            right += 1
        if count:
            return ""

        left = 0
        while right < len(s):
            while asc[ord(s[left]) - 65] > 0:
                asc[ord(s[left]) - 65] -= 1
                left += 1

            if right - left < window:
                window = right - left
                start = left

            asc[ord(s[right]) - 65] += 1
            right += 1

        while asc[ord(s[left]) - 65] > 0:
            asc[ord(s[left]) - 65] -= 1
            left += 1
            if right - left < window:
                window = right - left
                start = left

        return s[start: start + window]



if __name__ == "__main__":
    obj = Solution()
    tests = [
        ("ADOBECODEBANC", "ABC"),
        ("a", "a"),
        ("a", "aa"),
        ("aabc", "caba"),
        ("jHZLKJBmxCvhFIDlewypqVjEOPPnddkAeQgciGSNjtOzGnzwflCTNQAmZeHSBEUElaCnyPoRjAEBsUgagTwSugBQzsxuPhaHBiMT", "IBnc"),
        ("jHZLKJBmxCvhFIDlewypqVjEOPPnddkAeQgciGSNjtOzGnzwflCTNQAmZeHSBEUElaCnyPoRjAEBsUgagTwSugBQzsxuPhaHBiMT", "IBArnc"),
        ("jHZLKJBmxCvhFIDlewypqVjEOPPnddkAeQgciGSNjtOzGnzwflCTNQAmZeHSBEUElaCnyPoRjAEBsUgagTwSugBQzsxuPhaHBiMT", "IBARnc"),

    ]
    #
    for t in tests:
        print(f"\"{t[0]}\"")
        print(f"\"{t[1]}\"")
        # print(obj.minWindow(*t), end="\n\n")


    # from random import randint
    # def test_gen(length):
    #     s = []
    #     for _ in range(length):
    #         cap = randint(0,1)
    #         s.append(chr(randint(65, 90)) if cap == 1 else chr(randint(97,122)))
    #     return "".join(s)
    # print(test_gen(100))
