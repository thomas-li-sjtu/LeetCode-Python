"""
给定一个可能有重复数字的整数数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。 


 candidates 中的每个数字在每个组合中只能使用一次，解集不能包含重复的组合。 

 

 示例 1: 

 
输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
] 

 示例 2: 

 
输入: candidates = [2,5,2,1,2], target = 5,
输出:
[
[1,2,2],
[5]
] 

 

 提示: 

 
 1 <= candidates.length <= 100 
 1 <= candidates[i] <= 50 
 1 <= target <= 30 
 

 

 注意：本题与主站 40 题相同： https://leetcode-cn.com/problems/combination-sum-ii/ 
 Related Topics 数组 回溯 👍 24 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def __init__(self):
        self.res = set()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def search(nums: list, start: int, end: int, cur_list: list, cur_sum):
            if cur_sum == target:
                self.res.add(tuple(cur_list[:]))
            elif cur_sum > target:
                return
            else:
                for i in range(start, end):
                    if start < i < end and nums[i] == nums[i - 1]:  # 剪枝
                        continue
                    cur_sum += nums[i]
                    cur_list.append(nums[i])
                    search(nums, i + 1, end, cur_list, cur_sum)
                    cur_sum -= nums[i]
                    cur_list.pop()

        search(candidates, 0, len(candidates), [], 0)

        return [list(i) for i in self.res]
# leetcode submit region end(Prohibit modification and deletion)
