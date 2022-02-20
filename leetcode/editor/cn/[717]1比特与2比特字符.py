# 有两种特殊字符： 
# 
#  
#  第一种字符可以用一个比特 0 来表示 
#  第二种字符可以用两个比特(10 或 11)来表示、 
#  
# 
#  给定一个以 0 结尾的二进制数组 bits ，如果最后一个字符必须是一位字符，则返回 true 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: bits = [1, 0, 0]
# 输出: true
# 解释: 唯一的编码方式是一个两比特字符和一个一比特字符。
# 所以最后一个字符是一比特字符。
#  
# 
#  示例 2: 
# 
#  
# 输入: bits = [1, 1, 1, 0]
# 输出: false
# 解释: 唯一的编码方式是两比特字符和两比特字符。
# 所以最后一个字符不是一比特字符。
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= bits.length <= 1000 
#  bits[i] == 0 or 1 
#  
#  Related Topics 数组 
#  👍 255 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        flag = {10: 0, 11: 0}
        length = len(bits) - 1
        for index, char in enumerate(bits):
            if char == 1:
                if flag[10] == 0 and flag[11] == 0 and bits[index+1] == 0:
                    flag[10] = 1
                elif flag[11] == 0 and bits[index+1] == 1:
                    flag[11] = 1
                else:
                    flag[11] = 0
            else:
                if flag[10] == 1 and index != length:
                    flag[10] = 0
                elif flag[10] == 1 and index == length:
                    return False
        return True
# leetcode submit region end(Prohibit modification and deletion)

