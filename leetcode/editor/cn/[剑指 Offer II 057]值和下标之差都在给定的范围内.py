"""
给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j]) <= t 
，同时又满足 abs(i - j) <= k 。 

 如果存在则返回 true，不存在返回 false。 

 

 示例 1： 

 
输入：nums = [1,2,3,1], k = 3, t = 0
输出：true 

 示例 2： 

 
输入：nums = [1,0,1,1], k = 1, t = 2
输出：true 

 示例 3： 

 
输入：nums = [1,5,9,1,5,9], k = 2, t = 3
输出：false 

 

 提示： 

 
 0 <= nums.length <= 2 * 10⁴ 
 -2³¹ <= nums[i] <= 2³¹ - 1 
 0 <= k <= 10⁴ 
 0 <= t <= 2³¹ - 1 
 

 

 注意：本题与主站 220 题相同： https://leetcode-cn.com/problems/contains-duplicate-iii/ 
 Related Topics 数组 桶排序 有序集合 排序 滑动窗口 👍 45 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
from typing import List


class Solution:
    # 以t为距离来分割，让不同元素落入不同桶
    # 计算桶序号方式：idx = x / t
    # 注意边界问题，在（-t, t）这个区间的数都会落在0这个序号，所以落在该桶里的数也需要继续对比，不能直接输出true。
    # 桶的实现，可以使用defaultdict，这里需要注意的是（-t, t）这个区间，所以用defaultdict(list)

    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        def getId(x):  # 以t为距离来分割，让不同元素落入不同桶
            """
            x:  输入的数字，int
            idx:  对应桶编号
            """
            if t == 0:
                idx = int(x / (t + 1))
            else:
                idx = int(x / t)
            return idx

        # 在遍历的过程中，使用桶来存储每个数字
        bucket = defaultdict(list)
        for i in range(len(nums)):
            idx = getId(nums[i])
            if idx in bucket:  # 在同一个桶里面，而桶元素的大小相差为t
                for j in bucket[idx]:
                    if abs(j - nums[i]) <= t:
                        return True

            # 查找左右两个桶是否存在
            if idx - 1 in bucket:
                for j in bucket[idx - 1]:
                    if abs(j - nums[i]) <= t:
                        return True
            if idx + 1 in bucket:
                for j in bucket[idx + 1]:
                    if abs(j - nums[i]) <= t:
                        return True

            bucket[idx].append(nums[i])
            # 去除k距离之前的数字
            if i >= k:
                rm_idx = getId(nums[i - k])
                bucket[rm_idx].remove(nums[i - k])
        return False

# leetcode submit region end(Prohibit modification and deletion)
