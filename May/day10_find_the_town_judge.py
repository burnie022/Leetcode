def findJudge(N: int, trust) -> int:
    if N == 1 and len(trust) == 0:
        return 1
    trust_dict = {}
    for p in range(len(trust)):
        if trust_dict.get(trust[p][1]) is None:
            trust_dict[trust[p][1]] = 1
        else:
            trust_dict[trust[p][1]] += 1

        trust_dict[trust[p][0]] = -N

    for key in trust_dict:
        if trust_dict[key] == N - 1:
            return key

    return -1

# For testing
n = 2
t = [[1,2],[2,1]]
print(findJudge(n, t))
