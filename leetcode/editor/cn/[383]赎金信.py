# 为了不在赎金信中暴露字迹，从杂志上搜索各个需要的字母，组成单词来表达意思。 
# 
#  给你一个赎金信 (ransomNote) 字符串和一个杂志(magazine)字符串，判断 ransomNote 能不能由 magazines 里面的字符
# 构成。 
# 
#  如果可以构成，返回 true ；否则返回 false 。 
# 
#  magazine 中的每个字符只能在 ransomNote 中使用一次。 
# 
#  .
# 
#  示例 1： 
# 
#  
# 输入：ransomNote = "a", magazine = "b"
# 输出：false
#  
# 
#  示例 2： 
# 
#  
# 输入：ransomNote = "aa", magazine = "ab"
# 输出：false
#  
# 
#  示例 3： 
# 
#  
# 输入：ransomNote = "aa", magazine = "aab"
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= ransomNote.length, magazine.length <= 105 
#  ransomNote 和 magazine 由小写英文字母组成 
#  
#  Related Topics 哈希表 字符串 计数 
#  👍 247 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        note_dict = {}
        mag_dict = {}
        for i in ransomNote:
            if note_dict.get(i):
                note_dict[i] += 1
            else:
                note_dict[i] = 1
        for i in magazine:
            if mag_dict.get(i):
                mag_dict[i] += 1
            else:
                mag_dict[i] = 1
        for key, value in note_dict.items():
            if not mag_dict.get(key) or mag_dict[key] < value:
                return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
