"""
给定一个 排序好 的数组 arr ，两个整数 k 和 x ，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。 

 整数 a 比整数 b 更接近 x 需要满足： 

 
 |a - x| < |b - x| 或者 
 |a - x| == |b - x| 且 a < b 
 

 

 示例 1： 

 
输入：arr = [1,2,3,4,5], k = 4, x = 3
输出：[1,2,3,4]
 

 示例 2： 

 
输入：arr = [1,2,3,4,5], k = 4, x = -1
输出：[1,2,3,4]
 

 

 提示： 

 
 1 <= k <= arr.length 
 1 <= arr.length <= 10⁴ 
 arr 按 升序 排列 
 -10⁴ <= arr[i], x <= 10⁴ 
 
 Related Topics 数组 双指针 二分查找 排序 堆（优先队列） 👍 319 👎 0

"""
import bisect
import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        heapq.heapify([])
        index = bisect.bisect_left(arr, x)
        counter = 0
        left, right = index-1 if index >= 0 else 0, index
        while counter < k:
            # print(left, right)
            if left == right:
                heapq.heappush(res, arr[left])
                counter += 1
                left -= 1
                continue
            if left >= 0 and right < len(arr):
                if abs(arr[left] - x) < abs(arr[right] - x) or (abs(arr[left] - x) == abs(arr[right] - x) and arr[left] <= arr[right]):
                    heapq.heappush(res, arr[left])
                    left -= 1
                    counter += 1
                elif abs(arr[left] - x) > abs(arr[right] - x):
                    heapq.heappush(res, arr[right])
                    right += 1
                    counter += 1
                    continue
                else:
                    print("asdfadf")
                    exit()
            if left < 0 and right < len(arr):
                while counter < k:
                    heapq.heappush(res, arr[right])
                    right += 1
                    counter += 1
                break
            if right == len(arr) and left >= 0:
                while counter < k:
                    heapq.heappush(res, arr[left])
                    left -= 1
                    counter += 1
                break

        res = [heapq.heappop(res) for _ in range(k)]
        return res


# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
print(s.findClosestElements([0,0,1,2,3,3,4,7,7,8],3,5))
