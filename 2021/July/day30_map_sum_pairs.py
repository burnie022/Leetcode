"""
Implement the MapSum class:
    - MapSum() Initializes the MapSum object.
    - void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original
        key-value pair will be overridden to the new one.
    - int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.

Example 1:
    Input
        ["MapSum", "insert", "sum", "insert", "sum"]
        [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
    Output
        [null, null, 3, null, 5]

    Explanation
        MapSum mapSum = new MapSum();
        mapSum.insert("apple", 3);
        mapSum.sum("ap");           // return 3 (apple = 3)
        mapSum.insert("app", 2);
        mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)


Constraints:
    1 <= key.length, prefix.length <= 50
    key and prefix consist of only lowercase English letters.
    1 <= val <= 1000
    At most 50 calls will be made to insert and sum.
"""


class TrieNode:
    def __init__(self, word=None, value=None):
        self.children = [None] * 26
        self.value = 0
        if word:
            self._insert(word, value)
        elif value:
            self.value = value

    def _insert(self, word, value):
        if word != "":
            if self.children[ord(word[0]) - 97]:
                self.children[ord(word[0]) - 97]._insert(word[1:], value)
            else:
                self.children[ord(word[0]) - 97] = TrieNode(word[1:], value)

        else:
            self.value = value

    def get_sum(self, searchWord):
        total = 0
        if searchWord == "":
            for child in self.children:
                if child:
                    total += child.get_sum(searchWord[1:])
        elif self.children[ord(searchWord[0]) - 97]:
            total += self.children[ord(searchWord[0]) - 97].get_sum(searchWord[1:])

        return total + self.value if searchWord == "" else total


class MapSum:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        self.root._insert(key, val)

    def sum(self, prefix: str) -> int:
        return self.root.get_sum(prefix)


if __name__ == "__main__":
    obj = MapSum()

    obj.insert("apple", 3)
    print(obj.sum("ap"))
    obj.insert("app", 2)
    print(obj.sum("ap"))

    #
    # tests = [
    #
    # ]
    #
    # for t in tests:
    #     print(t)
    #     print(obj.updateMatrix(t), end="\n\n")

# class MapSum:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#
#     def insert(self, key: str, val: int) -> None:
#
#     def sum(self, prefix: str) -> int:
#
# # Your MapSum object will be instantiated and called as such:
# # obj = MapSum()
# # obj.insert(key,val)
# # param_2 = obj.sum(prefix)
