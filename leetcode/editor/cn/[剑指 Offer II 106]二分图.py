"""
存在一个 无向图 ，图中有 n 个节点。其中每个节点都有一个介于 0 到 n - 1 之间的唯一编号。 

 给定一个二维数组 graph ，表示图，其中 graph[u] 是一个节点数组，由节点 u 的邻接节点组成。形式上，对于 graph[u] 中的每个 v ，都
存在一条位于节点 u 和节点 v 之间的无向边。该无向图同时具有以下属性： 

 
 不存在自环（graph[u] 不包含 u）。 
 不存在平行边（graph[u] 不包含重复值）。 
 如果 v 在 graph[u] 内，那么 u 也应该在 graph[v] 内（该图是无向图） 
 这个图可能不是连通图，也就是说两个节点 u 和 v 之间可能不存在一条连通彼此的路径。 
 

 二分图 定义：如果能将一个图的节点集合分割成两个独立的子集 A 和 B ，并使图中的每一条边的两个节点一个来自 A 集合，一个来自 B 集合，就将这个图称为 
二分图 。 

 如果图是二分图，返回 true ；否则，返回 false 。 

 

 示例 1： 

 

 
输入：graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
输出：false
解释：不能将节点分割成两个独立的子集，以使每条边都连通一个子集中的一个节点与另一个子集中的一个节点。 

 示例 2： 

 

 
输入：graph = [[1,3],[0,2],[1,3],[0,2]]
输出：true
解释：可以将节点分成两组: {0, 2} 和 {1, 3} 。 

 

 提示： 

 
 graph.length == n 
 1 <= n <= 100 
 0 <= graph[u].length < n 
 0 <= graph[u][i] <= n - 1 
 graph[u] 不会包含 u 
 graph[u] 的所有值 互不相同 
 如果 graph[u] 包含 v，那么 graph[v] 也会包含 u 
 

 

 注意：本题与主站 785 题相同： https://leetcode-cn.com/problems/is-graph-bipartite/ 
 Related Topics 深度优先搜索 广度优先搜索 并查集 图 👍 23 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # 任选一个节点开始，给它染成红色。随后我们对整个图进行遍历，将该节点直接相连的所有节点染成绿色，
        # 表示这些节点不能与起始节点属于同一个集合。我们再将这些绿色节点直接相连的所有节点染成红色，以此类推，直到无向图中的每个节点均被染色

        n = len(graph)
        UNCOLORED, RED, GREEN = 0, 1, 2
        color = [UNCOLORED] * n

        for i in range(n):
            if color[i] == UNCOLORED:
                q = [i]
                color[i] = RED
                while q:
                    node = q.pop(0)
                    cNei = GREEN if color[node] == RED else RED
                    for neighbor in graph[node]:
                        if color[neighbor] == UNCOLORED:
                            q.append(neighbor)
                            color[neighbor] = cNei
                        elif color[neighbor] != cNei:
                            return False

        return True

# leetcode submit region end(Prohibit modification and deletion)
