"""
如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。 

 
 例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。 
 

 
 
 给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。 

 子数组 是数组中的一个连续序列。 

 

 示例 1： 

 
输入：nums = [1,2,3,4]
输出：3
解释：nums 中有三个子等差数组：[1, 2, 3]、[2, 3, 4] 和 [1,2,3,4] 自身。
 

 示例 2： 

 
输入：nums = [1]
输出：0
 

 

 提示： 

 
 1 <= nums.length <= 5000 
 -1000 <= nums[i] <= 1000 
 
 
 
 Related Topics 数组 动态规划 👍 436 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        def slide_num(n, m):
            return n-m+1

        result = 0
        if len(nums) < 3:
            return 0
        sub = [nums[i+1] - nums[i] for i in range(len(nums)-1)]
        tmp_sub, counter = sub[0], 1
        for i in range(1, len(sub)):
            if sub[i] == tmp_sub:
                counter += 1
            else:
                if counter >= 2:
                    for j in range(counter, 1, -1):
                        result += slide_num(counter, j)
                counter = 1
                tmp_sub = sub[i]
        if counter >= 2:
            for j in range(counter, 1, -1):
                result += slide_num(counter, j)

        return result
# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.numberOfArithmeticSlices( [1,2,3,4]))
