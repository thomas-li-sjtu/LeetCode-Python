"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。 

 

 示例 1: 

 
输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
] 

 示例 2: 

 
输入: n = 1, k = 1
输出: [[1]] 

 

 提示: 

 
 1 <= n <= 20 
 1 <= k <= n 
 

 

 注意：本题与主站 77 题相同： https://leetcode-cn.com/problems/combinations/ 
 Related Topics 数组 回溯 👍 26 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i + 1 for i in range(n)]

        def search(array, start, end, cur):
            if len(cur) == k:
                self.res.append(cur[:])
            else:
                for i in range(start, end):
                    cur.append(array[i])
                    search(array, i + 1, end, cur)
                    cur.pop()

        search(nums, 0, n, [])

        return self.res
# leetcode submit region end(Prohibit modification and deletion)
