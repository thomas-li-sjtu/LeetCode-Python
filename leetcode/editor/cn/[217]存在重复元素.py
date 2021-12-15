# 给定一个整数数组，判断是否存在重复元素。 
# 
#  如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: [1,2,3,1]
# 输出: true 
# 
#  示例 2: 
# 
#  
# 输入: [1,2,3,4]
# 输出: false 
# 
#  示例 3: 
# 
#  
# 输入: [1,1,1,3,3,4,3,2,4,2]
# 输出: true 
#  Related Topics 数组 哈希表 排序 
#  👍 530 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import collections
        num_dict = collections.defaultdict(int)
        for i in nums:
            num_dict[i] += 1
        for key, value in num_dict.items():
            if value >= 2:
                return True
        return False
# leetcode submit region end(Prohibit modification and deletion)
