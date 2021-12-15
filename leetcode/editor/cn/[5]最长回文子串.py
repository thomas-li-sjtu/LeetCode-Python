# 给你一个字符串 s，找到 s 中最长的回文子串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "cbbd"
# 输出："bb"
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "a"
# 输出："a"
#  
# 
#  示例 4： 
# 
#  
# 输入：s = "ac"
# 输出："a"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 仅由数字和英文字母（大写和/或小写）组成 
#  
#  Related Topics 字符串 动态规划 
#  👍 4368 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s):
        # 动态规划，dp[i][j]表示s[i:j]是否为回文子串
        # 每次判断s[i][j]时更新maxlen=j-i+1和start=i
        # 边界，当j-i+1<2时，肯定是回文串; dp[i][i]=True
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start, max_len = 0, 1

        # 边界
        if n < 2:
            return s
        # 初始化
        for i in range(n):
            dp[i][i] = True
        # 枚举区间终点
        for j in range(1, n):
            # 枚举起点
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j]:
                    l = j - i + 1
                    if l > max_len:
                        max_len = l
                        start = i

        return s[start: start + max_len]

# leetcode submit region end(Prohibit modification and deletion)
