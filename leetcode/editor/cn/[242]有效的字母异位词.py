# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。 
# 
#  注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "anagram", t = "nagaram"
# 输出: true
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "rat", t = "car"
# 输出: false 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length, t.length <= 5 * 104 
#  s 和 t 仅包含小写字母 
#  
# 
#  
# 
#  进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？ 
#  Related Topics 哈希表 字符串 排序 
#  👍 463 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = {}
        for i in s:
            if s_dict.get(i):
                s_dict[i] += 1
            else:
                s_dict[i] = 1
        t_dict = {}
        for i in t:
            if t_dict.get(i):
                t_dict[i] += 1
            else:
                t_dict[i] = 1
        if set(s_dict.keys()) != set(t_dict.keys()):
            return False
        for key, value in s_dict.items():
            if t_dict[key] != value:
                return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
