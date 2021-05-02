"""
Implement a trie with insert, search, and startsWith methods.

Example:
    Trie trie = new Trie();
    trie.insert("apple");
    trie.search("apple");   // returns true
    trie.search("app");     // returns false
    trie.startsWith("app"); // returns true
    trie.insert("app");
    trie.search("app");     // returns true
Note:
You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""


class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        if self.trie.get(word[0]) is None:
            self.trie[word[0]] = set()
        self.trie[word[0]].add(word)

    def search(self, word: str) -> bool:
        if self.trie.get(word[0]) is None:
            return False
        if word in self.trie[word[0]]:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        if self.trie.get(prefix[0]) is None:
            return False
        return any(word.startswith(prefix) for word in self.trie[prefix[0]])


# For Testing
obj = Trie()
word = "app"
obj.insert(word)
print(obj.search(word))
print(obj.search("apple"))
print(obj.startsWith("app"))
