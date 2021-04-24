# 编写一个函数来查找字符串数组中的最长公共前缀。 
# 
#  如果不存在公共前缀，返回空字符串 ""。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
#  
# 
#  示例 2： 
# 
#  
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= strs.length <= 200 
#  0 <= strs[i].length <= 200 
#  strs[i] 仅由小写英文字母组成 
#  
#  Related Topics 字符串 
#  👍 1578 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        tmp_char = [i for i in strs[0]]
        result = ''
        for char in range(len(tmp_char)):
            for i in range(0, len(strs)):
                if char >= len(strs[i]):
                    return result
                if tmp_char[char] != strs[i][char]:
                    return result
                if i == len(strs)-1:
                    result += tmp_char[char]
        return result  # 特殊情况 [""]
# leetcode submit region end(Prohibit modification and deletion)
