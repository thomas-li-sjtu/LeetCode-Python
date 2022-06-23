"""
给你一个整数数组 nums ，按要求返回一个新数组 counts 。数组 counts 有该性质： counts[i] 的值是 nums[i] 右侧小于 
nums[i] 的元素的数量。 

 

 示例 1： 

 
输入：nums = [5,2,6,1]
输出：[2,1,1,0] 
解释：
5 的右侧有 2 个更小的元素 (2 和 1)
2 的右侧仅有 1 个更小的元素 (1)
6 的右侧有 1 个更小的元素 (1)
1 的右侧有 0 个更小的元素
 

 示例 2： 

 
输入：nums = [-1]
输出：[0]
 

 示例 3： 

 
输入：nums = [-1,-1]
输出：[0,0]
 

 

 提示： 

 
 1 <= nums.length <= 10⁵ 
 -10⁴ <= nums[i] <= 10⁴ 
 
 Related Topics 树状数组 线段树 数组 二分查找 分治 有序集合 归并排序 👍 834 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # 维护一个有序数组sl，从右往左依次往里添加nums的元素，每次添加nums[i]前，通过二分查找判断当前sl中比nums[i]小的元素
        # 这个就是nums[i]右侧比nums[i]还要小的元素个数
        n = len(nums)
        res = [0] * n
        sl = []  # 有序数组

        def bisect_left(arr, x, low, high):
            left, right = low, high
            while left < right:
                mid = (left + right) // 2
                if arr[mid] < x:
                    left = mid + 1
                else:
                    right = mid
            # arr.insert(left, x)
            return left

        for i in range(n - 1, -1, -1):  # 反向遍历
            # pos = bisect.bisect_left(sl, nums[i])           # 找到右边比当前值小的元素个数
            pos = bisect_left(sl, nums[i], 0, len(sl))  # 找到右边比当前值小的元素个数
            res[i] = pos  # 记入答案
            sl.insert(pos, nums[i])  # 将当前值加入有序数组中

        return res

# leetcode submit region end(Prohibit modification and deletion)
