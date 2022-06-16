"""
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。 

 
 '.' 匹配任意单个字符 
 '*' 匹配零个或多个前面的那一个元素 
 

 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。 
 

 示例 1： 

 
输入：s = "aa", p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。
 

 示例 2: 

 
输入：s = "aa", p = "a*"
输出：true
解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
 

 示例 3： 

 
输入：s = "ab", p = ".*"
输出：true
解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
 

 

 提示： 

 
 1 <= s.length <= 20 
 1 <= p.length <= 30 
 s 只包含从 a-z 的小写字母。 
 p 只包含从 a-z 的小写字母，以及字符 . 和 *。 
 保证每次出现字符 * 时，前面都匹配到有效的字符 
 
 Related Topics 递归 字符串 动态规划 👍 3032 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0:
            return len(s) == 0

        if len(p) > 1 and p[1] == "*":
            if len(s) != 0 and (s[0] == p[0] or p[0] == "."):
                return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])  # 如果s[0] == p[0]，要看接下来*匹配了一次，或者*匹配了零次
            else:
                return self.isMatch(s, p[2:])  # *匹配了零次
        else:
            return len(s) != 0 and (s[0] == p[0] or p[0] == ".") and self.isMatch(s[1:], p[1:])

# leetcode submit region end(Prohibit modification and deletion)
