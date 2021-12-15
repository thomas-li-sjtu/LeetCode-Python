# 给定一个字符串 s 和一个整数 k，从字符串开头算起，每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符。 
# 
#  
#  如果剩余字符少于 k 个，则将剩余字符全部反转。 
#  如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "abcdefg", k = 2
# 输出："bacdfeg"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "abcd", k = 2
# 输出："bacd"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 104 
#  s 仅由小写英文组成 
#  1 <= k <= 104 
#  
#  Related Topics 双指针 字符串 
#  👍 220 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        flag = 0
        lenght = len(s)
        while flag < lenght:
            # if flag + k > lenght:
            #     return ''.join(s)
            pre = flag  # pre代表每次的最前面的
            cur = 0
            for _ in range(k // 2):
                if flag + k > lenght and flag <= lenght - cur - 1:
                    s[flag], s[lenght - cur - 1] = s[lenght - cur - 1], s[flag]
                    flag += 1
                    cur += 1
                elif flag > lenght - cur - 1:
                    break
                else:
                    s[flag + cur], s[flag - cur + k - 1] = s[flag - cur + k - 1], s[flag + cur]
                    cur += 1

            flag = pre + 2 * k
        return ''.join(s)

# leetcode submit region end(Prohibit modification and deletion)
