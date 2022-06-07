"""
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。 

 示例1： 

 输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4 

 限制： 

 0 <= 链表长度 <= 1000 

 注意：本题与主站 21 题相同：https://leetcode-cn.com/problems/merge-two-sorted-lists/ 
 Related Topics 递归 链表 👍 249 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        if not l1 and l2:
            return l2
        if l1 and not l2:
            return l1
        pointer_1, pointer_2 = l1, l2
        new_head = ListNode(0)
        new_head_backup = new_head
        while pointer_1 and pointer_2:
            if pointer_1.val <= pointer_2.val:
                tmp_node = ListNode(pointer_1.val)
                new_head.next = tmp_node
                new_head = new_head.next

                pointer_1 = pointer_1.next
            else:
                tmp_node = ListNode(pointer_2.val)
                new_head.next = tmp_node
                new_head = new_head.next

                pointer_2 = pointer_2.next
        if not pointer_1:
            new_head.next = pointer_2
        if not pointer_2:
            new_head.next = pointer_1

        return new_head_backup.next

# leetcode submit region end(Prohibit modification and deletion)
