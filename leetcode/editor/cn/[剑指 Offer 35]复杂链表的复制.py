"""
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链
表中的任意节点或者 null。 

 

 示例 1： 

 

 输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
 

 示例 2： 

 

 输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
 

 示例 3： 

 

 输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
 

 示例 4： 

 输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
 

 

 提示： 

 
 -10000 <= Node.val <= 10000 
 Node.random 为空（null）或指向链表中的节点。 
 节点数目不超过 1000 。 
 

 

 注意：本题与主站 138 题相同：https://leetcode-cn.com/problems/copy-list-with-random-
pointer/ 

 
 Related Topics 哈希表 链表 👍 536 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)

# Definition for a Node.
import copy


# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # # 先建立dict，后“连线”
        # if not head:
        #     return None
        # head_backup = head
        # random_dict = {}
        # while head:
        #     random_dict[head] = Node(head.val)
        #     head = head.next
        # head = head_backup
        # while head:
        #     if head.next:
        #         random_dict[head].next = random_dict[head.next]
        #     if head.random:
        #         random_dict[head].random = random_dict[head.random]
        #
        #     head = head.next
        # return random_dict[head_backup]

        # 先建立dict、连线next，再连线random
        if not head:
            return None
        cur = Node(head.val)
        cur_backup = cur
        head_backup = head
        random_dict = {}
        while head:
            if head.next:
                cur.next = Node(head.next.val)
            random_dict[head] = cur
            cur = cur.next
            head = head.next
        cur = cur_backup
        head = head_backup
        while head:
            if head.random:
                cur.random = random_dict[head.random]
            cur = cur.next
            head = head.next
        return cur_backup
        
# leetcode submit region end(Prohibit modification and deletion)
