"""
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构) 

 B是A的子结构， 即 A中有出现和B相同的结构和节点值。 

 例如: 
给定的树 A: 

 3 
 / \ 
 4 5 
 / \ 
 1 2 
给定的树 B： 

 4 
 / 
 1 
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。 

 示例 1： 

 输入：A = [1,2,3], B = [3,1]
输出：false
 

 示例 2： 

 输入：A = [3,4,5,1,2], B = [4,1]
输出：true 

 限制： 

 0 <= 节点个数 <= 10000 
 Related Topics 树 深度优先搜索 二叉树 👍 566 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not B:
            return False

        def dfs(a_node, b_node):
            a_stack = [a_node]
            b_stack = [b_node]
            while a_stack and b_stack:
                a_tmp, b_tmp = a_stack.pop(), b_stack.pop()
                if a_tmp.val != b_tmp.val:
                    return False
                if (
                        (not a_tmp.left and b_tmp.left) or
                        (not a_tmp.right and b_tmp.right)
                ):
                    return False

                if a_tmp.right and b_tmp.right:
                    a_stack.append(a_tmp.right)
                    b_stack.append(b_tmp.right)
                if a_tmp.left and b_tmp.left:
                    a_stack.append(a_tmp.left)
                    b_stack.append(b_tmp.left)
            return True

        stack = [A]
        flag = False
        while stack:
            tmp = stack.pop()
            if tmp.val == B.val:
                flag = dfs(tmp, B)

            if tmp.left:
                stack.append(tmp.left)
            if tmp.right:
                stack.append(tmp.right)
        return flag
# leetcode submit region end(Prohibit modification and deletion)
