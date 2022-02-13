# 给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。 
# 
#  字符串 text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：text = "nlaebolko"
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：text = "loonbalxballpoon"
# 输出：2
#  
# 
#  示例 3： 
# 
#  输入：text = "leetcode"
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= text.length <= 10^4 
#  text 全部由小写英文字母组成 
#  
#  Related Topics 哈希表 字符串 计数 
#  👍 74 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        char_dict = {}
        for i in text:
            if i in ["b", "a", "l", "o", "n"]:
                if char_dict.get(i):
                    char_dict[i] += 1
                else:
                    char_dict[i] = 1
        counter = 0
        while True:
            if char_dict.get("b") and char_dict.get("a") and char_dict.get("l") and char_dict.get("o") and char_dict.get("n"):
                if char_dict["b"] - 1 >= 0 \
                        and char_dict["a"] - 1 >= 0 \
                        and char_dict["l"] - 2 >= 0 \
                        and char_dict["o"] - 2 >= 0 \
                        and char_dict["n"] - 1 >= 0:
                    counter += 1
                    char_dict["b"] -= 1
                    char_dict["a"] -= 1
                    char_dict["n"] -= 1
                    char_dict["l"] -= 2
                    char_dict["o"] -= 2
                else:
                    return counter
            else:
                return counter
# leetcode submit region end(Prohibit modification and deletion)
