"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。 

 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个
节点也可以是它自己的祖先）。” 

 例如，给定如下二叉树: root = [3,5,1,6,2,0,8,null,null,7,4] 

 

 

 示例 1: 

 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
 

 示例 2: 

 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
 

 

 说明: 

 
 所有节点的值都是唯一的。 
 p、q 为不同节点且均存在于给定的二叉树中。 
 

 注意：本题与主站 236 题相同：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-
binary-tree/ 
 Related Topics 树 深度优先搜索 二叉树 👍 449 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        tree_dict = {}
        stack = [root]
        while stack:
            cur_node = stack.pop()
            if cur_node.right:
                tree_dict[cur_node.right] = cur_node
                stack.append(cur_node.right)
            if cur_node.left:
                tree_dict[cur_node.left] = cur_node
                stack.append(cur_node.left)

        p_parents = [p]
        while tree_dict.get(p):
            p_parents.append(tree_dict[p])
            p = tree_dict[p]
        q_parents = [q]
        while tree_dict.get(q):
            q_parents.append(tree_dict[q])
            q = tree_dict[q]

        for i in range(len(p_parents)):
            for j in range(len(q_parents)):
                if p_parents[i].val == q_parents[j].val:
                    return p_parents[i]
# leetcode submit region end(Prohibit modification and deletion)
