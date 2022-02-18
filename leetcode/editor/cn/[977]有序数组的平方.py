# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。 
# 
#  
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
# 解释：平方后，数组变为 [16,1,0,9,100]
# 排序后，数组变为 [0,1,9,16,100] 
# 
#  示例 2： 
# 
#  
# 输入：nums = [-7,-3,2,3,11]
# 输出：[4,9,9,49,121]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 104 
#  -104 <= nums[i] <= 104 
#  nums 已按 非递减顺序 排序 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  请你设计时间复杂度为 O(n) 的算法解决本问题 
#  
#  Related Topics 数组 双指针 排序 
#  👍 432 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        while left < len(nums) and nums[left] <= 0:
            if nums[left] <= 0:
                nums[left] = nums[left]*nums[left]
                left += 1
        a = nums[:left][::-1]
        b = [i*i for i in nums[left:]]
        res = []

        i, j = 0, 0
        while i < len(a) and j < len(b):
            if i < len(a) and a[i] <= b[j]:
                res.append(a[i])
                i += 1
            if j < len(b) and i < len(a) and b[j] <= a[i]:
                res.append(b[j])
                j += 1
        if i == len(a):
            res.extend(b[j:])
        elif j == len(b):
            res.extend(a[i:])
        return res

# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.sortedSquares([-7,-3,2,3,11]))