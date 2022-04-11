"""
给定一个二叉树 

 
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
} 

 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。 

 初始状态下，所有 next 指针都被设置为 NULL。 p[

 

 进阶： 

 
 你只能使用常量级额外空间。 
 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。 
 

 

 示例： 

 

 
输入：root = [1,2,3,4,5,null,7]
输出：[1,#,2,3,#,4,5,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化输出按层序遍历顺序（由 next 指针连
接），'#' 表示每层的末尾。 

 

 提示： 

 
 树中的节点数小于 6000 
 -100 <= node.val <= 100 
 

 

 
 
 Related Topics 树 深度优先搜索 广度优先搜索 链表 二叉树 👍 535 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        stack = [(root, 0)]
        layer_count = -1
        tree, tmp_layer_list = [], []
        while stack:
            tmp_node, tmp_layer = stack.pop(0)
            if tmp_layer != layer_count:
                tree.append(tmp_layer_list)
                tmp_layer_list = [tmp_node]
                layer_count = tmp_layer
            else:
                tmp_layer_list.append(tmp_node)

            if tmp_node.left:
                stack.append((tmp_node.left, tmp_layer + 1))
            if tmp_node.right:
                stack.append((tmp_node.right, tmp_layer + 1))
        tree.pop(0)
        tree.append(tmp_layer_list)

        for layer in tree:
            for i in range(len(layer) - 1):
                layer[i].next = layer[i + 1]
            layer[-1].next = None

        return tree[0][0]

# leetcode submit region end(Prohibit modification and deletion)
