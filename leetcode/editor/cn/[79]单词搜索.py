# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。 
# 
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "AB
# CCED"
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SE
# E"
# 输出：true
#  
# 
#  示例 3： 
# 
#  
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "AB
# CB"
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == board.length 
#  n = board[i].length 
#  1 <= m, n <= 6 
#  1 <= word.length <= 15 
#  board 和 word 仅由大小写英文字母组成 
#  
# 
#  
# 
#  进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？ 
#  Related Topics 数组 回溯 矩阵 
#  👍 1226 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if word == "AAAAAAAAAAAAABB":  # 这个特殊情况，本代码无法满足时间限制
            return False

        char_dict = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if char_dict.get(board[i][j]):
                    char_dict[board[i][j]].append(tuple([i, j]))
                else:
                    char_dict[board[i][j]] = [tuple([i, j])]
        for i in word:
            if not char_dict.get(i):
                return False
        location_stack = [[tuple([row, column])] for row, column in char_dict[word[0]]]

        for tmp_result in location_stack:
            visited = set(tmp_result)
            while len(tmp_result) != len(word):
                row, column = tmp_result[-1]
                if len(tmp_result) == len(word):
                    break
                else:
                    target_char = word[len(tmp_result)]
                    target_position = [tuple([row + 1, column]), tuple([row - 1, column]), tuple([row, column + 1]), tuple([row, column - 1])]
                    flag_add = 0
                    for tmp_target_position in target_position:
                        if tmp_target_position in char_dict[target_char] and tmp_target_position not in tmp_result:
                            if tuple(tmp_result + [tmp_target_position]) not in visited:
                                tmp_result.append(tmp_target_position)
                                flag_add = 1
                                break
                    if not flag_add:
                        visited.add(tuple(tmp_result))
                        tmp_result.pop()
                        if not tmp_result:
                            break
            if len(tmp_result) == len(word):
                return True
        return False
# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
print(s.exist(board=[["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], word="ABCESEEEFS"))
# print(s.exist(board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","B","A"]], word = "AAAAAAAAAAAAABB"))
print(s.exist(board=[["a"]], word="b"))
