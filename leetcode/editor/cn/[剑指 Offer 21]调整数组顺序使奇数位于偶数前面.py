"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。 

 

 示例： 

 
输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。 

 

 提示： 

 
 0 <= nums.length <= 50000 
 0 <= nums[i] <= 10000 
 
 Related Topics 数组 双指针 排序 👍 229 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        # 初始化： i, j 双指针，分别指向数组 nums 左右两端；
        # 循环交换： 当 i = j 时跳出；
        #          指针 i 遇到奇数则执行 i = i + 1 跳过，直到找到偶数；
        #          指针 j 遇到偶数则执行 j = j - 1 跳过，直到找到奇数；
        #          交换 nums[i] 和 nums[j] 值；

        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] & 1 == 1: i += 1
            while i < j and nums[j] & 1 == 0: j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums

# leetcode submit region end(Prohibit modification and deletion)
