"""
给你两个正整数数组 nums1 和 nums2 ，数组的长度都是 n 。 

 数组 nums1 和 nums2 的 绝对差值和 定义为所有 |nums1[i] - nums2[i]|（0 <= i < n）的 总和（下标从 0 开始）。
 

 你可以选用 nums1 中的 任意一个 元素来替换 nums1 中的 至多 一个元素，以 最小化 绝对差值和。 

 在替换数组 nums1 中最多一个元素 之后 ，返回最小绝对差值和。因为答案可能很大，所以需要对 10⁹ + 7 取余 后返回。 

 |x| 定义为： 

 
 如果 x >= 0 ，值为 x ，或者 
 如果 x <= 0 ，值为 -x 
 

 

 示例 1： 

 
输入：nums1 = [1,7,5], nums2 = [2,3,5]
输出：3
解释：有两种可能的最优方案：
- 将第二个元素替换为第一个元素：[1,7,5] => [1,1,5] ，或者
- 将第二个元素替换为第三个元素：[1,7,5] => [1,5,5]
两种方案的绝对差值和都是 |1-2| + (|1-3| 或者 |5-3|) + |5-5| = 3
 

 示例 2： 

 
输入：nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]
输出：0
解释：nums1 和 nums2 相等，所以不用替换元素。绝对差值和为 0
 

 示例 3： 

 
输入：nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]
输出：20
解释：将第一个元素替换为第二个元素：[1,10,4,4,2,7] => [10,10,4,4,2,7]
绝对差值和为 |10-9| + |10-3| + |4-5| + |4-1| + |2-7| + |7-4| = 20
 

 

 提示： 

 
 n == nums1.length 
 n == nums2.length 
 1 <= n <= 10⁵ 
 1 <= nums1[i], nums2[i] <= 10⁵ 
 
 Related Topics 数组 二分查找 有序集合 排序 👍 129 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        # 对于某一对 nums1[i], nums2[i] 最佳的替换方案是将 nums1[i] 替换为最接近 nums2[i] 的值
        # 查找最接近 某一个值 的数字，简单的办法是先对 nums1 排序，然后使用二分查找
        # 一般二分查找的结果是大于或等于 target 的第一个位置，还需要检查前一个位置即 小于 target 的最大值

        n = len(nums1)
        st = sorted(nums1)
        s, mx = 0, 0
        for x, y in zip(nums1, nums2):
            if x == y:
                continue
            z = abs(x - y)
            s += z
            # 二分查找最接近 y 的两个值
            left, right = 0, n - 1
            while left < right:
                mid = left + right >> 1
                if st[mid] < y:
                    left = mid + 1
                else:
                    right = mid
            mx = max(mx, z - min(abs(st[left] - y), abs(st[left - 1] - y) if left - 1 > 0 else z))
        return (s - mx) % 1000000007

# leetcode submit region end(Prohibit modification and deletion)
