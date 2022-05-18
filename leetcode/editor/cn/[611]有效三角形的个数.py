"""
给定一个包含非负整数的数组 nums ，返回其中可以组成三角形三条边的三元组个数。 

 

 示例 1: 

 
输入: nums = [2,2,3,4]
输出: 3
解释:有效的组合是: 
2,3,4 (使用第一个 2)
2,3,4 (使用第二个 2)
2,2,3
 

 示例 2: 

 
输入: nums = [4,2,3,4]
输出: 4 

 

 提示: 

 
 1 <= nums.length <= 1000 
 0 <= nums[i] <= 1000 
 
 Related Topics 贪心 数组 双指针 二分查找 排序 👍 382 👎 0

"""
from typing import List
import bisect


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        # print(nums)
        length = len(nums)
        counter = 0
        for i in range(length - 2):
            for j in range(i + 1, length - 1):
                tmp_sum = nums[i] + nums[j]
                tmp_index = bisect.bisect_left(nums, tmp_sum)
                # print(tmp_index, tmp_sum, j)
                counter += tmp_index - j - 1 if tmp_index >= j + 1 else 0
                # print(counter)

        return counter


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.triangleNumber([4, 2, 3, 4]))
