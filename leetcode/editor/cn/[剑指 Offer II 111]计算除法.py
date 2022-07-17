"""
给定一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和 values[
i] 共同表示等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。 

 另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj = ?
 的结果作为答案。 

 返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 -1.0 替代这
个答案。 

 注意：输入总是有效的。可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。 

 

 示例 1： 

 
输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],[
"b","a"],["a","e"],["a","a"],["x","x"]]
输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
解释：
条件：a / b = 2.0, b / c = 3.0
问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]
 

 示例 2： 

 
输入：equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], 
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
输出：[3.75000,0.40000,5.00000,0.20000]
 

 示例 3： 

 
输入：equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a",
"c"],["x","y"]]
输出：[0.50000,2.00000,-1.00000,-1.00000]
 

 

 提示： 

 
 1 <= equations.length <= 20 
 equations[i].length == 2 
 1 <= Ai.length, Bi.length <= 5 
 values.length == equations.length 
 0.0 < values[i] <= 20.0 
 1 <= queries.length <= 20 
 queries[i].length == 2 
 1 <= Cj.length, Dj.length <= 5 
 Ai, Bi, Cj, Dj 由小写英文字母与数字组成 
 

 

 注意：本题与主站 399 题相同： https://leetcode-cn.com/problems/evaluate-division/ 
 Related Topics 深度优先搜索 广度优先搜索 并查集 图 数组 最短路 👍 20 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 建图
        graph = []
        for xy, val in zip(equations, values):
            graph.append((xy[0], xy[1], val))
            graph.append((xy[1], xy[0], 1 / val))

        ans = []

        for x, y in queries:
            cur_l = len(ans)
            Q = []
            visited = set()
            for i in range(len(graph)):  # 添加起点
                if graph[i][0] == x:
                    Q.append([i, graph[i][2]])
                    visited.add(i)
            while Q:  # 然后BFS
                cur_p, cur_sum = Q.pop(0)
                if graph[cur_p][1] == y:  # 出现目标时更新答案
                    ans.append(cur_sum)
                    break
                else:
                    for i in range(len(graph)):
                        if i in visited:
                            continue
                        if graph[i][0] == graph[cur_p][1]:
                            Q.append([i, cur_sum * graph[i][2]])
                            visited.add(i)
            if len(ans) == cur_l:
                ans.append(float(-1))
        return ans

# leetcode submit region end(Prohibit modification and deletion)
