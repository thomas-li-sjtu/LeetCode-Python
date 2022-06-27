"""
给定字符串列表 strs ，返回其中 最长的特殊序列 。如果最长特殊序列不存在，返回 -1 。 

 特殊序列 定义如下：该序列为某字符串 独有的子序列（即不能是其他字符串的子序列）。 

 s 的 子序列可以通过删去字符串 s 中的某些字符实现。 

 
 例如，"abc" 是 "aebdc" 的子序列，因为您可以删除"aebdc"中的下划线字符来得到 "abc" 。"aebdc"的子序列还包括"aebdc"、 
"aeb" 和 "" (空字符串)。 
 

 

 示例 1： 

 
输入: strs = ["aba","cdc","eae"]
输出: 3
 

 示例 2: 

 
输入: strs = ["aaa","aaa","aa"]
输出: -1
 

 

 提示: 

 
 2 <= strs.length <= 50 
 1 <= strs[i].length <= 10 
 strs[i] 只包含小写英文字母 
 
 Related Topics 数组 哈希表 双指针 字符串 排序 👍 133 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def check(strs1,strs2):
            m = len(strs1)
            n = len(strs2)
            if n < m:
                return False
            dp = [[0] * (n+1) for _ in range(m+1)]

            for i in range(1, m+1):
                for j in range(1, n+1):
                    if strs1[i-1] == strs2[j-1]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])

                    if dp[i][j] == m:
                        return True
            return False

        res = -1
        for i in range(len(strs)):
            if len(strs[i]) < res:
                continue
            flag = True
            for j in range(len(strs)):
                if i == j:
                    continue
                if check(strs[i],strs[j]):
                    flag = False
            if flag:
                res = max(res, len(strs[i]))

        return res
# leetcode submit region end(Prohibit modification and deletion)
