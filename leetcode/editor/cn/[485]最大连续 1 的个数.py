# 给定一个二进制数组， 计算其中最大连续 1 的个数。 
# 
#  
# 
#  示例： 
# 
#  
# 输入：[1,1,0,1,1,1]
# 输出：3
# 解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
#  
# 
#  
# 
#  提示： 
# 
#  
#  输入的数组只包含 0 和 1 。 
#  输入数组的长度是正整数，且不超过 10,000。 
#  
#  Related Topics 数组 
#  👍 283 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        out = 0
        for i in nums:
            if i == 1:
                counter += 1
            else:
                if counter > out:
                    out = counter
                counter = 0
        if counter > out:
            out = counter
        return out
# leetcode submit region end(Prohibit modification and deletion)
