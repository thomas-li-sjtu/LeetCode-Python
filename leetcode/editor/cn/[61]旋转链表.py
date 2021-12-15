# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[4,5,1,2,3]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [0,1,2], k = 4
# 输出：[2,0,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目在范围 [0, 500] 内 
#  -100 <= Node.val <= 100 
#  0 <= k <= 2 * 109 
#  
#  Related Topics 链表 双指针 
#  👍 658 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        new_head = ListNode()
        new_head.next = head

        list_length = 0
        while head:
            list_length += 1
            head = head.next

        k = k % list_length
        if k == 0:
            return new_head.next
        else:
            tmp_head = new_head.next
            parent_before = new_head
            for _ in range(list_length-k):
                tmp_head = tmp_head.next
                parent_before = parent_before.next
            head = new_head.next
            parent_before.next = None
            new_head.next = tmp_head
            while tmp_head.next:
                tmp_head = tmp_head.next
            tmp_head.next = head

        return new_head.next
# leetcode submit region end(Prohibit modification and deletion)
