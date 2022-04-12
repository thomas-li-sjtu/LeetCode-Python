"""
给定一个未排序的整数数组 nums ， 返回最长递增子序列的个数 。 

 注意 这个数列必须是 严格 递增的。 

 

 示例 1: 

 
输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
 

 示例 2: 

 
输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
 

 

 提示: 

 

 
 1 <= nums.length <= 2000 
 -10⁶ <= nums[i] <= 10⁶ 
 
 Related Topics 树状数组 线段树 数组 动态规划 👍 587 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        res = [1]*len(nums)
        cnt = [1]*len(nums)  # cnt[i]: 以nums[i]结尾的上升子序列的个数
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if res[j] + 1 > res[i]:
                        res[i] = res[j] + 1
                        cnt[i] = cnt[j]  # 重置计数
                    elif res[j] + 1 == res[i]:
                        cnt[i] += cnt[j]

        max_len = max(res)
        out = 0
        for i in range(len(res)):
            if res[i] == max_len:
                max_len = res[i]
                out += cnt[i]

        return out


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.findNumberOfLIS([1,3,5,4,7]))
