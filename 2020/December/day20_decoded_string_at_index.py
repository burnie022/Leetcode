"""
An encoded string S is given.  To find and write the decoded string to a tape, the encoded string is read
one character at a time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit (say d), the entire current tape is repeatedly written d-1 more times in
total.
Now for some encoded string S, and an index K, find and return the K-th letter (1 indexed) in the decoded
string.

Example 1:
    Input: S = "leet2code3", K = 10
    Output: "o"
    Explanation:
        The decoded string is "leetleetcodeleetleetcodeleetleetcode".
        The 10th letter in the string is "o".
Example 2:
    Input: S = "ha22", K = 5
    Output: "h"
    Explanation:
        The decoded string is "hahahaha".  The 5th letter is "h".
Example 3:
    Input: S = "a2345678999999999999999", K = 1
    Output: "a"
    Explanation:
        The decoded string is "a" repeated 8301530446056247680 times.  The 1st letter is "a".

Constraints:
    2 <= S.length <= 100
    S will only contain lowercase letters and digits 2 through 9.
    S starts with a letter.
    1 <= K <= 10^9
    It's guaranteed that K is less than or equal to the length of the decoded string.
    The decoded string is guaranteed to have less than 2^63 letters.
"""


# my slow solution
def decodeAtIndex(S: str, K: int) -> str:
    decode = ""
    for c in S:
        if c.isdigit():
            decode *= int(c)
        else:
            decode += c
        if len(decode) >= K:
            return decode[K - 1]


# A fast leetcode solution
def decodeAtIndexLC(S: str, K: int) -> str:
    A = [1]
    for x in S[1:]:
        if A[-1] >= K:
            break
        if x.isdigit():
            A.append(A[-1] * int(x))
        else:
            A.append(A[-1] + 1)

    for i in reversed(range(len(A))):
        K %= A[i]
        if not K and not S[i].isdigit():
            return S[i]


# Test cases
tests = [
    ("leet2code3", 10),
    ("ha22", 5),
    ("a2345678999999999999999", 1),
    ("cpmxv8ewnfk3xxcilcmm68d2ygc88daomywc3imncfjgtwj8nrxjtwhiem5nzqnicxzo248g52y72v3yujqpvqcssrofd99lkovg", 480551547)
]

for t in tests:
    print(t)
    print(decodeAtIndex(*t))
