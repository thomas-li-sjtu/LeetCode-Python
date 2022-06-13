"""
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。 

 数值（按顺序）可以分成以下几个部分： 

 
 若干空格 
 一个 小数 或者 整数 
 （可选）一个 'e' 或 'E' ，后面跟着一个 整数 
 若干空格 
 

 小数（按顺序）可以分成以下几个部分： 

 
 （可选）一个符号字符（'+' 或 '-'） 
 下述格式之一：
 
 至少一位数字，后面跟着一个点 '.' 
 至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字 
 一个点 '.' ，后面跟着至少一位数字 
 
 
 

 整数（按顺序）可以分成以下几个部分： 

 
 （可选）一个符号字符（'+' 或 '-'） 
 至少一位数字 
 

 部分数值列举如下： 

 
 ["+100", "5e2", "-123", "3.1416", "-1E-16", "0123"] 
 

 部分非数值列举如下： 

 
 ["12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"] 
 

 

 示例 1： 

 
输入：s = "0"
输出：true
 

 示例 2： 

 
输入：s = "e"
输出：false
 

 示例 3： 

 
输入：s = "."
输出：false 

 示例 4： 

 
输入：s = "    .1  "
输出：true
 

 

 提示： 

 
 1 <= s.length <= 20 
 s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，空格 ' ' 或者点 '.' 。 
 
 Related Topics 字符串 👍 348 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isNumber(self, s: str) -> bool:
        if " " in s:
            if s[0] == " ":  # 清除后面的空格
                for i, char in enumerate(s):
                    if char != " ":
                        try:
                            s = s[i:]
                            break
                        except:
                            return False
            if s[-1] == " ":  # 清除前面的空格
                s = s[::-1]
                for i, char in enumerate(s):
                    if char != " ":
                        try:
                            s = s[i:][::-1]
                            break
                        except:
                            return False
        if " " in s:
            return False
        #
        # s = s.replace(" ", "")  # 取消空格
        # if len(s) == 0:
        #     return False
        print(s)
        e_flag = False

        if "e" in s:
            e_flag = True
            s = s.split("e")
            print(s)
        elif "E" in s:
            e_flag = True
            s = s.split("E")

        if e_flag:
            if len(s[0]) == 0 or len(s[1]) == 0:
                return False
            if len(s) != 2:
                return False
            else:
                return (
                    self.is_integer(s[0]) and self.is_integer(s[1])
                    or self.is_float(s[0]) and self.is_integer(s[1])
                )

        if "." in s:
            return self.is_float(s)
        else:
            return self.is_integer(s)

    def is_integer(self, s) -> bool:
        if s[0] == "+" or s[0] == "-":
            try:
                s = s[1:]
            except:
                return False  # 只有符号，没有数字（+，-），false

        digit_flag = False
        for char in s:
            if char.isdigit():
                digit_flag = True
            else:
                return False
        if digit_flag:
            return True
        else:
            return False

    def is_float(self, s) -> bool:
        if s[0] == "+" or s[0] == "-":
            try:
                s = s[1:]
            except:
                return False  # 只有符号，没有数字（+，-），false

        if not s:
            return False
        if s[0] == ".":
            try:
                s = s[1:]
                if s[0] == "-" or s[0] == "+":
                    return False
                return self.is_integer(s)
            except:
                return False
        if s[-1] == ".":
            return self.is_integer(s[:-1])

        s = s.split(".")
        if len(s) != 2:
            return False
        else:
            return self.is_integer(s[0]) and self.is_integer(s[1])

# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.isNumber("1 "))
