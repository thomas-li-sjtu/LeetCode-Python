# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b
# ], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）： 
# 
#  
#  0 <= a, b, c, d < n 
#  a、b、c 和 d 互不相同 
#  nums[a] + nums[b] + nums[c] + nums[d] == target 
#  
# 
#  你可以按 任意顺序 返回答案 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,0,-1,0,-2,2], target = 0
# 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,2,2,2,2], target = 8
# 输出：[[2,2,2,2]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 200 
#  -109 <= nums[i] <= 109 
#  -109 <= target <= 109 
#  
#  Related Topics 数组 双指针 排序 
#  👍 1102 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        res = []
        nums.sort()
        for i in range(len(nums) - 3):
            tar = target - nums[i]
            candidate = [nums[i]]
            for group in self.threeSum(nums[i+1:], tar):
                if group:
                    # print(candidate, group)
                    candidate.extend(group)
                    res.append(tuple(candidate))
                    candidate = [nums[i]]
        res = [list(i) for i in list(set(res))]
        return res

    @staticmethod
    def threeSum(nums, target):
        res = []
        for i in range(len(nums) - 2):
            point1, point2 = i+1, len(nums) - 1
            tar = target - nums[i]
            while point1 < point2:
                if nums[point1] + nums[point2] == tar:
                    res.append([nums[i], nums[point1], nums[point2]])
                    point1 += 1
                    point2 -= 1
                elif nums[point1] + nums[point2] < tar:
                    point1 += 1
                else:
                    point2 -= 1
        return res


# leetcode submit region end(Prohibit modification and deletion)
