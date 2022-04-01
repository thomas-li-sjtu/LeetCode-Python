"""
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。 

 你可以按 任何顺序 返回答案。 

 

 示例 1： 

 
输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
] 

 示例 2： 

 
输入：n = 1, k = 1
输出：[[1]] 

 

 提示： 

 
 1 <= n <= 20 
 1 <= k <= n 
 
 Related Topics 数组 回溯 👍 924 👎 0

"""
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 回溯算法模板框架如下
        # def backtracking(参数):
        #     if (终止条件):
        #         存放结果
        #         return
        #     for i in range(选择：本层集合中元素（树中节点孩子的数量就是集合的大小）):
        #         处理节点
        #     backtracking()
        #     回溯，撤销处理的结果

        result = []  # 存放结果
        path = []  # 存放路径

        def backtracking(n, k, startIndex):
            if k == len(path):
                result.append(path[:])
                return
            for i in range(startIndex, n + 1):
                path.append(i)
                backtracking(n, k, i + 1)
                path.pop()  # 回溯，撤销处理结果

        backtracking(n, k, 1)
        return result

# leetcode submit region end(Prohibit modification and deletion)
