# 根据 百度百科 ， 生命游戏 ，简称为 生命 ，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。 
# 
#  给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态： 1 即为 活细胞 （live），或 0 即为 死细胞
#  （dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律： 
# 
#  
#  如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡； 
#  如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活； 
#  如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡； 
#  如果死细胞周围正好有三个活细胞，则该位置死细胞复活； 
#  
# 
#  下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。给你 m x n 网格面板 board 的当前状态，返
# 回下一个状态。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# 输出：[[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
#  
# 
#  示例 2： 
# 
#  
# 输入：board = [[1,1],[1,0]]
# 输出：[[1,1],[1,1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == board.length 
#  n == board[i].length 
#  1 <= m, n <= 25 
#  board[i][j] 为 0 或 1 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  你可以使用原地算法解决本题吗？请注意，面板上所有格子需要同时被更新：你不能先更新某些格子，然后使用它们的更新后的值再更新其他格子。 
#  本题中，我们使用二维数组来表示面板。原则上，面板是无限的，但当活细胞侵占了面板边界时会造成问题。你将如何解决这些问题？ 
#  
#  Related Topics 数组 矩阵 模拟 
#  👍 412 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        import copy
        new_board = copy.deepcopy(board)
        m = len(new_board)
        n = len(new_board[0])

        for i in range(m):
            for j in range(n):
                if self.is_alive(board=board, i=i, j=j):
                    new_board[i][j] = 1
                else:
                    new_board[i][j] = 0
        for i in range(m):
            for j in range(n):
                board[i][j] = new_board[i][j]

    def is_alive(self, board, i, j):
        m = len(board)
        n = len(board[0])
        origin = board[i][j]
        counter_alive, counter_dead = 0, 0
        for row, column in [(i-1, j-1), (i-1, j), (i-1,j+1),
                            (i, j-1), (i, j+1),
                            (i+1, j-1), (i+1, j), (i+1, j+1)]:
            if 0 <= row < m and 0 <= column < n:
                if board[row][column] == 1:
                    counter_alive += 1
                else:
                    counter_dead += 1
        if origin == 1 and counter_alive < 2:
            return False
        elif origin == 1 and (counter_alive == 3 or counter_alive == 2):
            return True
        elif origin == 1 and counter_alive > 3:
            return False
        elif origin == 0 and counter_alive == 3:
            return True
        else:
            return False
# leetcode submit region end(Prohibit modification and deletion)
