# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。 
# 
#  
# 
#  示例： 
# 
#  s = "leetcode"
# 返回 0
# 
# s = "loveleetcode"
# 返回 2
#  
# 
#  
# 
#  提示：你可以假定该字符串只包含小写字母。 
#  Related Topics 队列 哈希表 字符串 计数 
#  👍 456 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        char_dict = collections.defaultdict(list)
        for index, char in enumerate(s):
            char_dict[char] = [char_dict[char][0]+1, char_dict[char][1]] if len(char_dict[char]) else [1, index]

        result = []
        for key, value in char_dict.items():
            if char_dict[key][0] == 1:
                result.append(char_dict[key][1])
        return min(result) if len(result) else -1
# leetcode submit region end(Prohibit modification and deletion)

