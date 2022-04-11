"""
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。 

 

 示例 1： 

 
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
 

 示例 2： 

 
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

 

 提示： 

 
 1 <= nums.length <= 8 
 -10 <= nums[i] <= 10 
 
 Related Topics 数组 回溯 👍 1015 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        start, end = 0, len(nums)

        def permutation(m, n):
            # m之前已经完成全排序，考虑m到n之间的全排序
            if m == n:
                # 出口
                res.add(tuple(nums[:]))
                return
            else:
                for i in range(m, n, 1):  # nums[i]为要做全排列的第一个数
                    nums[m], nums[i] = nums[i], nums[m]  # 把要做全排列的数放到开头（即m所在的位置）
                    permutation(m+1, n)
                    nums[m], nums[i] = nums[i], nums[m]  # 恢复初始的排序避免重复

        permutation(start, end)

        return [list(i) for i in res]
# leetcode submit region end(Prohibit modification and deletion)
