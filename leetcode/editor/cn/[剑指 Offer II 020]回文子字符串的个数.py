"""
给定一个字符串 s ，请计算这个字符串中有多少个回文子字符串。 

 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。 

 

 示例 1： 

 
输入：s = "abc"
输出：3
解释：三个回文子串: "a", "b", "c"
 

 示例 2： 

 
输入：s = "aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa" 

 

 提示： 

 
 1 <= s.length <= 1000 
 s 由小写英文字母组成 
 

 

 注意：本题与主站 647 题相同：https://leetcode-cn.com/problems/palindromic-substrings/ 
 Related Topics 字符串 动态规划 👍 55 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False for _ in range(len(s))] for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True

        res = len(s)
        for j in range(1, len(s)):
            for i in range(j):
                if s[i] == s[j]:
                    if j - i == 1:
                        dp[i][j] = True
                        res += 1
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                        if dp[i][j]:
                            res += 1
                else:
                    dp[i][j] = False
        return res
# leetcode submit region end(Prohibit modification and deletion)
