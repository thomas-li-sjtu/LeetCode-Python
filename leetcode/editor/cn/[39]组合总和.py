"""
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所
有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。 

 candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 

 对于给定的输入，保证和为 target 的不同组合数少于 150 个。 

 

 示例 1： 

 
输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。 

 示例 2： 

 
输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]] 

 示例 3： 

 
输入: candidates = [2], target = 1
输出: []
 

 

 提示： 

 
 1 <= candidates.length <= 30 
 1 <= candidates[i] <= 200 
 candidate 中的每个元素都 互不相同 
 1 <= target <= 500 
 
 Related Topics 数组 回溯 👍 1888 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 超时
        # rest = target
        # res = set()
        # path = []
        #
        # def combine(rest):
        #     if rest == 0:
        #         res.add(tuple(sorted(path[:])))
        #     elif rest < 0:
        #         return
        #     else:
        #         for i in range(0, len(candidates)):
        #             path.append(candidates[i])
        #             combine(rest - candidates[i])
        #             path.pop()
        #
        # combine(rest)
        # return [list(i) for i in res]

        res, track = list(), list()

        def backtrack(candidates, start, trackSum, target):
            # 结束条件
            if trackSum == target:
                res.append(track[:])  # ！！！此处有坑需要注意
                return
            if trackSum > target:
                return
            for i in range(start, len(candidates)):
                track.append(candidates[i])
                trackSum += candidates[i]
                backtrack(candidates, i, trackSum, target)  # 重复使用元素任意次 令start==i
                track.pop()
                trackSum -= candidates[i]

        backtrack(candidates, 0, 0, target)
        return res

    # 回溯模板
    # result = []
    #
    # def backtrack(选择列表, 路径):
    #     if 满足结束条件:
    #         result.add(路径)
    #         return
    #
    #     for 选择 in 选择列表:
    #         # 做选择
    #         路径.add(选择)
    #         将该选择从选择列表移除
    #         backtrack(选择列表, 路径)  # 核心 递归调用之前【做选择】，调用之后【撤销选择】
    #         # 撤销选择
    #         路径.remove(选择)
    #         将该选择再加入选择列表


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.combinationSum(candidates=[2, 3, 5], target=8))
