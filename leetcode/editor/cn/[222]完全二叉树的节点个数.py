"""
给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。 

 完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第
 h 层，则该层包含 1~ 2ʰ 个节点。 

 

 示例 1： 

 
输入：root = [1,2,3,4,5,6]
输出：6
 

 示例 2： 

 
输入：root = []
输出：0
 

 示例 3： 

 
输入：root = [1]
输出：1
 

 

 提示： 

 
 树中节点的数目范围是[0, 5 * 10⁴] 
 0 <= Node.val <= 5 * 10⁴ 
 题目数据保证输入的树是 完全二叉树 
 

 

 进阶：遍历树来统计节点是一种时间复杂度为 O(n) 的简单解决方案。你可以设计一个更快的算法吗？ 
 Related Topics 树 深度优先搜索 二分查找 二叉树 👍 692 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDepth(self, root):  # 计算当前树的深度
        depth = 0
        while root:
            depth += 1
            root = root.left
        return depth

    def countNodes(self, root: TreeNode) -> int:
        cnt = 0
        while root:
            left = self.getDepth(root.left)  # 左子树深度
            right = self.getDepth(root.right)  # 右子树深度
            if left == right:  # 左右子树深度相同，左子树一定是满二叉树，右子树可能为满二叉树，一定为完全二叉树
                root = root.right
                cnt += 2 ** left
            else:  # 左右子树深度不同，右子树一定是满二叉树，左子树可能为满二叉树，一定为完全二叉树
                root = root.left
                cnt += 2 ** right
        return cnt

# leetcode submit region end(Prohibit modification and deletion)
