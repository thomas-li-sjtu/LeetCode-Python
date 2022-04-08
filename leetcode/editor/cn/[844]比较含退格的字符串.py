"""
给定 s 和 t 两个字符串，当它们分别被输入到空白的文本编辑器后，如果两者相等，返回 true 。# 代表退格字符。 

 注意：如果对空文本输入退格字符，文本继续为空。 

 

 示例 1： 

 
输入：s = "ab#c", t = "ad#c"
输出：true
解释：s 和 t 都会变成 "ac"。
 

 示例 2： 

 
输入：s = "ab##", t = "c#d#"
输出：true
解释：s 和 t 都会变成 ""。
 

 示例 3： 

 
输入：s = "a#c", t = "b"
输出：false
解释：s 会变成 "c"，但 t 仍然是 "b"。 

 

 提示： 

 
 1 <= s.length, t.length <= 200 
 s 和 t 只含有小写字母以及字符 '#' 
 

 

 进阶： 

 
 你可以用 O(n) 的时间复杂度和 O(1) 的空间复杂度解决该问题吗？ 
 
 Related Topics 栈 双指针 字符串 模拟 👍 404 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        res_s = []
        res_t = []
        s_len, t_len, length = len(s), len(t), max(len(s), len(t))
        for i in range(len(s)):
            if s[i] != "#":
                res_s.append(s[i])
            else:
                if res_s:
                    res_s.pop()
                else:
                    continue
        for i in range(len(t)):
            if t[i] != "#":
                res_t.append(t[i])
            else:
                if res_t:
                    res_t.pop()
                else:
                    continue
        if "".join(res_s) == "".join(res_t):
            return True
        else:
            return False
# leetcode submit region end(Prohibit modification and deletion)
