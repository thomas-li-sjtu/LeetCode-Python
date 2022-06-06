"""
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。 

 返回删除后的链表的头节点。 

 注意：此题对比原题有改动 

 示例 1: 

 输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
 

 示例 2: 

 输入: head = [4,5,1,9], val = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
 

 

 说明： 

 
 题目保证链表中节点的值互不相同 
 若使用 C 或 C++ 语言，你不需要 free 或 delete 被删除的节点 
 
 Related Topics 链表 👍 228 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        real_head = ListNode(x=1e-69)
        real_head.next = head
        real_head_backup = real_head

        while head and head.val != val:
            real_head = real_head.next
            head = head.next
        if not head:  # 如果head为None，则找到了最后也没有val的节点
            return real_head_backup.next
        real_head.next = head.next
        return real_head_backup.next

# leetcode submit region end(Prohibit modification and deletion)
