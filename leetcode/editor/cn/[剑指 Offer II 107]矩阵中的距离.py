"""
给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。 

 两个相邻元素间的距离为 1 。 

 

 示例 1： 

 

 
输入：mat = [[0,0,0],[0,1,0],[0,0,0]]
输出：[[0,0,0],[0,1,0],[0,0,0]]
 

 示例 2： 

 

 
输入：mat = [[0,0,0],[0,1,0],[1,1,1]]
输出：[[0,0,0],[0,1,0],[1,2,1]]
 

 

 提示： 

 
 m == mat.length 
 n == mat[i].length 
 1 <= m, n <= 10⁴ 
 1 <= m * n <= 10⁴ 
 mat[i][j] is either 0 or 1. 
 mat 中至少有一个 0 
 

 

 注意：本题与主站 542 题相同：https://leetcode-cn.com/problems/01-matrix/ 
 Related Topics 广度优先搜索 数组 动态规划 矩阵 👍 27 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dist = [[0] * n for _ in range(m)]
        zeroes_pos = [(i, j) for i in range(m) for j in range(n) if mat[i][j] == 0]
        # 将所有的 0 添加进初始队列中
        q = zeroes_pos
        seen = set(zeroes_pos)

        # 广度优先搜索
        while q:
            i, j = q.pop(0)
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))
                    seen.add((ni, nj))

        return dist

# leetcode submit region end(Prohibit modification and deletion)
