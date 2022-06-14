"""
请实现两个函数，分别用来序列化和反序列化二叉树。 

 你需要设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串
反序列化为原始的树结构。 

 提示：输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解
决这个问题。 

 

 示例： 

 
输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]
 

 

 注意：本题与主站 297 题相同：https://leetcode-cn.com/problems/serialize-and-deserialize-
binary-tree/ 
 Related Topics 树 深度优先搜索 广度优先搜索 设计 字符串 二叉树 👍 310 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        stack = [root]
        if not root:
            return "[]"
        res = []
        while stack:
            cur_node = stack.pop(0)
            if not cur_node:
                res.append("null")
            else:
                res.append(str(cur_node.val))
                stack.append(cur_node.left)
                stack.append(cur_node.right)
        return "[" + ",".join(res) + "]"

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "[]":
            return
        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# leetcode submit region end(Prohibit modification and deletion)
