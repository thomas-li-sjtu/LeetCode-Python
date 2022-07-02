"""
给定一个单链表 L 的头节点 head ，单链表 L 表示为： 

 L0 → L1 → … → Ln-1 → Ln 
请将其重新排列后变为： 

 L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → … 

 不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 

 

 示例 1: 

 

 
输入: head = [1,2,3,4]
输出: [1,4,2,3] 

 示例 2: 

 

 
输入: head = [1,2,3,4,5]
输出: [1,5,2,4,3] 

 

 提示： 

 
 链表的长度范围为 [1, 5 * 10⁴] 
 1 <= node.val <= 1000 
 

 

 注意：本题与主站 143 题相同：https://leetcode-cn.com/problems/reorder-list/ 
 Related Topics 栈 递归 链表 双指针 👍 64 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        l2 = slow.next
        slow.next = None
        l1 = head

        l2 = self.reverseList(l2)

        while l1 and l2:
            tmp_1 = l1.next
            tmp_2 = l2.next

            l1.next = l2
            l2.next = tmp_1

            l1 = tmp_1
            l2 = tmp_2

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
