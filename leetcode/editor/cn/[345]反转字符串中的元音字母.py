# 给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。 
# 
#  元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "hello"
# 输出："holle"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "leetcode"
# 输出："leotcede" 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 3 * 105 
#  s 由 可打印的 ASCII 字符组成 
#  
#  Related Topics 双指针 字符串 
#  👍 230 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        letters = ['a', 'e', 'i', 'o', 'u']
        for i in range(5):
            letters.append(letters[i].upper())
        index = []
        for i, char in enumerate(s):
            if char in letters:
                index.append(i)
        index_reverse = index[::-1]
        new_s = list(s)
        for i in range(len(index)):
            new_s[index[i]] = s[index_reverse[i]]
        return "".join(new_s)
# leetcode submit region end(Prohibit modification and deletion)
