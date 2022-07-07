"""
给定一个整数数组 nums 和一个整数 k ，请返回其中出现频率前 k 高的元素。可以按 任意顺序 返回答案。 

 

 示例 1: 

 
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
 

 示例 2: 

 
输入: nums = [1], k = 1
输出: [1] 

 

 提示： 

 
 1 <= nums.length <= 10⁵ 
 k 的取值范围是 [1, 数组中不相同的元素的个数] 
 题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的 
 

 

 进阶：所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。 

 

 注意：本题与主站 347 题相同：https://leetcode-cn.com/problems/top-k-frequent-elements/ 
 Related Topics 数组 哈希表 分治 桶排序 计数 快速选择 排序 堆（优先队列） 👍 31 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        bucket = [0.5] * (len(nums) + 1)
        num_dict = defaultdict(int)
        for i in nums:
            num_dict[i] += 1

        for key, value in num_dict.items():
            if bucket[value] != 0.5:
                if isinstance(bucket[value], int):
                    bucket[value] = [bucket[value], key]
                else:
                    bucket[value].append(key)
            else:
                bucket[value] = key

        counter = 0
        for i in range(len(nums), -1, -1):
            if bucket[i] == 0.5:
                continue
            else:
                if isinstance(bucket[i], int):
                    res.append(bucket[i])
                    counter += 1
                else:
                    res += bucket[i]
                    counter += len(bucket[i])
            if counter >= k:
                break
        return res

# leetcode submit region end(Prohibit modification and deletion)
