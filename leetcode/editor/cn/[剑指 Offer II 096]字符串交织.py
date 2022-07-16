"""
给定三个字符串 s1、s2、s3，请判断 s3 能不能由 s1 和 s2 交织（交错） 组成。 

 两个字符串 s 和 t 交织 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串： 

 
 s = s1 + s2 + ... + sn 
 t = t1 + t2 + ... + tm 
 |n - m| <= 1 
 交织 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ... 
 

 提示：a + b 意味着字符串 a 和 b 连接。 

 

 示例 1： 

 

 
输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出：true
 

 示例 2： 

 
输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出：false
 

 示例 3： 

 
输入：s1 = "", s2 = "", s3 = ""
输出：true
 

 

 提示： 

 
 0 <= s1.length, s2.length <= 100 
 0 <= s3.length <= 200 
 s1、s2、和 s3 都由小写英文字母组成 
 

 

 注意：本题与主站 97 题相同： https://leetcode-cn.com/problems/interleaving-string/ 
 Related Topics 字符串 动态规划 👍 23 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3: return False
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        dp[0][0] = True
        # 赋初值，第一列表示当s2为空时s1与s3是否匹配
        for i in range(1, n1 + 1):
            if s1[i - 1] == s3[i - 1]:
                dp[i][0] = dp[i - 1][0]
        # 赋初值，第一排表示当s1为空时s2与s3是否匹配
        for j in range(1, n2 + 1):
            if s2[j - 1] == s3[j - 1]:
                dp[0][j] = dp[0][j - 1]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = (dp[i - 1][j] | dp[i][j - 1])
                elif s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i - 1][j]
                elif s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j - 1]
        return dp[n1][n2]

# leetcode submit region end(Prohibit modification and deletion)
