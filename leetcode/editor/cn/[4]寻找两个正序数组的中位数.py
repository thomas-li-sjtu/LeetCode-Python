# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
#  
# 
#  示例 2： 
# 
#  
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
#  
# 
#  示例 3： 
# 
#  
# 输入：nums1 = [0,0], nums2 = [0,0]
# 输出：0.00000
#  
# 
#  示例 4： 
# 
#  
# 输入：nums1 = [], nums2 = [1]
# 输出：1.00000
#  
# 
#  示例 5： 
# 
#  
# 输入：nums1 = [2], nums2 = []
# 输出：2.00000
#  
# 
#  
# 
#  提示： 
# 
#  
#  nums1.length == m 
#  nums2.length == n 
#  0 <= m <= 1000 
#  0 <= n <= 1000 
#  1 <= m + n <= 2000 
#  -106 <= nums1[i], nums2[i] <= 106 
#  
# 
#  
# 
#  进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？ 
#  Related Topics 数组 二分查找 分治算法 
#  👍 4021 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        n1, n2 = len(nums1), len(nums2)

        def get_kth_element(k: int) -> int:
            i1, i2 = 0, 0
            while k != 0:
                if i1 == n1:
                    return nums2[i2 + k - 1]
                if i2 == n2:
                    return nums1[i1 + k - 1]
                if k == 1:  # 1//2 = 0 所有也要判断一下
                    return min(nums1[i1], nums2[i2])

                new_i1 = min(i1 + k // 2 - 1, n1 - 1)  # 每个数组贡献 k//2
                new_i2 = min(i2 + k // 2 - 1, n2 - 1)
                pivot_1, pivot_2 = nums1[new_i1], nums2[new_i2]
                if pivot_1 <= pivot_2:  # 把小的那段扔掉
                    k -= (new_i1 - i1 + 1)  # 做好index的更新
                    i1 = new_i1 + 1
                else:
                    k -= (new_i2 - i2 + 1)
                    i2 = new_i2 + 1

        n = n1 + n2
        if n % 2 == 1:
            return get_kth_element((n + 1) // 2)  # 0 1 2 3 4  n=5 取第3个
        else:
            return (get_kth_element(n // 2) + get_kth_element((n + 2) // 2)) / 2.0

        # 暴力破解
        # nums1.extend(nums2)
        # nums1.sort()
        # n = len(nums1)
        # k = int(n / 2)
        # if n % 2 == 0:
        #     temp = (nums1[k - 1] + nums1[k]) / 2.0
        # else:
        #     temp = nums1[k]
        # return temp
# leetcode submit region end(Prohibit modification and deletion)
