# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。 
# 
#  回文串 是正着读和反着读都一样的字符串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "a"
# 输出：[["a"]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 16 
#  s 仅由小写英文字母组成 
#  
#  Related Topics 字符串 动态规划 回溯 
#  👍 1043 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # 将字符串 s 的每个子串 s[i..j] 是否为回文串预处理出来，使用动态规划即可
        func = [[] for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(len(s)):
                func[i].append(True if i >= j else False)
        for i in range(len(s)-1, -1, -1):
            for j in range(len(s)):
                if i < len(s)-1 and j > 0 and i < j:
                    func[i][j] = func[i+1][j-1] and s[i] == s[j]

        result = []
        ans = []

        def dfs(i):
            if i == len(s):
                result.append(ans[:])
                return
            else:
                for j in range(i, len(s)):
                    if func[i][j]:
                        ans.append(s[i:j+1])
                        dfs(j+1)
                        ans.pop()
        dfs(0)
        return result

# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.partition("abbab"))
