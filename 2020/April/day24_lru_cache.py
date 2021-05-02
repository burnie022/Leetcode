"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the
following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache,
otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached
its capacity, it should invalidate the least recently used item before inserting a new item.
The cache is initialized with a positive capacity.
Follow up:
    Could you do both operations in O(1) time complexity?
Example:
    LRUCache cache = new LRUCache( 2 /* capacity */ );

    cache.put(1, 1);
    cache.put(2, 2);
    cache.get(1);       // returns 1
    cache.put(3, 3);    // evicts key 2
    cache.get(2);       // returns -1 (not found)
    cache.put(4, 4);    // evicts key 1
    cache.get(1);       // returns -1 (not found)
    cache.get(3);       // returns 3
    cache.get(4);       // returns 4
"""


class LRUCache:

    def __init__(self, capacity: int):
        self.lru_dict = {}
        self.cap = capacity
        self.last_node_key = None
        self.least_used_key = None

    class ListNode:
        def __init__(self, value):
            self.value = value
            # self.next is a key (int)
            self.next = None
            # self.last is a key (int)
            self.last = None

    def move_node_to_end(self, key):
        if self.cap > 1:
            self.update_least_recently_used(key)
            last_key = self.lru_dict[key].last
            next_key = self.lru_dict[key].next
            #print(self.least_used_key)
            if next_key is None:
                return None # because it's already the last key
            #print(next_key)
            if last_key is not None:
                self.lru_dict[last_key].next = self.lru_dict[key].next
            # else: # last_key is none, meaning this was the least used key. Next key is now least used key
            #     self.least_used_key = next_key
                #print("LRU is now %d" % (next_key))
            # since we've established this is not the last key have the next key's last point to our current last
            self.lru_dict[next_key].last = self.lru_dict[key].last

            self.lru_dict[self.last_node_key].next = key
            self.lru_dict[key].last = self.last_node_key
            self.lru_dict[key]. next = None
            self.last_node_key = key

    def pop_least_recently_used(self, key):
        # update least recently used pointer
        self.update_least_recently_used(key)
        # remove previous pointer to old recently used key
        self.lru_dict[self.least_used_key].last = None
        # pop the key and node from the dictionary
        self.lru_dict.pop(key)

    def add_node(self, key, value):
        new_node = LRUCache.ListNode(value)
        if self.last_node_key:
            self.lru_dict[self.last_node_key].next = key
        new_node.last = self.last_node_key

        self.lru_dict[key] = new_node
        self.last_node_key = key

    def update_least_recently_used(self, key):
        if key == self.least_used_key:
            if self.lru_dict[self.least_used_key].next:
                self.least_used_key = self.lru_dict[self.least_used_key].next
            else:
                print("Lost updating LRU key")

    def get(self, key: int) -> int:
        node = self.lru_dict.get(key)
        if node is not None:
            self.update_least_recently_used(key)
            self.move_node_to_end(key)
        return node.value if node is not None else -1

    def put(self, key: int, value: int) -> None:
        node = self.lru_dict.get(key)
        if len(self.lru_dict) == 0:
            self.least_used_key = key

        if len(self.lru_dict) == self.cap and node is None:
            self.pop_least_recently_used(self.least_used_key)
            self.add_node(key,value)
        elif node is not None:
            self.lru_dict[key].value = value
            self.update_least_recently_used(key)
            self.move_node_to_end(key)
        else:  # node is None but there is capacity
            self.add_node(key, value)

    """class ListNode:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None
            self.last = None

    def get(self, key: int) -> int:
        node = self.lru_dict.get(key)
        return node.value if node is not None else -1

    def put(self, key: int, value: int) -> None:
        # elif dict has values but not key, and capacity not full, add key and node, assign node as
        # curr.next, and assign curr to curr.next, and add to dict
        if self.lru_dict.get(key) is None and len(self.lru_dict) < self.cap:
            node = LRUCache.ListNode(key, value)
            # If dict is empty, assign node as head and curr_node, else add as curr.next increment curr_node
            if len(self.lru_dict) == 0:
                self.head = node
                self.curr_Node = node
            else:
                self.curr_Node.next = node
                self.curr_Node = self.curr_Node.next
            self.lru_dict[key] = node

        # if key exists, just change the value and bring it to the end of the list
        elif self.lru_dict.get(key):
            node = self.lru_dict.get(key)
            # check if node is head
            if node is self.head.next:
                self.head.next = node.next
            # change pointers at last and next nodes
            node.last.next = node.next
            if node.next:
                node.next.last = node.last
            # assign nose as curr_Node.next, then as curr_Node, and finally, update dictionary
            self.curr_Node.next = node
            self.curr_Node = self.curr_Node.next
            self.lru_dict[key] = node

        # key doesnt exist in dict and dict is full
        # if self.lru_dict.get(key) == None and len(self.lru_dict) == self.cap:
        else:
            # key not in dict and no capacity, remove lru value and update lru_key
            node = self.head.next
            self.head.next = self.head.next.next
            if self.head.next:
                self.head.next.last = None
            self.lru_dict.pop(node.key)
            # create new node, assign, key, value, assign as curr_node, add to dict
            node = LRUCache.ListNode(key, value)
            self.curr_Node.next = node
            self.curr_Node = self.curr_Node.next
            self.lru_dict[key] = node
        print(self.lru_dict)"""


# Your LRUCache object will be instantiated and called as such:
cap = 2
obj = LRUCache(cap)
print(obj.get(1))       # returns -1

obj.put(1, 1)
# print("LEast used key: " + str(obj.least_used_key))
obj.put(2, 2)
# print("LEast used key: " + str(obj.least_used_key))
print(obj.get(1))       # // returns 1
# print("LEast used key: " + str(obj.least_used_key))
print(obj.put(3, 3))    # // evicts key 2
# print("LEast used key: " + str(obj.least_used_key))
print(obj.get(2))       # // returns -1 (not found)
# print("LEast used key: " + str(obj.least_used_key))
print(obj.put(4, 4))    # // evicts key 1
# print("LEast used key: " + str(obj.least_used_key))
print(obj.get(1))       # // returns -1 (not found)
# print("LEast used key: " + str(obj.least_used_key))
print("Next line should read 3")
print(obj.get(3))       # // returns 3
print(obj.get(4))       # returns 4

print(obj.lru_dict)

"""
My answer still doesn't work. The one below does
    def __init__(self, capacity: int):
        self.lru_dict = collections.OrderedDict()
        self.cap = capacity

        
    def get(self, key: int) -> int:
        if key in self.lru_dict:
            self.lru_dict.move_to_end(key)
            return self.lru_dict[key]
            
        return -1
            

    def put(self, key: int, value: int) -> None:
        if key in self.lru_dict:
            self.lru_dict.move_to_end(key)
        elif (len(self.lru_dict) == self.cap):
            self.lru_dict.popitem(last = False)
            
        self.lru_dict[key] = value
        print(self.lru_dict[key])"""


""" Some submission errors for testing
Line 47: KeyError: 2
Last executed input:
["LRUCache","put","get","put","get","get"]
[[1],[2,1],[2],[3,2],[2],[3]]


["LRUCache","put","put","get","put","put","get"]
[[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]
Output:
[null,null,null,1,null,null,-1]
Expected:
[null,null,null,2,null,null,-1]
"""