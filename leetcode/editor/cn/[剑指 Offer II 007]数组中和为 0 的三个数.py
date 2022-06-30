"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a ，b ，c ，使得 a + b + c = 0 ？请找出所有和为 0 且 不重
复 的三元组。 

 

 示例 1： 

 
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
 

 示例 2： 

 
输入：nums = []
输出：[]
 

 示例 3： 

 
输入：nums = [0]
输出：[]
 

 

 提示： 

 
 0 <= nums.length <= 3000 
 -10⁵ <= nums[i] <= 10⁵ 
 

 

 注意：本题与主站 15 题相同：https://leetcode-cn.com/problems/3sum/ 
 Related Topics 数组 双指针 排序 👍 66 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        if length <= 2:
            return []
        res = set()
        for i in range(length - 2):
            target = -nums[i]
            start, end = i + 1, length - 1

            while start < end:
                if nums[start] + nums[end] < target:
                    start += 1
                elif nums[start] + nums[end] > target:
                    end -= 1
                else:
                    res.add((nums[i], nums[start], nums[end]))
                    start += 1
                    end -= 1
        return [list(i) for i in res]
# leetcode submit region end(Prohibit modification and deletion)
