# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：["()"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 8 
#  
#  Related Topics 字符串 动态规划 回溯 
#  👍 2368 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = [[None], ["()"]]
        for i in range(2, n+1):
            new = []
            for j in range(i):
                p = res[i-j-1]
                q = res[j]
                for char_1 in p:
                    for char_2 in q:
                        if char_1 is None:
                            char_1 = ""
                        if char_2 is None:
                            char_2 = ""
                        new.append("(" + char_1 + ")" + char_2)
            res.append(new)
        return res[n]
# leetcode submit region end(Prohibit modification and deletion)

