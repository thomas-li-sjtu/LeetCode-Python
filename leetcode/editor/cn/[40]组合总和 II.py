"""
给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。 

 candidates 中的每个数字在每个组合中只能使用 一次 。 

 注意：解集不能包含重复的组合。 

 

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
 
 Related Topics 数组 回溯 👍 916 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)  # 剪枝
        path = []

        def cal(start, count):
            if count == target:
                res.append(path[:])
            if count > target:
                return
            else:
                for i in range(start, len(candidates)):
                    if i > start and candidates[i - 1] == candidates[i]:  # 剪枝
                        continue
                    path.append(candidates[i])
                    cal(i + 1, count + candidates[i])
                    path.pop()
        cal(0, 0)
        return res

# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.combinationSum2([1,1,2,5,6,7,10], 8))
