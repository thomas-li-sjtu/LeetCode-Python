"""
给定一个二叉搜索树 root 和一个目标结果 k，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。 

 

 示例 1： 

 
输入: root = [5,3,6,2,4,null,7], k = 9
输出: true
 

 示例 2： 

 
输入: root = [5,3,6,2,4,null,7], k = 28
输出: false
 

 

 提示: 

 
 二叉树的节点个数的范围是 [1, 10⁴]. 
 -10⁴ <= Node.val <= 10⁴ 
 root 为二叉搜索树 
 -10⁵ <= k <= 10⁵ 
 
 Related Topics 树 深度优先搜索 广度优先搜索 二叉搜索树 哈希表 双指针 二叉树 👍 386 👎 0

"""
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # 如果有一个从小到大的排列好的数组，只需要一个指针从左往右扫，一个指针从右往左扫
        # 从小到大的数组，从BST的中序遍历便可以得到
        # 不遍历完就模拟出两个指针——迭代器
        def in_order(node):
            if node:
                yield from in_order(node.left)
                yield node.val
                yield from in_order(node.right)

        def in_order_reverse(node):
            if node:
                yield from in_order_reverse(node.right)
                yield node.val
                yield from in_order_reverse(node.left)

        left_gen, right_gen = in_order(root), in_order_reverse(root)
        left, right = next(left_gen), next(right_gen)
        while left < right:
            if left + right < k:
                left = next(left_gen)
            elif left + right > k:
                right = next(right_gen)
            else:
                return True
        return False

# leetcode submit region end(Prohibit modification and deletion)
