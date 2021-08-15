"""
There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push
some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the
dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or
already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.

Example 1:
    Input: dominoes = "RR.L"
    Output: "RR.L"
    Explanation: The first domino expends no additional force on the second domino.

Example 2: VIEW EXAMPLE PIC: dominoes_ex2.png
    Input: dominoes = ".L.R...LR..L.."
    Output: "LL.RR.LLRRLL.."

Constraints:
    n == dominoes.length
    1 <= n <= 10^5
    dominoes[i] is either 'L', 'R', or '.'.
"""


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        right, left, ans = [1 if dominoes[0] == "R" else 0], [1 if dominoes[-1] == "L" else 0], []
        for c in dominoes[1:]:
            if c == 'R':
                right.append(1)
            elif c == 'L':
                right.append(0)
            else:
                right.append(right[-1] + 1 if right[-1] else 0)

        for c in dominoes[::-1][1:]:
            if c == 'L':
                left.append(1)
            elif c == 'R':
                left.append(0)
            else:
                left.append(left[-1] + 1 if left[-1] else 0)
        left = left[::-1]

        for i in range(len(dominoes)):
            if dominoes[i] == '.': #L' or c == 'R':
                if left[i] and right[i]:
                    if left[i] == right[i]:
                        ans.append('.')
                    elif left[i] < right[i]:
                        ans.append('L')
                    else:
                        ans.append('R')
                else:
                    if left[i]:
                        ans.append('L')
                    elif right[i]:
                        ans.append('R')
                    else:
                        ans.append('.')
            else:
                ans.append(dominoes[i])

        return ''.join(ans)


if __name__ == "__main__":
    obj = Solution()
    tests = [
        "RR.L", ".L.R...LR..L..", 'R.....L', 'R......L', 'R', 'L', '.', ".L.R...LR..RL.L.", "RR.L.R...LR..L.."
    ]

    for t in tests:
        print(f"\"{t}\"")
        # print(obj.pushDominoes(t), end="\n\n")

