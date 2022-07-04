"""
完全二叉树是每一层（除最后一层外）都是完全填充（即，节点数达到最大，第 n 层有 2ⁿ⁻¹ 个节点）的，并且所有的节点都尽可能地集中在左侧。 

 设计一个用完全二叉树初始化的数据结构 CBTInserter，它支持以下几种操作： 

 
 CBTInserter(TreeNode root) 使用根节点为 root 的给定树初始化该数据结构； 
 CBTInserter.insert(int v) 向树中插入一个新节点，节点类型为 TreeNode，值为 v 。使树保持完全二叉树的状态，并返回插入的新节
点的父节点的值； 
 CBTInserter.get_root() 将返回树的根节点。 
 

 

 
 

 示例 1： 

 
输入：inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
输出：[null,1,[1,2]]
 

 示例 2： 

 
输入：inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,
6]],[7],[8],[]]
输出：[null,3,4,[1,2,3,4,5,6,7,8]]
 

 

 提示： 

 
 最初给定的树是完全二叉树，且包含 1 到 1000 个节点。 
 每个测试用例最多调用 CBTInserter.insert 操作 10000 次。 
 给定节点或插入节点的每个值都在 0 到 5000 之间。 
 

 

 注意：本题与主站 919 题相同： https://leetcode-cn.com/problems/complete-binary-tree-
inserter/ 
 Related Topics 树 广度优先搜索 设计 二叉树 👍 34 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:

    def __init__(self, root: TreeNode):
        # 两个队列表示当前层和下一层，初始化的时候，就要不断地往下遍历，使得当前层是未填满的一层
        self.root = root
        self.Q = deque([self.root])  # 当前层
        self.Q2 = deque([])  # 下一层
        while self.Q:
            a = self.Q[0]
            if not a.left:
                break
            elif not a.right:
                self.Q2.append(a.left)
                break
            else:
                cur = self.Q.popleft()
                self.Q2.append(cur.left)
                self.Q2.append(cur.right)
                if not self.Q:
                    self.Q = self.Q2
                    self.Q2 = deque([])

    def insert(self, v: int) -> int:
        # 插入时，判断当前层的第一个元素，如果没有左子树，就插入到该节点的左子树，然后在Q2中更新
        # 如果没有右子树，除了插入操作以外，还需要把这个节点从Q中pop出来，更新Q2
        # 如果Q空了，就让Q=Q2
        cur = self.Q[0]
        if not cur.left:
            cur.left = TreeNode(v)
            self.Q2.append(cur.left)
        else:
            cur.right = TreeNode(v)
            self.Q2.append(cur.right)
            self.Q.popleft()
            if not self.Q:
                self.Q = self.Q2
                self.Q2 = deque([])
        return cur.val

    def get_root(self) -> TreeNode:
        return self.root

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
# leetcode submit region end(Prohibit modification and deletion)
