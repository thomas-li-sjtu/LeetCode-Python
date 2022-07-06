"""
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重
构得到原数据。 

 请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列
化为原始的树结构。 

 

 示例 1： 

 

 
输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]
 

 示例 2： 

 
输入：root = []
输出：[]
 

 示例 3： 

 
输入：root = [1]
输出：[1]
 

 示例 4： 

 
输入：root = [1,2]
输出：[1,2]
 

 

 提示： 

 
 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，也可以采用其他的方法解决这个问
题。 
 树中结点数在范围 [0, 10⁴] 内 
 -1000 <= Node.val <= 1000 
 

 

 注意：本题与主站 297 题相同：https://leetcode-cn.com/problems/serialize-and-deserialize-
binary-tree/ 
 Related Topics 树 深度优先搜索 广度优先搜索 设计 字符串 二叉树 👍 50 👎 0

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
        if not root:
            return "[]"
        stack = [root]
        res = []
        while stack:
            cur_node = stack.pop(0)
            if cur_node:
                res.append(str(cur_node.val))
                stack.append(cur_node.left)
                stack.append(cur_node.right)
            else:
                res.append("null")

        return "[" + ",".join(res) + "]"

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "[]":
            return None
        else:
            data = data[1:-1].split(",")

        queue = []
        root = TreeNode(int(data[0]))
        queue.append(root)
        i = 1
        while queue:
            cur = queue.pop(0)
            if not cur:
                continue
            cur.left = TreeNode(int(data[i])) if data[i] != "null" else None
            cur.right = TreeNode(int(data[i + 1])) if data[i + 1] != "null" else None
            i += 2
            queue.append(cur.left)
            queue.append(cur.right)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# leetcode submit region end(Prohibit modification and deletion)
