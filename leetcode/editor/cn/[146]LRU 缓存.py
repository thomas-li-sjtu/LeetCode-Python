# 请你设计并实现一个满足 LRU (最近最少使用) 缓存 约束的数据结构。 
# 
#  实现 LRUCache 类： 
# 
#  
#  
#  
#  LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存 
#  int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。 
#  void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 ke
# y-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。 
#  
# 
#  函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。 
#  
#  
# 
#  
# 
#  示例： 
# 
#  
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= capacity <= 3000 
#  0 <= key <= 10000 
#  0 <= value <= 105 
#  最多调用 2 * 105 次 get 和 put 
#  
#  Related Topics 设计 哈希表 链表 双向链表 
#  👍 1858 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.hashmap = {}
        # 新建两个节点 head 和 tail
        self.head = ListNode()
        self.tail = ListNode()
        # 初始化链表为 head <-> tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # 因为get与put操作都可能需要将双向链表中的某个节点移到头部(变成最新访问的)，所以定义一个方法
    def move_node_to_header(self, key):
        # 先将哈希表key指向的节点拎出来，为了简洁起名node
        #      hashmap[key]                               hashmap[key]
        #           |                                          |
        #           V              -->                         V
        # prev <-> node <-> next         pre <-> next   ...   node
        node = self.hashmap[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        # 之后将node插入到头部节点前
        #                   hashmap[key]                     hashmap[key]
        #                       |                                 |
        #                       V        -->                      V
        # header <-> next  ... node                   header <-> node <-> next
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def add_node_to_header(self, key, value):
        new = ListNode(key, value)
        self.hashmap[key] = new
        new.prev = self.head
        new.next = self.head.next
        self.head.next.prev = new
        self.head.next = new

    def pop_tail(self):
        last_node = self.tail.prev
        # 去掉链表尾部的节点在哈希表的对应项
        self.hashmap.pop(last_node.key)
        # 去掉最久没有被访问过的节点，即尾部Tail之前的一个节点
        last_node.prev.next = self.tail
        self.tail.prev = last_node.prev
        return last_node

    def get(self, key):
        if key in self.hashmap:
            # 如果已经在链表中了久把它移到头部（变成最新访问的）
            self.move_node_to_header(key)
        res = self.hashmap.get(key, -1)
        if res == -1:
            return res
        else:
            return res.value

    def put(self, key, value):
        if key in self.hashmap:
            # 如果key本身已经在哈希表中了就不需要在链表中加入新的节点
            # 但是需要更新字典该值对应节点的value
            self.hashmap[key].value = value
            # 之后将该节点移到链表头部
            self.move_node_to_header(key)
        else:
            if len(self.hashmap) >= self.capacity:
                # 若cache容量已满，删除cache中最不常用的节点
                self.pop_tail()
            self.add_node_to_header(key, value)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)
