"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。 

 

 为了让您更好地理解问题，以下面的二叉搜索树为例： 

 

 

 

 我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一
个节点。 

 下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。 

 

 

 

 特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。 

 

 注意：本题与主站 426 题相同：https://leetcode-cn.com/problems/convert-binary-search-tree-
to-sorted-doubly-linked-list/ 

 注意：此题对比原题有改动。 
 Related Topics 栈 树 深度优先搜索 二叉搜索树 链表 二叉树 双向链表 👍 519 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # if not root:
        #     return None
        # res = []
        #
        # def dfs(node: Node):
        #     if node.left:
        #         dfs(node.left)
        #     res.append(node)
        #     if node.right:
        #         dfs(node.right)
        # dfs(root)
        # for i in range(len(res)-1):
        #     res[i].right = res[i+1]
        #     res[i+1].left = res[i]
        # res[0].left = res[-1]
        # res[-1].right = res[0]
        # return res[0]

        # 递归中修改
        def dfs(cur):
            if not cur: return
            dfs(cur.left)  # 递归左子树
            if self.pre:  # 修改节点引用
                self.pre.right, cur.left = cur, self.pre
            else:  # 记录头节点
                self.head = cur
            self.pre = cur  # 保存 cur
            dfs(cur.right)  # 递归右子树

        if not root: return
        self.pre = None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head


# leetcode submit region end(Prohibit modification and deletion)
