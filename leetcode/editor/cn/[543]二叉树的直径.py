# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。 
# 
#  
# 
#  示例 : 
# 给定二叉树 
# 
#            1
#          / \
#         2   3
#        / \     
#       4   5    
#  
# 
#  返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。 
# 
#  
# 
#  注意：两结点之间的路径长度是以它们之间边的数目表示。 
#  Related Topics 树 深度优先搜索 二叉树 
#  👍 854 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 重点是任意一个结点，都要记录以此结点为根的直径情况：左子树高度+右子树高度
    def __init__(self):
        self.max = 0

    def diameterOfBinaryTree(self, root):
        self.depth(root)

        return self.max

    def depth(self, root):
        if not root:
            return 0
        l = self.depth(root.left)
        r = self.depth(root.right)
        '''每个结点都要去判断左子树+右子树的高度是否大于self.max，更新最大值'''
        self.max = max(self.max, l + r)

        # 返回的是高度
        return max(l, r) + 1

# leetcode submit region end(Prohibit modification and deletion)
