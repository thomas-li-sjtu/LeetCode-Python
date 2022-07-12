"""
给定链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。 

 
 

 

 示例 1： 

 

 
输入：head = [4,2,1,3]
输出：[1,2,3,4]
 

 示例 2： 

 

 
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
 

 示例 3： 

 
输入：head = []
输出：[]
 

 

 提示： 

 
 链表中节点的数目在范围 [0, 5 * 10⁴] 内 
 -10⁵ <= Node.val <= 10⁵ 
 

 

 进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？ 

 

 注意：本题与主站 148 题相同：https://leetcode-cn.com/problems/sort-list/ 
 Related Topics 链表 双指针 分治 排序 归并排序 👍 70 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        list_a, list_b = head, slow.next
        slow.next = None

        a_sort = self.sortList(list_a)
        b_sort = self.sortList(list_b)

        new_head = backup = ListNode(0)
        while a_sort and b_sort:
            if a_sort.val < b_sort.val:
                backup.next = a_sort
                a_sort = a_sort.next
            else:
                backup.next = b_sort
                b_sort = b_sort.next
            backup = backup.next
        backup.next = a_sort if a_sort else b_sort
        return new_head.next

# leetcode submit region end(Prohibit modification and deletion)
