"""
Given a 2D board and a list of words from the dictionary, find all words in the board.
Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
or vertically neighboring. The same letter cell may not be used more than once in a word.
Example:
    Input:
        board = [
              ['o','a','a','n'],
              ['e','t','a','e'],
              ['i','h','k','r'],
              ['i','f','l','v']
            ]
        words = ["oath","pea","eat","rain"]
    Output: ["eat","oath"]

Note:
    All inputs are consist of lowercase letters a-z.
    The values of words are distinct.
Hint #1
    You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?
Hint #2
If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of
data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? If you
would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.
"""

class Trie:

    def __init__(self):
        self.trie = {}
        self.letters = set()

    def insert(self, word: str) -> None:
        if self.trie.get(word[0]) is None:
            self.trie[word[0]] = set()
        self.trie[word[0]].add(word)
        self.letters.add(word[0])

    def search(self, word: str) -> bool:
        if self.trie.get(word[0]) is None:
            return False
        if word in self.trie[word[0]]:
            return True
        return False

    def removeWord(self, word):
        self.trie[word[0]].remove(word)
        if self.trie[word[0]] is None:
            self.trie.pop(word[0])
            self.letters.remove(word[0])

    def startsWith(self, prefix: str) -> bool:
        if self.trie.get(prefix[0]) is None:
            return False
        return any(word.startswith(prefix) for word in self.trie[prefix[0]])

    def hasStartLetter(self, char):
        return char in self.letters



def findWords(board, words):
    if not words:
        return []
    rows, cols = len(board), len(board[0])
    words_found = []
    trie = Trie()
    for word in words:
        trie.insert(word)

    def search(row, col, indexes_used, word_so_far=""):
        if (row,col) in indexes_used:
            return

        if 0 <= row < rows and 0 <= col < cols:
            curr_word = word_so_far + board[row][col]
            if trie.startsWith(curr_word):
                if trie.search(curr_word):
                    trie.removeWord(curr_word)
                    words_found.append(curr_word)

                indexes_used = set(indexes_used)
                indexes_used.add((row, col))

                for r, c in [[0, -1], [-1, 0], [1, 0], [0, 1]]:
                    search(row + r, col + c, indexes_used, curr_word)


    for row in range(rows):
        for col in range(cols):
            if trie.hasStartLetter(board[row][col]):
                search(row, col, set())

            if len(words_found) == len(words):
                return words_found

    return words_found


# For testing
b1 = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
w1 = ["oath","pea","eat","rain"]

b2 = [["o","a","a","n"],["e","t","a","e"],["i","h","k","a"],["i","h","t","r"]]
w2 = ["oath","pea","eat","rain","ear","earth"]

b3 = [["a","b"],["a","a"]]
w3 = ["aba","baa","bab","aaab","aaa","aaaa","aaba"]

b4 = [["a","a", "b"]]
w4 = ["a", "a", "b"]

print(findWords(b4, w4))


"""
[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
["oath","pea","eat","rain"]

[["o","a","a","n"],["e","t","a","e"],["i","h","k","a"],["i","h","t","r"]]
["oath","pea","eat","rain","ear","earth"]

[["a","a"]]
["a"]

[["a","b"],["a","a"]]
["aba","baa","bab","aaab","aaa","aaaa","aaba"]
my output: ["aaa","aaab","baa","aaba"]
expected: ["aaa","aaab","aaba","aba","baa"]

"""