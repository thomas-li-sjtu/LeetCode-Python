"""
给定两个单词 word1 和 word2 ，返回使得 word1 和 word2 相同所需的最小步数。 

 每步 可以删除任意一个字符串中的一个字符。 

 

 示例 1： 

 
输入: word1 = "sea", word2 = "eat"
输出: 2
解释: 第一步将 "sea" 变为 "ea" ，第二步将 "eat "变为 "ea"
 

 示例 2: 

 
输入：word1 = "leetcode", word2 = "etco"
输出：4
 

 

 提示： 
 

 
 1 <= word1.length, word2.length <= 500 
 word1 和 word2 只包含小写英文字母 
 
 Related Topics 字符串 动态规划 👍 402 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 求最长公共子序列LCS，ans = word1.length() + word2.length() - 2LCS
        dp_matrix = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp_matrix[i][j] = dp_matrix[i - 1][j - 1] + 1
                else:
                    dp_matrix[i][j] = max(dp_matrix[i - 1][j], dp_matrix[i][j - 1])

        return len(word1) + len(word2) - 2*dp_matrix[-1][-1]
# leetcode submit region end(Prohibit modification and deletion)
