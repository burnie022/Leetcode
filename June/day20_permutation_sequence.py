"""
The set [1,2,3,...,n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
    "123"
    "132"
    "213"
    "231"
    "312"
    "321"

Given n and k, return the kth permutation sequence.
Note:
    Given n will be between 1 and 9 inclusive.
    Given k will be between 1 and n! inclusive.
Example 1:
    Input: n = 3, k = 3
    Output: "213"
Example 2:
    Input: n = 4, k = 9
    Output: "2314"
"""


def getPermutation(n: int, k: int) -> str:
    if k == 1:
        return "".join([str(i) for i in range(1, n + 1)])

    permutations = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    n = [str(i) for i in range(1, n + 1)]
    ans = ""

    while k and n:
        perm = permutations[len(n)-1]
        index = k // perm
        if k % perm == 0:
            index -= 1

        ans += n.pop(index)
        k -= (perm * index)

    return ans


# For testing
tests = [(5, 24), (5, 25), (3, 3), (4, 9), (4, 1)]
for n, k in tests:
    print("n:", n, "k:", k, "ans:", getPermutation(n, k))
