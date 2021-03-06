# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。 
# 
#  请你将两个数相加，并以相同形式返回一个表示和的链表。 
# 
#  你可以假设除了数字 0 之外，这两个数都不会以 0 开头。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
#  
# 
#  示例 2： 
# 
#  
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#  
# 
#  示例 3： 
# 
#  
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  每个链表中的节点数在范围 [1, 100] 内 
#  0 <= Node.val <= 9 
#  题目数据保证列表表示的数字不含前导零 
#  
#  Related Topics 递归 链表 数学 
#  👍 7099 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # num_l1, num_l2 = [], []
        # while l1:
        #     num_l1.append(str(l1.val))
        #     l1 = l1.next
        # while l2:
        #     num_l2.append(str(l2.val))
        #     l2 = l2.next
        # num_l1 = int("".join(num_l1[::-1]))
        # num_l2 = int("".join(num_l2[::-1]))
        # out = list(str(num_l1 + num_l2))[::-1]
        # newhead = ListNode()
        # head = newhead
        # for i in out:
        #     tmp = ListNode(val=int(i))
        #     head.next = tmp
        #     head = tmp
        # return newhead.next

        cur_head = ListNode(-1)
        head_backup = cur_head

        increment = 0
        while l1 and l2:
            cur_val = l1.val + l2.val
            if increment > 0:
                cur_val += increment
                increment = 0
            if cur_val > 9:
                increment = cur_val // 10
                cur_val = cur_val % 10

            next_node = ListNode(cur_val)
            head_backup.next = next_node
            head_backup = head_backup.next
            l1 = l1.next
            l2 = l2.next

        if l1 and not l2:
            while l1:
                cur_val = l1.val
                if increment:
                    cur_val += increment
                    increment = 0
                if cur_val > 9:
                    increment = cur_val // 10
                    cur_val = cur_val % 10
                next_node = ListNode(cur_val)
                head_backup.next = next_node
                head_backup = head_backup.next
                l1 = l1.next
        elif l2 and not l1:
            while l2:
                cur_val = l2.val
                if increment:
                    cur_val += increment
                    increment = 0
                if cur_val > 9:
                    increment = cur_val // 10
                    cur_val = cur_val % 10
                next_node = ListNode(cur_val)
                head_backup.next = next_node
                head_backup = head_backup.next
                l2 = l2.next

        if increment > 0:
            next_node = ListNode(increment)
            head_backup.next = next_node
        return cur_head.next


# leetcode submit region end(Prohibit modification and deletion)
