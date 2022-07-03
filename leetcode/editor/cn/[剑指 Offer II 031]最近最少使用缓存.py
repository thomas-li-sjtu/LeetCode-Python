"""

 运用所掌握的数据结构，设计和实现一个 LRU (Least Recently Used，最近最少使用) 缓存机制 。 

 实现 LRUCache 类： 

 
 LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存 
 int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。 
 void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时
，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。 
 

 

 示例： 

 
输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
 

 

 提示： 

 
 1 <= capacity <= 3000 
 0 <= key <= 10000 
 0 <= value <= 10⁵ 
 最多调用 2 * 10⁵ 次 get 和 put 
 
 

 

 进阶：是否可以在 O(1) 时间复杂度内完成这两种操作？ 

 

 注意：本题与主站 146 题相同：https://leetcode-cn.com/problems/lru-cache/ 
 Related Topics 设计 哈希表 链表 双向链表 👍 54 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)

class Node:

    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.cur_num = 0

    def get(self, key: int) -> int:
        if self.hashmap.get(key) is not None:
            node = self.hashmap[key]
            node.prev.next = node.next
            node.next.prev = node.prev

            self.head.next.prev = node
            node.next = self.head.next
            node.prev = self.head
            self.head.next = node

            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.hashmap.get(key) is not None:
            node = self.hashmap[key]
            node.value = value

            node.prev.next = node.next
            node.next.prev = node.prev

            self.head.next.prev = node
            node.next = self.head.next
            node.prev = self.head
            self.head.next = node
        else:
            self.cur_num += 1

            node = Node(key, value)
            self.hashmap[key] = node
            self.head.next.prev = node
            node.next = self.head.next
            node.prev = self.head
            self.head.next = node

            if self.cur_num > self.capacity:
                last_node = self.tail.prev

                last_node.prev.next = self.tail
                self.tail.prev = last_node.prev

                del self.hashmap[last_node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)
