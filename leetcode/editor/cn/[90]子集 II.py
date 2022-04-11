"""
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。 

 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。 

 
 
 

 示例 1： 

 
输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
 

 示例 2： 

 
输入：nums = [0]
输出：[[],[0]]
 

 

 提示： 

 
 1 <= nums.length <= 10 
 -10 <= nums[i] <= 10 
 
 
 
 Related Topics 位运算 数组 回溯 👍 793 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)

        result = []  # 存放结果
        path = []  # 存放路径

        def backtracking(length, k, startIndex):
            if k == len(path):
                result.append(path[:])
                return
            for i in range(startIndex, length+1):
                path.append(i)
                backtracking(length, k, i + 1)
                path.pop()  # 回溯，撤销处理结果
        for k in range(length+1):
            backtracking(length, k, 1)

        res_set = set()
        for i in range(len(result)):
            result[i].sort()
            for j in range(len(result[i])):
                result[i][j] = nums[result[i][j]-1]
            res_set.add(tuple(sorted(result[i])))

        return [list(i) for i in res_set]

# leetcode submit region end(Prohibit modification and deletion)
