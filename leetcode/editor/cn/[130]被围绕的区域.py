"""
给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
 
 
 

 示例 1： 

 
输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X",
"X"]]
输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被
填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
 

 示例 2： 

 
输入：board = [["X"]]
输出：[["X"]]
 

 

 提示： 

 
 m == board.length 
 n == board[i].length 
 1 <= m, n <= 200 
 board[i][j] 为 'X' 或 'O' 
 
 
 
 Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 769 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, column = len(board), len(board[0])
        dir_list = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited, stack = set(), []
        zero_pos = []

        for i in range(row):
            for j in range(column):
                if board[i][j] == 'O' and (i == 0 or i == row - 1 or j == 0 or j == column - 1):
                    zero_pos.append((i, j))
        while zero_pos:
            tmp_r, tmp_c = zero_pos.pop(0)
            visited.add((tmp_r, tmp_c))
            for bias_r, bias_c in dir_list:
                if 0 <= tmp_r + bias_r < row and 0 <= tmp_c + bias_c < column and (tmp_r + bias_r, tmp_c + bias_c) not in visited and \
                        board[tmp_r + bias_r][tmp_c + bias_c] == 'O':
                    zero_pos.append((tmp_r + bias_r, tmp_c + bias_c))
                    visited.add((tmp_r + bias_r, tmp_c + bias_c))
        for i in range(row):
            for j in range(column):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = "X"
# leetcode submit region end(Prohibit modification and deletion)
