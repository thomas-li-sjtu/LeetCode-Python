"""
你有 n 个工作和 m 个工人。给定三个数组： difficulty, profit 和 worker ，其中: 

 
 difficulty[i] 表示第 i 个工作的难度，profit[i] 表示第 i 个工作的收益。 
 worker[i] 是第 i 个工人的能力，即该工人只能完成难度小于等于 worker[i] 的工作。 
 

 每个工人 最多 只能安排 一个 工作，但是一个工作可以 完成多次 。 

 
 举个例子，如果 3 个工人都尝试完成一份报酬为 $1 的同样工作，那么总收益为 $3 。如果一个工人不能完成任何工作，他的收益为 $0 。 
 

 返回 在把工人分配到工作岗位后，我们所能获得的最大利润 。 

 

 示例 1： 

 
输入: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
输出: 100 
解释: 工人被分配的工作难度是 [4,4,6,6] ，分别获得 [20,20,30,30] 的收益。 

 示例 2: 

 
输入: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
输出: 0 

 

 提示: 

 
 n == difficulty.length 
 n == profit.length 
 m == worker.length 
 1 <= n, m <= 10⁴ 
 1 <= difficulty[i], profit[i], worker[i] <= 10⁵ 
 
 Related Topics 贪心 数组 双指针 二分查找 排序 👍 85 👎 0

"""
from typing import List
import bisect


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        length = len(difficulty)
        dif_tuple = [(i, j) for i, j in zip(difficulty, profit)]
        dif_tuple = sorted(dif_tuple)
        difficulty, profit = [x[0] for x in dif_tuple], [x[1] for x in dif_tuple]
        tmp_max = -1
        for i in range(len(profit)):
            if tmp_max < profit[i]:
                tmp_max = profit[i]
            else:
                profit[i] = tmp_max

        # print(difficulty)
        # print(profit)
        res = []
        for i in worker:
            index = bisect.bisect_right(difficulty, i)
            if index == length:
                res.append(profit[-1])
                continue
            if difficulty[index] == i:
                res.append(profit[index])
            else:
                if index == 0:
                    continue
                else:
                    res.append(profit[index - 1])

        return sum(res)


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.maxProfitAssignment(difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]))
print(s.maxProfitAssignment([23, 30, 35, 35, 43, 46, 47, 81, 83, 98],
                            [8, 11, 11, 20, 33, 37, 60, 72, 87, 95],
                            [95, 46, 47, 97, 11, 35, 99, 56, 41, 92]))
