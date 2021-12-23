# 给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。 
# 
#  美式键盘 中： 
# 
#  
#  第一行由字符 "qwertyuiop" 组成。 
#  第二行由字符 "asdfghjkl" 组成。 
#  第三行由字符 "zxcvbnm" 组成。 
#  
# 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：words = ["Hello","Alaska","Dad","Peace"]
# 输出：["Alaska","Dad"]
#  
# 
#  示例 2： 
# 
#  
# 输入：words = ["omk"]
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：words = ["adsdf","sfd"]
# 输出：["adsdf","sfd"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= words.length <= 20 
#  1 <= words[i].length <= 100 
#  words[i] 由英文字母（小写和大写字母）组成 
#  
#  Related Topics 数组 哈希表 字符串 
#  👍 193 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        key_board = {"line1": {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'},
                     "line2": {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'},
                     "line3": {'z', 'x', 'c', 'v', 'b', 'n', 'm'}}
        result = []
        for tmp in words:
            word = set(list(tmp.lower()))
            if word & key_board["line1"] == word or word & key_board["line2"] == word or word & key_board["line3"] == word:
                result.append(tmp)
        return result
# leetcode submit region end(Prohibit modification and deletion)
