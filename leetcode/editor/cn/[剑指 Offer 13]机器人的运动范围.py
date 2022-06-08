"""
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（
不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不
能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？ 

 

 示例 1： 

 输入：m = 2, n = 3, k = 1
输出：3
 

 示例 2： 

 输入：m = 3, n = 1, k = 0
输出：1
 

 提示： 

 
 1 <= n,m <= 100 
 0 <= k <= 20 
 
 Related Topics 深度优先搜索 广度优先搜索 动态规划 👍 512 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = set()
        stack = [(0, 0)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while stack:
            tmp_location = stack.pop(0)
            visited.add(tmp_location)
            for add_r, add_c in directions:
                new_r, new_c = tmp_location[0] + add_r, tmp_location[1] + add_c
                if 0 <= new_r < m and 0 <= new_c < n and (new_r, new_c) not in visited:
                    cur_sum, cur_r, cur_c = 0, new_r, new_c
                    while cur_r > 0:
                        cur_sum += cur_r % 10
                        cur_r //= 10
                    while cur_c > 0:
                        cur_sum += cur_c % 10
                        cur_c //= 10
                    if cur_sum <= k:
                        stack.append((new_r, new_c))
                        visited.add((new_r, new_c))
        return len(visited)

# leetcode submit region end(Prohibit modification and deletion)
