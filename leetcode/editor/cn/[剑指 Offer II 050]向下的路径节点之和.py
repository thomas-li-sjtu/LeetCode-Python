"""
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。 

 路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。 

 

 示例 1： 

 

 
输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3
解释：和等于 8 的路径有 3 条，如图所示。
 

 示例 2： 

 
输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：3
 

 

 提示: 

 
 二叉树的节点个数的范围是 [0,1000] 
 -10⁹ 
 -1000 <= targetSum <= 1000 
 

 

 注意：本题与主站 437 题相同：https://leetcode-cn.com/problems/path-sum-iii/ 
 Related Topics 树 深度优先搜索 二叉树 👍 50 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.target = 0
        self.prefix_dict = defaultdict(int)
        self.prefix_dict[0] = 1
        self.count = 0

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        self.target = targetSum

        def search(root, cur_val):
            if not root:
                return 0

            cur_val += root.val
            if self.prefix_dict.get(cur_val - targetSum):
                self.count += self.prefix_dict[cur_val - targetSum]
            self.prefix_dict[cur_val] += 1

            if root.left:
                search(root.left, cur_val)
            if root.right:
                search(root.right, cur_val)
            self.prefix_dict[cur_val] -= 1

        search(root, 0)
        return self.count

# leetcode submit region end(Prohibit modification and deletion)
