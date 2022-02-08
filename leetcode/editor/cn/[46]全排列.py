# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1]
# 输出：[[1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 6 
#  -10 <= nums[i] <= 10 
#  nums 中的所有整数 互不相同 
#  
#  Related Topics 数组 回溯 
#  👍 1754 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import copy
        # 任取一个数打头，对后面n-1个数进行全排序，要求n-1个数的全排序，则要求n-2个数的全排序……
        # 直到要求的全排序只有一个数，找到出口
        res = []
        start, end = 0, len(nums)

        def permutation(m, n):
            # m之前已经完成全排序，考虑m到n之间的全排序
            if m == n:
                # 出口
                res.append(copy.deepcopy(nums))
                return
            else:
                for i in range(m, n, 1):  # nums[i]为要做全排列的第一个数
                    nums[m], nums[i] = nums[i], nums[m]  # 把要做全排列的数放到开头（即m所在的位置）
                    permutation(m+1, n)
                    nums[m], nums[i] = nums[i], nums[m]  # 恢复初始的排序避免重复

        permutation(start, end)
        return res


# leetcode submit region end(Prohibit modification and deletion)
