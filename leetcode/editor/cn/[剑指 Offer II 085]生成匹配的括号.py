"""
正整数 n 代表生成括号的对数，请设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 

 

 示例 1： 

 
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
 

 示例 2： 

 
输入：n = 1
输出：["()"]
 

 

 提示： 

 
 1 <= n <= 8 
 

 

 注意：本题与主站 22 题相同： https://leetcode-cn.com/problems/generate-parentheses/ 
 Related Topics 字符串 动态规划 回溯 👍 42 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 一棵满二叉树，父节点到左儿子的边代表 (，到右儿子的边代表 )
        # 可以抽象为：如何在二叉树的遍历过程中找出有效的路径
        # 若 C_L < n，则仍可放入 (，即可继续遍历其左子树。反之，则不能遍历左子树了
        # 若 C_L < C_R，则仍可放入 )，即可继续遍历其右子树。反之，则不能遍历右子树了
        # 若 C_L = C_R = n，则说明到达了叶子节点，需记录根节点到该叶子的路径

        def walk(left, right, cur):
            if left == n and right == n:
                res.append("".join(cur))
                return

            if left < n:
                cur.append("(")
                walk(left+1, right, cur)
                cur.pop()
            if right < left:  # 这里一定为，
                cur.append(")")
                walk(left, right+1, cur)
                cur.pop()

        res = []
        walk(0, 0, [])
        return res

# leetcode submit region end(Prohibit modification and deletion)
