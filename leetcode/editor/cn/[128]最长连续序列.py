# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。 
# 
#  请你设计并实现时间复杂度为 O(n) 的算法解决此问题。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 105 
#  -109 <= nums[i] <= 109 
#  
#  Related Topics 并查集 数组 哈希表 
#  👍 1062 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_length = 0
        nums_set = set(nums)
        for i in nums_set:
            if i-1 not in nums_set:  # 重点在于这个判断！这个判断使得不重复遍历！
                cur_length = 1
                cur_num = i
                while cur_num+1 in nums_set:
                    cur_num += 1
                    cur_length += 1
                max_length = max(cur_length, max_length)
        return max_length
# leetcode submit region end(Prohibit modification and deletion)
