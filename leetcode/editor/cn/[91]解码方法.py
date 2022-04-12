"""
一条包含字母 A-Z 的消息通过以下映射进行了 编码 ： 

 
'A' -> "1"
'B' -> "2"
...
'Z' -> "26" 

 要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为： 

 
 "AAJF" ，将消息分组为 (1 1 10 6) 
 "KJF" ，将消息分组为 (11 10 6) 
 

 注意，消息不能分组为 (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。 

 给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。 

 题目数据保证答案肯定是一个 32 位 的整数。 

 

 示例 1： 

 
输入：s = "12"
输出：2
解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
 

 示例 2： 

 
输入：s = "226"
输出：3
解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
 

 示例 3： 

 
输入：s = "0"
输出：0
解释：没有字符映射到以 0 开头的数字。
含有 0 的有效映射是 'J' -> "10" 和 'T'-> "20" 。
由于没有字符，因此没有有效的方法对此进行解码，因为所有数字都需要映射。
 

 

 提示： 

 
 1 <= s.length <= 100 
 s 只包含数字，并且可能包含前导零。 
 
 Related Topics 字符串 动态规划 👍 1152 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numDecodings(self, s: str) -> int:
        dict_1 = {str(i): 1 for i in range(1, 11)}
        dict_2 = {str(i): 2 for i in range(11, 20)}
        dict_4 = {"20": 1}
        dict_3 = {str(i): 2 for i in range(21, 27)}
        count_dict = {**dict_1, **dict_2, **dict_4, **dict_3}

        res = []
        if s[0] == '0':
            return 0
        else:
            res.append(1)
        if count_dict.get(s[:2]):
            res.append(count_dict[s[:2]])
        else:
            if s[1] == '0':
                return 0
            else:
                res.append(1)

        pos = 2
        while pos < len(s):
            if s[pos] == '0':
                if s[pos - 1] == '0' or not count_dict.get(s[pos - 1] + s[pos]):
                    return 0
                else:
                    res.append(res[pos - 2])
            elif count_dict.get(s[pos - 1] + s[pos]) and count_dict[s[pos - 1] + s[pos]] == 2:
                res.append(res[pos - 1] + res[pos - 2])
            elif count_dict.get(s[pos - 1] + s[pos]) and count_dict[s[pos - 1] + s[pos]] == 1:
                res.append(res[pos - 1])
            elif not count_dict.get(s[pos - 1] + s[pos]) and (int(s[pos - 1] + s[pos]) > 26 or s[pos - 1] == '0'):
                res.append(res[pos - 1])
            pos += 1

        return res[-1]


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.numDecodings("1201234"))
print(s.numDecodings("230"))
