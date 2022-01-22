# 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。 
# 
#  注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [10,2]
# 输出："210" 
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,30,34,5,9]
# 输出："9534330"
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1]
# 输出："1"
#  
# 
#  示例 4： 
# 
#  
# 输入：nums = [10]
# 输出："10"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 100 
#  0 <= nums[i] <= 109 
#  
#  Related Topics 贪心 字符串 排序 
#  👍 856 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if self.compare(str(nums[i]), str(nums[j])):
                    nums[i], nums[j] = nums[j], nums[i]
        result = "".join([str(i) for i in nums])
        flag = 1
        for i in result:
            if i != "0":
                flag = 0
                break
        if flag:
            return "0"
        else:
            return result

    def compare(self, num1, num2):
        if int(num1+num2) > int(num2+num1):
            return False
        else:
            return True
# leetcode submit region end(Prohibit modification and deletion)
