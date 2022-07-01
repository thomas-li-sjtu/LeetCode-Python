"""
给定一个非空字符串 s，请判断如果 最多 从字符串中删除一个字符能否得到一个回文字符串。 

 

 示例 1: 

 
输入: s = "aba"
输出: true
 

 示例 2: 

 
输入: s = "abca"
输出: true
解释: 可以删除 "c" 字符 或者 "b" 字符
 

 示例 3: 

 
输入: s = "abc"
输出: false 

 

 提示: 

 
 1 <= s.length <= 10⁵ 
 s 由小写英文字母组成 
 

 

 注意：本题与主站 680 题相同： https://leetcode-cn.com/problems/valid-palindrome-ii/ 
 Related Topics 贪心 双指针 字符串 👍 38 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        else:
            def checkPalindrome(low, high):
                i, j = low, high
                while i < j:
                    if s[i] != s[j]:
                        return False
                    i += 1
                    j -= 1
                return True

            low, high = 0, len(s) - 1
            while low < high:
                if s[low] == s[high]:
                    low += 1
                    high -= 1
                else:
                    return checkPalindrome(low + 1, high) or checkPalindrome(low, high - 1)
# leetcode submit region end(Prohibit modification and deletion)
