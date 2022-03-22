# 给定单链表的头节点 head ，将所有索引为奇数的节点和索引为偶数的节点分别组合在一起，然后返回重新排序的列表。 
# 
#  第一个节点的索引被认为是 奇数 ， 第二个节点的索引为 偶数 ，以此类推。 
# 
#  请注意，偶数组和奇数组内部的相对顺序应该与输入时保持一致。 
# 
#  你必须在 O(1) 的额外空间复杂度和 O(n) 的时间复杂度下解决这个问题。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入: head = [1,2,3,4,5]
# 输出: [1,3,5,2,4] 
# 
#  示例 2: 
# 
#  
# 
#  
# 输入: head = [2,1,3,5,6,4,7]
# 输出: [2,3,6,7,1,5,4] 
# 
#  
# 
#  提示: 
# 
#  
#  n == 链表中的节点数 
#  0 <= n <= 104 
#  -106 <= Node.val <= 106 
#  
#  Related Topics 链表 
#  👍 553 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        list_o_head = head  # 奇数链表头
        list_p_head = head.next  # 偶数链表头
        node_e = list_p_head

        while list_o_head.next and node_e.next:
            list_o_head.next = node_e.next
            list_o_head = node_e.next
            node_e.next = list_o_head.next
            node_e = list_o_head.next
        list_o_head.next = list_p_head
        return head
# leetcode submit region end(Prohibit modification and deletion)

