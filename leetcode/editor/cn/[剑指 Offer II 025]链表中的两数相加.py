"""
给定两个 非空链表 l1和 l2 来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。 

 可以假设除了数字 0 之外，这两个数字都不会以零开头。 

 

 示例1： 

 

 
输入：l1 = [7,2,4,3], l2 = [5,6,4]
输出：[7,8,0,7]
 

 示例2： 

 
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[8,0,7]
 

 示例3： 

 
输入：l1 = [0], l2 = [0]
输出：[0]
 

 

 提示： 

 
 链表的长度范围为 [1, 100] 
 0 <= node.val <= 9 
 输入数据保证链表代表的数字无前导 0 
 

 

 进阶：如果输入链表不能修改该如何处理？换句话说，不能对列表中的节点进行翻转。 

 

 注意：本题与主站 445 题相同：https://leetcode-cn.com/problems/add-two-numbers-ii/ 
 Related Topics 栈 链表 数学 👍 58 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        new_head = backup = ListNode(0)
        carry = 0
        while l1 and l2:
            res = l1.val + l2.val + carry
            if res >= 10:
                carry = 1
                new_node = ListNode(res - 10)
            else:
                carry = 0
                new_node = ListNode(res)
            new_head.next = new_node
            new_head = new_node

            l1 = l1.next
            l2 = l2.next
        if not l1 and not l2:
            if carry == 1:
                new_node = ListNode(carry)
                new_head.next = new_node
                new_head = new_node
            return self.reverseList(backup.next)
        else:
            if l1 and not l2:
                while l1:
                    res = l1.val + carry
                    if res >= 10:
                        carry = 1
                        new_node = ListNode(res - 10)
                    else:
                        carry = 0
                        new_node = ListNode(res)
                    new_head.next = new_node
                    new_head = new_node
                    l1 = l1.next
            else:
                while l2:
                    res = l2.val + carry
                    if res >= 10:
                        carry = 1
                        new_node = ListNode(res - 10)
                    else:
                        carry = 0
                        new_node = ListNode(res)
                    new_head.next = new_node
                    new_head = new_node
                    l2 = l2.next
            if carry == 1:
                new_node = ListNode(carry)
                new_head.next = new_node
                new_head = new_node
            return self.reverseList(backup.next)

    def reverseList(self, head: ListNode) -> ListNode:
        new_head = ListNode(0)
        new_head.next = head

        cur = head
        prev = new_head
        while cur:
            next_node = cur.next
            if not next_node:
                break
            cur.next = next_node.next

            old_first = prev.next
            prev.next = next_node
            next_node.next = old_first
        return new_head.next
# leetcode submit region end(Prohibit modification and deletion)
