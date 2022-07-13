"""
给定一个可包含重复数字的整数集合 nums ，按任意顺序 返回它所有不重复的全排列。 

 

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
 

 

 注意：本题与主站 47 题相同： https://leetcode-cn.com/problems/permutations-ii/ 
 Related Topics 数组 回溯 👍 23 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 每当确定一个i位元素，把它加入HashSet中，后续要交换的元素若和HashSet中某元素相同，则跳过
        def permute_pick(idx):
            if idx == n:
                ans.append(nums[:])
            else:
                switched = set()
                for i in range(idx, n):
                    if nums[i] in switched:
                        continue
                    else:
                        switched.add(nums[i])
                        nums[idx], nums[i] = nums[i], nums[idx]
                        permute_pick(idx + 1)
                        nums[i], nums[idx] = nums[idx], nums[i]

        nums.sort()
        n, ans = len(nums), []
        permute_pick(0)
        return ans

        # def permute_pick(idx):
        #     if idx == n:
        #         ans.add(tuple(nums[:]))
        #     else:
        #         for i in range(idx, n):
        #             nums[idx], nums[i] = nums[i], nums[idx]
        #             permute_pick(idx + 1)
        #             nums[i], nums[idx] = nums[idx], nums[i]
        #
        # n, ans = len(nums), set()
        # permute_pick(0)
        # return [list(i) for i in ans]
# leetcode submit region end(Prohibit modification and deletion)
