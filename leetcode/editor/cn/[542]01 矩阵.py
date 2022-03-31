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
 
 Related Topics 广度优先搜索 数组 动态规划 矩阵 👍 645 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # # DFS（超时）
        # res = mat.copy()
        # row, column = len(mat), len(mat[0])
        # dir_list = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # visited = set()
        #
        # def dfs(i, j, counter, paths):
        #     visited.add((i, j))
        #     for add_r, add_c in dir_list:
        #         if 0 <= i + add_r < row and 0 <= j + add_c < column and mat[i + add_r][j + add_c] == 1 and (i + add_r, j + add_c) not in visited:
        #             counter += 1
        #             paths.append(dfs(i + add_r, j + add_c, counter, paths))
        #             counter -= 1
        #             visited.remove((i + add_r, j + add_c))
        #         elif 0 <= i + add_r < row and 0 <= j + add_c < column and mat[i + add_r][j + add_c] == 0:
        #             paths.append(counter + 1)
        #
        # for i in range(row):
        #     for j in range(column):
        #         if mat[i][j] == 0:
        #             continue
        #         paths = []
        #         dfs(i, j, 0, paths)
        #         visited = set()
        #         res[i][j] = min([i for i in paths if i])
        #
        # return res

        # # BFS+少许动态规划（超时）
        # row, column = len(mat), len(mat[0])
        # res = [[0 for _ in range(column)] for _ in range(row)]
        # dir_list = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        # for i in range(row):
        #     for j in range(column):
        #         if mat[i][j] == 0:
        #             continue
        #         flag = 0
        #         for add_r, add_c in dir_list:
        #             if 0 <= i + add_r < row and 0 <= j + add_c < column and mat[i + add_r][j + add_c] == 0:
        #                 flag, res[i][j] = 1, 1
        #                 break
        #         if flag:
        #             continue
        #
        #         visited, paths = set(), []
        #         stack = [(i, j, 1)]
        #         while stack:
        #             tmp_r, tmp_c, tmp_count = stack.pop(0)
        #             visited.add((tmp_r, tmp_c))
        #             for add_r, add_c in dir_list:
        #                 if 0 <= tmp_r + add_r < row and 0 <= tmp_c + add_c < column \
        #                         and mat[tmp_r + add_r][tmp_c + add_c] == 1 and (tmp_r + add_r, tmp_c + add_c) not in visited:
        #                     if tmp_r + add_r < i and tmp_c + add_c < j:  # 已经存储过（动态规划）
        #                         paths.append(res[tmp_r + add_r][tmp_c + add_c] + abs(tmp_r + add_r - i) + abs(tmp_c + add_c - j))
        #                     else:
        #                         visited.add((tmp_r + add_r, tmp_c + add_c))
        #                         stack.append((tmp_r + add_r, tmp_c + add_c, tmp_count + 1))
        #                 elif 0 <= tmp_r + add_r < row and 0 <= tmp_c + add_c < column \
        #                         and mat[tmp_r + add_r][tmp_c + add_c] == 0:
        #                     paths.append(tmp_count)
        #
        #         res[i][j] = min([tmp_val for tmp_val in paths if tmp_val])
        # return res

        # # 动态规划，从左上往右下看，非0点到0的最短距离；从右下到左上遍历，注意这次更新除了要取右下两个点的最短距离之外，还要跟当前位置的点做一次最小值比较
        # matrix = mat
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         l, t = 100000, 1000000
        #         if matrix[i][j] != 0:
        #             if i > 0:
        #                 t = matrix[i - 1][j]
        #
        #             if j > 0:
        #                 l = matrix[i][j - 1]
        #
        #             matrix[i][j] = min(l, t) + 1
        #
        # for i in range(len(matrix) - 1, -1, -1):
        #     for j in range(len(matrix[0]) - 1, -1, -1):
        #         r, b = 1000000, 1000000
        #         if matrix[i][j] != 0:
        #             if i < len(matrix) - 1:
        #                 b = matrix[i + 1][j]
        #
        #             if j < len(matrix[0]) - 1:
        #                 r = matrix[i][j + 1]
        #
        #             matrix[i][j] = min(matrix[i][j], min(r, b) + 1)
        # return matrix

        # # 基于0的BFS
        # import collections
        #
        # m, n = len(mat), len(mat[0])
        # dist = [[0] * n for _ in range(m)]
        # zeroes_pos = [(i, j) for i in range(m) for j in range(n) if mat[i][j] == 0]
        # que = collections.deque(zeroes_pos)
        # seen = set(zeroes_pos)
        #
        # while que:
        #     i, j = que.popleft()
        #     for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        #         if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
        #             dist[ni][nj] = dist[i][j] + 1
        #             que.append((ni, nj))
        #             seen.add((ni, nj))
        # return dist

# leetcode submit region end(Prohibit modification and deletion)

