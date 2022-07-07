"""
给你一棵二叉搜索树，请 按中序遍历 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。 

 

 示例 1： 

 

 
输入：root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
 

 示例 2： 

 

 
输入：root = [5,1,7]
输出：[1,null,5,null,7]
 

 

 提示： 

 
 树中节点数的取值范围是 [1, 100] 
 0 <= Node.val <= 1000 
 

 

 注意：本题与主站 897 题相同： https://leetcode-cn.com/problems/increasing-order-search-
tree/ 
 Related Topics 栈 树 深度优先搜索 二叉搜索树 二叉树 👍 34 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        self.node_stack = []

        def search(node):
            if node.left:
                search(node.left)
            self.node_stack.append(node)
            if node.right:
                search(node.right)

        search(root)
        for i in range(1, len(self.node_stack)):
            self.node_stack[i - 1].left = None
            self.node_stack[i - 1].right = self.node_stack[i]
            self.node_stack[i].left = None
        self.node_stack[-1].left = None
        self.node_stack[-1].right = None

        return self.node_stack[0]

# leetcode submit region end(Prohibit modification and deletion)
