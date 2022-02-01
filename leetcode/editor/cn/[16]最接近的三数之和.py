# 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。 
# 
#  返回这三个数的和。 
# 
#  假定每组输入只存在恰好一个解。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,0,0], target = 1
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= nums.length <= 1000 
#  -1000 <= nums[i] <= 1000 
#  -104 <= target <= 104 
#  
#  Related Topics 数组 双指针 排序 
#  👍 1028 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        best = 1000000
        nums.sort()
        sums = -100

        for i in range(len(nums)-1):
            j = i + 1
            k = len(nums)-1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while j < k:
                if abs(nums[i]+nums[j]+nums[k] - target) < best:
                    sums = nums[i]+nums[j]+nums[k]
                    best = abs(nums[i]+nums[j]+nums[k] - target)
                if nums[i]+nums[j]+nums[k] < target:
                    j += 1
                elif nums[i]+nums[j]+nums[k] > target:
                    k -= 1
                else:
                    return target
        return sums
# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
print(s.threeSumClosest([1,2,4,8,16,32,64,128], 82))
