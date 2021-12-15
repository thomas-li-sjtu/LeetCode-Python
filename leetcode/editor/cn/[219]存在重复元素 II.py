# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值
#  至多为 k。 
# 
#  
# 
#  示例 1: 
# 
#  输入: nums = [1,2,3,1], k = 3
# 输出: true 
# 
#  示例 2: 
# 
#  输入: nums = [1,0,1,1], k = 1
# 输出: true 
# 
#  示例 3: 
# 
#  输入: nums = [1,2,3,1,2,3], k = 2
# 输出: false 
#  Related Topics 数组 哈希表 滑动窗口 
#  👍 341 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict_index = {}
        for i, num in enumerate(nums):
            if dict_index.get(num):
                dict_index[num].append(i)
            else:
                dict_index[num] = [i]
        flag = 0
        for key, value in dict_index.items():
            if len(value) > 1:
                for i in range(len(value)-1):
                    for j in range(i+1, len(value)):
                        if value[j]-value[i] <= k:
                            flag = 1
        if flag:
            return True
        else:
            return False
# leetcode submit region end(Prohibit modification and deletion)
