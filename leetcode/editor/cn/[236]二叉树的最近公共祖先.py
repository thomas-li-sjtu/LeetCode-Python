"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。 

 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个
节点也可以是它自己的祖先）。” 

 

 示例 1： 

 
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
 

 示例 2： 

 
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
 

 示例 3： 

 
输入：root = [1,2], p = 1, q = 2
输出：1
 

 

 提示： 

 
 树中节点数目在范围 [2, 10⁵] 内。 
 -10⁹ <= Node.val <= 10⁹ 
 所有 Node.val 互不相同 。 
 p != q 
 p 和 q 均存在于给定的二叉树中。 
 
 Related Topics 树 深度优先搜索 二叉树 👍 1701 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node_val_father = {root.val: None}

        cur_stack = [root]
        while cur_stack:
            tmp_node = cur_stack.pop()
            if tmp_node.left:
                node_val_father[tmp_node.left.val] = tmp_node
                cur_stack.append(tmp_node.left)
            if tmp_node.right:
                node_val_father[tmp_node.right.val] = tmp_node
                cur_stack.append(tmp_node.right)
        p_cur_father = [p, node_val_father[p.val]]
        q_cur_father = [q, node_val_father[q.val]]
        while True:
            if p_cur_father[-1]:
                p_cur_father.append(node_val_father[p_cur_father[-1].val])
            else:
                break
        while True:
            if q_cur_father[-1]:
                q_cur_father.append(node_val_father[q_cur_father[-1].val])
            else:
                break

        for i in p_cur_father:
            if i in q_cur_father:
                return i

        
# leetcode submit region end(Prohibit modification and deletion)
