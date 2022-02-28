# 给你两棵二叉树： root1 和 root2 。 
# 
#  想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。你需要将这两棵树合并成一棵新二叉树。合并的规则是：如果两个节点重叠
# ，那么将这两个节点的值相加作为合并后节点的新值；否则，不为 null 的节点将直接作为新二叉树的节点。 
# 
#  返回合并后的二叉树。 
# 
#  注意: 合并过程必须从两个树的根节点开始。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# 输出：[3,4,5,5,4,null,7]
#  
# 
#  示例 2： 
# 
#  
# 输入：root1 = [1], root2 = [1,2]
# 输出：[2,2]
#  
# 
#  
# 
#  提示： 
# 
#  
#  两棵树中的节点数目在范围 [0, 2000] 内 
#  -104 <= Node.val <= 104 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 
#  👍 885 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """

        def dfs(r1, r2):
            # 如果 r1和r2中，只要有一个是null，函数就直接返回
            if not (r1 and r2):
                return r1 if r1 else r2
            # 让r1的值 等于  r1和r2的值累加
            # 再递归的计算两颗树的左节点、右节点
            r1.val += r2.val
            r1.left = dfs(r1.left, r2.left)
            r1.right = dfs(r1.right, r2.right)
            return r1

        return dfs(root1, root2)
# leetcode submit region end(Prohibit modification and deletion)
