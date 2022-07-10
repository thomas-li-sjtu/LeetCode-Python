"""
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。 

 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。 

 

 示例 1: 

 
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
 

 示例 2: 

 
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4 

 

 提示： 

 
 1 <= k <= nums.length <= 10⁴ 
 -10⁴ <= nums[i] <= 10⁴ 
 

 

 注意：本题与主站 215 题相同： https://leetcode-cn.com/problems/kth-largest-element-in-an-
array/ 
 Related Topics 数组 分治 快速选择 排序 堆（优先队列） 👍 38 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for x in nums:
            heapq.heappush(maxHeap, -x)
        for _ in range(k - 1):
            heapq.heappop(maxHeap)
        return -maxHeap[0]

# leetcode submit region end(Prohibit modification and deletion)
