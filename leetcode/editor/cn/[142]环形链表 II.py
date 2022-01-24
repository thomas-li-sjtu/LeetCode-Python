# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。 
# 
#  如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到
# 链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。 
# 
#  不允许修改 链表。 
# 
#  
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：head = [3,2,0,-4], pos = 1
# 输出：返回索引为 1 的链表节点
# 解释：链表中有一个环，其尾部连接到第二个节点。
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：head = [1,2], pos = 0
# 输出：返回索引为 0 的链表节点
# 解释：链表中有一个环，其尾部连接到第一个节点。
#  
# 
#  示例 3： 
# 
#  
# 
#  
# 输入：head = [1], pos = -1
# 输出：返回 null
# 解释：链表中没有环。
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目范围在范围 [0, 104] 内 
#  -105 <= Node.val <= 105 
#  pos 的值为 -1 或者链表中的一个有效索引 
#  
# 
#  
# 
#  进阶：你是否可以使用 O(1) 空间解决此题？ 
#  Related Topics 哈希表 链表 双指针 
#  👍 1341 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 定义快慢两个指针，慢指针每次前进一步，快指针每次前进两步，若链表有环，则快慢指针一定会相遇。
        # 当快慢指针相遇时，我们让慢指针指向头节点，快指针不变，然后每次快慢指针都前进一步，当两个指针再次相遇时，两个指针所指向的节点就是入环节点。
        if not head:
            return None
        true_head = ListNode(-1)
        true_head.next = head
        tmp_node = true_head.next

        point_i, point_j = head, head
        while True:
            if point_i.next:
                point_i = point_i.next
            if point_j.next and point_j.next.next:
                point_j = point_j.next.next
            else:
                return None
            if point_j == point_i:
                point_i = head
                while True:  # 先判断！！
                    if point_j == point_i:
                        return point_i
                    point_i = point_i.next
                    point_j = point_j.next




        
# leetcode submit region end(Prohibit modification and deletion)
