"""
给定两个以升序排列的整数数组 nums1 和 nums2 , 以及一个整数 k 。 

 定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2 。 

 请找到和最小的 k 个数对 (u1,v1), (u2,v2) ... (uk,vk) 。 

 

 示例 1: 

 
输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
输出: [1,2],[1,4],[1,6]
解释: 返回序列中的前 3 对数：
    [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
 

 示例 2: 

 
输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
输出: [1,1],[1,1]
解释: 返回序列中的前 2 对数：
     [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
 

 示例 3: 

 
输入: nums1 = [1,2], nums2 = [3], k = 3 
输出: [1,3],[2,3]
解释: 也可能序列中所有的数对都被返回:[1,3],[2,3]
 

 

 提示: 

 
 1 <= nums1.length, nums2.length <= 10⁴ 
 -10⁹ <= nums1[i], nums2[i] <= 10⁹ 
 nums1, nums2 均为升序排列 
 1 <= k <= 1000 
 

 

 注意：本题与主站 373 题相同：https://leetcode-cn.com/problems/find-k-pairs-with-smallest-
sums/ 
 Related Topics 数组 堆（优先队列） 👍 38 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        ans = []
        heapq.heappush(res, (nums1[0] + nums2[0], nums1[0], nums2[0], [0, 0]))

        visited = [[False for j in range(len(nums2))] for i in range(len(nums1))]
        visited[0][0] = True

        while len(ans) < k:
            _, a, b, [i, j] = heapq.heappop(res)
            ans.append([a, b])
            if i < len(nums1) - 1 and not visited[i+1][j]:
                heapq.heappush(res, (nums1[i + 1] + nums2[j], nums1[i + 1], nums2[j], [i + 1, j]))
                visited[i + 1][j] = True
            if j < len(nums2) - 1 and not visited[i][j+1]:
                heapq.heappush(res, (nums1[i] + nums2[j+1], nums1[i], nums2[j + 1], [i, j + 1]))
                visited[i][j+1] = True
            if not res:
                break
        return ans

        # 暴力
        # r = []
        # for i in nums1:
        #     for j in nums2:
        #         r.append([i, j])
        # r.sort(key=lambda x: x[0] + x[1])
        # return r[:k]

# leetcode submit region end(Prohibit modification and deletion)
