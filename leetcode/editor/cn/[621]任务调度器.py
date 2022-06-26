"""
给你一个用字符数组 tasks 表示的 CPU 需要执行的任务列表。其中每个字母表示一种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位
时间内执行完。在任何一个单位时间，CPU 可以完成一个任务，或者处于待命状态。 

 然而，两个 相同种类 的任务之间必须有长度为整数 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。 

 你需要计算完成所有任务所需要的 最短时间 。 

 

 示例 1： 

 
输入：tasks = ["A","A","A","B","B","B"], n = 2
输出：8
解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B
     在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间，而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。 

 示例 2： 

 
输入：tasks = ["A","A","A","B","B","B"], n = 0
输出：6
解释：在这种情况下，任何大小为 6 的排列都可以满足要求，因为 n = 0
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
诸如此类
 

 示例 3： 

 
输入：tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
输出：16
解释：一种可能的解决方案是：
     A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> (待命) -> (待命) -> A -> (待命)
 -> (待命) -> A
 

 

 提示： 

 
 1 <= task.length <= 10⁴ 
 tasks[i] 是大写英文字母 
 n 的取值范围为 [0, 100] 
 
 Related Topics 贪心 数组 哈希表 计数 排序 堆（优先队列） 👍 932 👎 0

"""
from typing import List
import heapq


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_dict = {}
        for i in tasks:
            if task_dict.get(i):
                task_dict[i] += 1
            else:
                task_dict[i] = 1
        task_list = [(-value, key) for key, value in task_dict.items()]  # 记录剩余的任务数
        task_dict = {key: 0 for key, value in task_dict.items()}  # 记录未完成的任务，上一次实行的时间点
        heapq.heapify(task_list)

        counter = 0
        while task_list:
            cur_ready = set()  # 检查有没有可以本轮执行的任务
            for key, value in task_dict.items():
                if value == 0 or value + n <= counter:
                    cur_ready.add(key)

            if len(cur_ready) == 0:  # 没有本轮执行的任务，跳过
                counter += 1
                continue
            else:
                # 取出本轮执行的任务
                task_cache = []
                while True:
                    cur_task = heapq.heappop(task_list)
                    if cur_task[1] in cur_ready:
                        break
                    else:
                        task_cache.append(cur_task)
                if task_cache:
                    for task in task_cache:
                        heapq.heappush(task_list, task)

                cur_task = (cur_task[0]+1, cur_task[1])
                counter += 1
                if cur_task[0] >= 0:
                    del task_dict[cur_task[1]]
                    continue
                else:
                    task_dict[cur_task[1]] = counter
                    heapq.heappush(task_list, cur_task)

        return counter
# leetcode submit region end(Prohibit modification and deletion)
