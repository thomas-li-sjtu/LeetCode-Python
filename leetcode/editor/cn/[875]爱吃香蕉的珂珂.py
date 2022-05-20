"""
珂珂喜欢吃香蕉。这里有 n 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 h 小时后回来。 

 珂珂可以决定她吃香蕉的速度 k （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 k 根。如果这堆香蕉少于 k 根，她将吃掉这堆的所有香蕉，然后这一
小时内不会再吃更多的香蕉。 

 珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。 

 返回她可以在 h 小时内吃掉所有香蕉的最小速度 k（k 为整数）。 

 

 
 

 示例 1： 

 
输入：piles = [3,6,7,11], h = 8
输出：4
 

 示例 2： 

 
输入：piles = [30,11,23,4,20], h = 5
输出：30
 

 示例 3： 

 
输入：piles = [30,11,23,4,20], h = 6
输出：23
 

 

 提示： 

 
 1 <= piles.length <= 10⁴ 
 piles.length <= h <= 10⁹ 
 1 <= piles[i] <= 10⁹ 
 
 Related Topics 数组 二分查找 👍 300 👎 0

"""
from typing import List
import math


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Can Koko eat all bananas in H hours with eating speed K?
        def possible(K):
            return sum((p - 1) // K + 1 for p in piles) <= h

        lo, hi = 1, max(piles)
        while lo < hi:
            mi = (lo + hi) // 2
            if not possible(mi):
                lo = mi + 1
            else:
                hi = mi
        return int(lo)

        # # 超时
        # if len(piles) == 1:
        #     return math.ceil(piles[0] / (h+0.0))
        # piles.sort()
        # tmp_speed = piles[-1]
        # last_speed = piles[-1]
        # while 1 <= tmp_speed <= last_speed:
        #     tmp_time = [math.ceil(i/(tmp_speed+0.0)) for i in piles]
        #     time_sum = sum(tmp_time)
        #     if time_sum == h:
        #         break
        #     if time_sum < h:
        #         last_speed = tmp_speed
        #         tmp_speed = tmp_speed // 2
        #     else:
        #         tmp_speed = (last_speed + tmp_speed) // 2
        #     if abs(tmp_speed-last_speed) == 1:
        #         break
        # print(tmp_speed)
        # for speed in range(tmp_speed+1, -1, -1):
        #     tmp_time = [math.ceil(i / (speed + 0.0)) for i in piles]
        #     # print(tmp_time)
        #     time_sum = sum(tmp_time)
        #     if time_sum <= h:
        #         continue
        #     else:
        #
        #         return speed+1

# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.minEatingSpeed([332484035,524908576,855865114,632922376,222257295,690155293,112677673,679580077,337406589,290818316,877337160,901728858,679284947,688210097,692137887,718203285,629455728,941802184],23855818))
print(s.minEatingSpeed([1,1,1,999999999],10))
