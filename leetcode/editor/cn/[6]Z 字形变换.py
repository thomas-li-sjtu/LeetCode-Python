# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。 
# 
#  比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下： 
# 
#  
# P   A   H   N
# A P L S I I G
# Y   I   R 
# 
#  之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。 
# 
#  请你实现这个将字符串进行指定行数变换的函数： 
# 
#  
# string convert(string s, int numRows); 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "PAYPALISHIRING", numRows = 3
# 输出："PAHNAPLSIIGYIR"
#  
# 示例 2：
# 
#  
# 输入：s = "PAYPALISHIRING", numRows = 4
# 输出："PINALSIGYAHRPI"
# 解释：
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "A", numRows = 1
# 输出："A"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 由英文字母（小写和大写）、',' 和 '.' 组成 
#  1 <= numRows <= 1000 
#  
#  Related Topics 字符串 
#  👍 1119 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        matrix = [[0]*numRows]
        if numRows == 1:
            return s
        counter = 0
        rows = 0
        reverse_flag = 0
        for i in range(len(s)):
            matrix[rows][counter] = s[i]
            if not reverse_flag:
                counter += 1
            else:
                counter -= 1
                rows += 1
                matrix.append([0]*numRows)

            if counter == 0 and reverse_flag:
                counter = 0
                reverse_flag = 0
            elif counter == numRows and not reverse_flag:
                counter = numRows-2
                if counter != 0:  # 特殊情况：numRows = 2
                    reverse_flag = 1
                rows += 1
                matrix.append([0] * numRows)

        new_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        s = ''.join([j for i in new_matrix for j in i if j != 0])
        return s

# leetcode submit region end(Prohibit modification and deletion)
