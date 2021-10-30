# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重
# 复的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [0]
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 3000 
#  -105 <= nums[i] <= 105 
#  
#  Related Topics 数组 双指针 排序 
#  👍 3917 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        savelst = []
        nums.sort()
        for i in range(len(nums)):
            # 第一个数一定要是小于等于0，如果大于零三个数的和不可能等于0
            if (i == 0 or nums[i] != nums[i - 1]) and (nums[i] <= 0):
                k = i + 1
                j = len(nums) - 1  # ikj都是下标
                while k < j:
                    if nums[i] == nums[k] == nums[j] == 0:
                        savelst.append([0, 0, 0])
                        break
                    s = nums[i] + nums[k] + nums[j]
                    if s == 0:
                        savelst.append([nums[i], nums[k], nums[j]])
                        k += 1
                        while nums[k] == nums[k - 1] and (k + 1 < len(nums) - 1):
                            k += 1
                            # j减到与之不相等的数
                        j -= 1
                        while nums[j] == nums[j + 1]:
                            j -= 1
                    elif s > 0:
                        j -= 1
                        while nums[j] == nums[j + 1]:
                            j -= 1
                    else:
                        k += 1
                        while nums[k] == nums[k - 1] and (k + 1 < len(nums) - 1):
                            k += 1
        return savelst
# leetcode submit region end(Prohibit modification and deletion)
