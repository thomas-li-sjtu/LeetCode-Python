"""
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。 

 

 示例 1： 

 输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
 

 示例 2： 

 输入：nums =
输出：[2,10] 或 [10,2] 

 

 限制： 

 
 2 <= nums.length <= 10000 
 

 
 Related Topics 位运算 数组 👍 656 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        res = nums[0]
        for i in range(1, len(nums)):
            res = res ^ nums[i]
        index = 0
        while res & 1 == 0:
            index += 1
            res >>= 1
        out_1, out_2 = 0, 0
        for i in nums:
            if i >> index & 1 == 0:
                out_1 ^= i
            else:
                out_2 ^= i
        return [out_1, out_2]
# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.singleNumbers())
