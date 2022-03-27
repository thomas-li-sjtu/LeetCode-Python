"""
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。 

 

 示例 1： 

 
输入：nums = [1,1,1], k = 2
输出：2
 

 示例 2： 

 
输入：nums = [1,2,3], k = 3
输出：2
 

 

 提示： 

 
 1 <= nums.length <= 2 * 10⁴ 
 -1000 <= nums[i] <= 1000 
 -10⁷ <= k <= 10⁷ 
 
 Related Topics 数组 哈希表 前缀和 👍 1389 👎 0

"""
from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 暴力解法
        # result = 0
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i, len(nums)):
        #         sum += nums[j]
        #         if sum == k:
        #             result += 1
        # return result


        # 维护一个 hashmap，hashmap 的 key 为累加值 acc，value 为累加值 acc 出现的次数
        # 迭代数组，然后不断更新 acc 和 hashmap，
        # 如果 acc 等于 k，那么很明显应该+1. 如果 hashmap[acc - k] 存在，就把它加到结果中去
        from collections import defaultdict
        presum_map = defaultdict(int)
        presum_map[0] = 1
        presum, ans = 0, 0

        for i in range(len(nums)):
            presum += nums[i]
            target = presum - k
            if target in presum_map:  # 如果前缀和减去目标值k所得到的值在字典中出现，即当前位置前缀和减去之前某一位的前缀和等于目标值
                ans += presum_map[target]
            presum_map[presum] += 1
        print(presum_map)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.subarraySum(nums = [1,2,3], k = 3))
