"""
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。 

 

 示例: 

 输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。 

 说明: 

 
 1 是丑数。 
 n 不超过1690。 
 

 注意：本题与主站 264 题相同：https://leetcode-cn.com/problems/ugly-number-ii/ 
 Related Topics 哈希表 数学 动态规划 堆（优先队列） 👍 349 👎 0

"""
import heapq

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 自己写出，另外动态递归的方法见leetcode 264
        stack_2 = [2]
        heapq.heapify(stack_2)
        stack_3 = [3]
        heapq.heapify(stack_3)
        stack_5 = [5]
        heapq.heapify(stack_5)
        dp = [1]
        for i in range(1, n):
            cur_2 = heapq.heappop(stack_2)
            while cur_2 <= dp[-1]:
                cur_2 = heapq.heappop(stack_2)
            cur_3 = heapq.heappop(stack_3)
            while cur_3 <= dp[-1]:
                cur_3 = heapq.heappop(stack_3)
            cur_5 = heapq.heappop(stack_5)
            while cur_5 <= dp[-1]:
                cur_5 = heapq.heappop(stack_5)
            min_cur = min(cur_5, cur_3, cur_2)
            if min_cur == cur_2:
                heapq.heappush(stack_2, min_cur*2)
                heapq.heappush(stack_3, cur_3)
                heapq.heappush(stack_3, min_cur*3)
                heapq.heappush(stack_5, cur_5)
                heapq.heappush(stack_5, min_cur*5)
            if min_cur == cur_3:
                heapq.heappush(stack_3, min_cur*3)
                heapq.heappush(stack_2, cur_2)
                heapq.heappush(stack_2, min_cur * 2)
                heapq.heappush(stack_5, cur_5)
                heapq.heappush(stack_5, min_cur*5)
            if min_cur == cur_5:
                heapq.heappush(stack_3, cur_3)
                heapq.heappush(stack_3, min_cur*3)
                heapq.heappush(stack_2, cur_2)
                heapq.heappush(stack_2, min_cur * 2)
                heapq.heappush(stack_5, min_cur*5)
            dp.append(min_cur)
        return dp[-1]


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.nthUglyNumber(11))
