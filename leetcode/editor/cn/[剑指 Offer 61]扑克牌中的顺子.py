"""
从若干副扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以
看成任意数字。A 不能视为 14。 

 

 示例 1: 

 
输入: [1,2,3,4,5]
输出: True 

 

 示例 2: 

 
输入: [0,0,1,2,5]
输出: True 

 

 限制： 

 数组长度为 5 

 数组的数取值为 [0, 13] . 
 Related Topics 数组 排序 👍 245 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        if nums.count(0) == 0:
            nums.sort()
            for i in range(len(nums)-1):
                if nums[i+1] - 1 != nums[i]:
                    return False
            return True
        else:
            nums.sort()

            index = -1
            for i in range(len(nums)):
                if nums[i] != 0:
                    index = i
                    break
            if index == 4 or index == 5:
                return True

            counter = 0
            for i in range(index, len(nums)-1):
                if nums[i+1] == nums[i]:
                    return False
                if nums[i+1] - 1 != nums[i]:
                    counter += nums[i+1] - 1 - nums[i]
            if counter <= index:
                return True
            return False

# leetcode submit region end(Prohibit modification and deletion)
