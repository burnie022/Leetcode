"""
Design a special dictionary which has some words and allows you to search the words in it by a prefix and a suffix.
Implement the WordFilter class:
    WordFilter(string[] words) Initializes the object with the words in the dictionary.
    f(string prefix, string suffix) Returns the index of the word in the dictionary which has the prefix "prefix" and
        the suffix "suffix". If there is more than one valid index, return the largest of them. If there is no such word
        in the dictionary, return -1.

Example 1:
    Input:
        ["WordFilter", "f"]
        [[["apple"]], ["a", "e"]]
    Output:
        [null, 0]

    Explanation:
        WordFilter wordFilter = new WordFilter(["apple"]);
        wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".

Constraints:
    1 <= words.length <= 15000
    1 <= words[i].length <= 10
    1 <= prefix.length, suffix.length <= 10
    words[i], prefix and suffix consist of lower-case English letters only.
    At most 15000 calls will be made to the function f.

Hint #1
    For a word like "test", consider "#test", "t#test", "st#test", "est#test", "test#test". Then if we have a query
    like prefix = "te", suffix = "t", we can find it by searching for something we've inserted starting with "t#te".
"""
from typing import List


class WordFilter:
    def __init__(self, words: List[str]):
        self.next = 0
        self.word_indexes = {}
        self.prefix_suffix_trie = Trie()
        self.add_words_to_trie(words)

    def add_words_to_trie(self, words):
        for word in words:
            self.word_indexes[word] = self.next
            self.next += 1
            self.prefix_suffix_trie.add_word(word)

    def f(self, prefix: str, suffix: str) -> int:
        matching_strings = self.prefix_suffix_trie.get_word(prefix, suffix)
        if matching_strings is None:
            return -1

        max_index = -1
        for string in matching_strings:
            max_index = max(max_index, self.word_indexes[string])

        return max_index


class Trie:
    def __init__(self):
        self.children = {}

    def add_word(self, word):
        if word:
            if self.children.get(word[0]) is None:
                self.children[word[0]] = TrieNode(word)
            else:
                self.children[word[0]].insert_word(word)

    def get_word(self, prefix, suffix):
        if self.children.get(prefix[0]) is not None:
            return self.children[prefix[0]].get_words(prefix[1:], suffix)


class TrieNode:
    def __init__(self, word):
        self.children = {}
        self.root = word[0]
        self.insert_word(word)

    def insert_word(self, word):
        if word and len(word) > 1:
            word = word[1:]
            if self.children.get(word[0]) is None:
                self.children[word[0]] = TrieNode(word)
            else:
                self.children[word[0]].insert_word(word)

    def get_words(self, prefix, suffix, word_so_far=""):
        if prefix:
            if self.children.get(prefix[0]) is not None:
                return self.children[prefix[0]].get_words(prefix[1:], suffix, word_so_far+self.root)

        elif self.children:
            result_string_set = set()
            for child in self.children:
                result = self.children[child].get_words(prefix, suffix, word_so_far+self.root)
                if result is not None:
                    result_string_set.update(result)
            if result_string_set:
                return result_string_set

        elif suffix:
            word_so_far += self.root
            if len(word_so_far) >= len(suffix):
                if word_so_far[-len(suffix):] == suffix:
                    return {word_so_far}


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)


# Test cases
strings = [
    "apple", "banana", "cherry", "lemon", "bandanna", "apa"
]

obj = WordFilter(strings)

tests = [
    ["a", "e"],
    ["b", "a"],
    ["l", "n"],
    ["c", "y"],
    ["c", "e"],
    ["app", "e"],
    ["ban", "a"],
    ["bann", "a"],
    ["ban", "la"],
    ["apa", "apa"]

]

for t in tests:
    print(obj.f(*t))

