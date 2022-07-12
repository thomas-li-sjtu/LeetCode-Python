"""
给定一个链表数组，每个链表都已经按升序排列。 

 请将所有链表合并到一个升序链表中，返回合并后的链表。 

 

 示例 1： 

 
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
 

 示例 2： 

 
输入：lists = []
输出：[]
 

 示例 3： 

 
输入：lists = [[]]
输出：[]
 

 

 提示： 

 
 k == lists.length 
 0 <= k <= 10^4 
 0 <= lists[i].length <= 500 
 -10^4 <= lists[i][j] <= 10^4 
 lists[i] 按 升序 排列 
 lists[i].length 的总和不超过 10^4 
 

 

 注意：本题与主站 23 题相同： https://leetcode-cn.com/problems/merge-k-sorted-lists/ 
 Related Topics 链表 分治 堆（优先队列） 归并排序 👍 47 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        x = None
        for y in lists:
            x = self.merge(x, y)
        return x

    def merge(self, a: ListNode, b: ListNode) -> ListNode:
        dummy = ListNode(-1)
        x = dummy
        while a and b:
            if a.val < b.val:
                x.next = a
                a = a.next
            else:
                x.next = b
                b = b.next
            x = x.next
        if a:
            x.next = a
        if b:
            x.next = b
        return dummy.next

# leetcode submit region end(Prohibit modification and deletion)
