"""
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。 

 

 示例 1： 

 输入：nums = [3,4,3,3]
输出：4
 

 示例 2： 

 输入：nums = [9,1,7,9,7,9,7]
输出：1 

 

 限制： 

 
 1 <= nums.length <= 10000 
 1 <= nums[i] < 2^31 
 

 
 Related Topics 位运算 数组 👍 351 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 只有一个数出现了一次，那么各个二进制位为1的个数 % 3 便能求出这个数的二进制中哪些位置为1
        bits = [0]*32
        for i in nums:
            j = 0
            while i > 0:
                bits[j] += i % 2
                i >>= 1
                j += 1
        res = 0
        for i in range(len(bits)):
            bits[i] = bits[i] % 3
            if bits[i] != 0:
                res += 2**i
        return res
# leetcode submit region end(Prohibit modification and deletion)
