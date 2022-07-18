"""
给定一个字符串 s，请将 s 分割成一些子串，使每个子串都是回文串。 

 返回符合要求的 最少分割次数 。 

 
 
 

 示例 1： 

 
输入：s = "aab"
输出：1
解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
 

 示例 2： 

 
输入：s = "a"
输出：0
 

 示例 3： 

 
输入：s = "ab"
输出：1
 

 

 提示： 

 
 1 <= s.length <= 2000 
 s 仅由小写英文字母组成 
 
 
 

 

 注意：本题与主站 132 题相同： https://leetcode-cn.com/problems/palindrome-partitioning-ii/ 

 Related Topics 字符串 动态规划 👍 35 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCut(self, s: str) -> int:
        length = len(s)
        dp = [[0 for _ in range(length)] for _ in range(length)]
        for i in range(length):
            dp[i][i] = 1

        for j in range(1, length):
            for i in range(j):
                if s[i] == s[j]:
                    if i + 1 == j:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 if dp[i+1][j-1] == 1 else 0
                else:
                    continue

        # 建立最少切割次数的dp数组
        dp_mincut = list(range(len(s)))
        for i in range(1, len(s)):
            if dp[0][i]:  # 0-i自身就是回文串
                dp_mincut[i] = 0
                continue
            for j in range(0, i):  # 对于每个可能的切割位置，如果切割后后面的是回文串，那么切割数为前方切割数+1
                if dp[j + 1][i]:
                    dp_mincut[i] = min(dp_mincut[i], dp_mincut[j] + 1)

        return dp_mincut[-1]

# leetcode submit region end(Prohibit modification and deletion)
