
def frequencySort(s: str) -> str:
    if s == "":
        return s
    chars = {}
    freq = {}
    fstr = ""

    for c in s:
        chars[c] = 1 + chars.get(c, 0)

    for c, f in chars.items():
        freq[f] = freq.get(f, []) + [c]

    for i in range(max(freq.keys()), 0, -1):
        r = freq.get(i, 0)
        if r:
            for c in r:
                fstr += c * i

    return fstr


# For testing
st = ["tree", "cccaaa", "Aabb", "Python", "gigantic","cccaaaCA"]

for s in st:
    print(frequencySort(s))
