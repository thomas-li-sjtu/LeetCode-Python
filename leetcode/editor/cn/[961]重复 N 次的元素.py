# 在大小为 2N 的数组 A 中有 N+1 个不同的元素，其中有一个元素重复了 N 次。 
# 
#  返回重复了 N 次的那个元素。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：[1,2,3,3]
# 输出：3
#  
# 
#  示例 2： 
# 
#  
# 输入：[2,1,2,5,3,2]
# 输出：2
#  
# 
#  示例 3： 
# 
#  
# 输入：[5,1,5,2,5,3,5,4]
# 输出：5
#  
# 
#  
# 
#  提示： 
# 
#  
#  4 <= A.length <= 10000 
#  0 <= A[i] < 10000 
#  A.length 为偶数 
#  
#  Related Topics 数组 哈希表 
#  👍 103 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = dict()
        for num in nums:
            dic[num] = dic.get(num, 0)+1
            if dic.get(num) != 1:
                return num
# leetcode submit region end(Prohibit modification and deletion)
