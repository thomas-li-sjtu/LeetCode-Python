"""
给你两个 非递增 的整数数组 nums1 和 nums2 ，数组下标均 从 0 开始 计数。 

 下标对 (i, j) 中 0 <= i < nums1.length 且 0 <= j < nums2.length 。如果该下标对同时满足 i <= j 且
 nums1[i] <= nums2[j] ，则称之为 有效 下标对，该下标对的 距离 为 j - i 。 

 返回所有 有效 下标对 (i, j) 中的 最大距离 。如果不存在有效下标对，返回 0 。 

 一个数组 arr ，如果每个 1 <= i < arr.length 均有 arr[i-1] >= arr[i] 成立，那么该数组是一个 非递增 数组。 

 

 示例 1： 

 
输入：nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
输出：2
解释：有效下标对是 (0,0), (2,2), (2,3), (2,4), (3,3), (3,4) 和 (4,4) 。
最大距离是 2 ，对应下标对 (2,4) 。
 

 示例 2： 

 
输入：nums1 = [2,2,2], nums2 = [10,10,1]
输出：1
解释：有效下标对是 (0,0), (0,1) 和 (1,1) 。
最大距离是 1 ，对应下标对 (0,1) 。 

 示例 3： 

 
输入：nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]
输出：2
解释：有效下标对是 (2,2), (2,3), (2,4), (3,3) 和 (3,4) 。
最大距离是 2 ，对应下标对 (2,4) 。
 

 

 提示： 

 
 1 <= nums1.length <= 10⁵ 
 1 <= nums2.length <= 10⁵ 
 1 <= nums1[i], nums2[j] <= 10⁵ 
 nums1 和 nums2 都是 非递增 数组 
 
 Related Topics 贪心 数组 双指针 二分查找 👍 32 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        i = 0
        res = 0
        for j in range(n2):
            while i < n1 and nums1[i] > nums2[j]:
                i += 1
            if i < n1:
                res = max(res, j - i)
        return res

        # # 双指针，超时
        # pointer_2 = 0
        # len_num1, len_num2 = len(nums1), len(nums2)
        # res = 0
        # for pointer_1 in range(len_num1):
        #     if pointer_2 < pointer_1:
        #         pointer_2 = pointer_1
        #     for i in range(pointer_2, len_num2):
        #         if nums2[i] >= nums1[pointer_1]:
        #             pointer_2 = i
        #     res = max(res, pointer_2-pointer_1)
        #     if pointer_2 == len_num2-1:
        #         break
        #
        # return res


        # # 二分，超时
        # pointer_1, pointer_2 = 0, 0
        # len_num1, len_num2 = len(nums1), len(nums2)
        # res = 0
        # while pointer_1 < len_num1 and pointer_2 < len_num2 and pointer_1 < len_num2:
        #     if nums1[pointer_1] > nums2[pointer_1]:
        #         pointer_1 += 1
        #     else:
        #         left, right, pos = pointer_2, len_num2-1, 0
        #         target = nums1[pointer_1]
        #         while left <= right:
        #             mid = (left+right) // 2
        #             if nums2[mid] >= target:
        #                 left += 1
        #                 pos = mid
        #             else:
        #                 right -= 1
        #         res = max(res, pos-pointer_1)
        #         pointer_1 += 1
        #         pointer_2 = pos

        return res
# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.maxDistance([55,30,5,4,2],
			[100,20,10,10,5]))
