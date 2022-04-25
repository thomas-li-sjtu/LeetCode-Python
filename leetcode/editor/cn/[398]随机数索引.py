"""
给你一个可能含有 重复元素 的整数数组 nums ，请你随机输出给定的目标数字 target 的索引。你可以假设给定的数字一定存在于数组中。 

 实现 Solution 类： 

 
 Solution(int[] nums) 用数组 nums 初始化对象。 
 int pick(int target) 从 nums 中选出一个满足 nums[i] == target 的随机索引 i 。如果存在多个有效的索引，则每个索
引的返回概率应当相等。 
 

 

 示例： 

 
输入
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
输出
[null, 4, 0, 2]

解释
Solution solution = new Solution([1, 2, 3, 3, 3]);
solution.pick(3); // 随机返回索引 2, 3 或者 4 之一。每个索引的返回概率应该相等。
solution.pick(1); // 返回 0 。因为只有 nums[0] 等于 1 。
solution.pick(3); // 随机返回索引 2, 3 或者 4 之一。每个索引的返回概率应该相等。
 

 

 
 
 
 提示： 

 
 1 <= nums.length <= 2 * 10⁴ 
 -2³¹ <= nums[i] <= 2³¹ - 1 
 target 是 nums 中的一个整数 
 最多调用 pick 函数 10⁴ 次 
 
 
 
 

 
 Related Topics 水塘抽样 哈希表 数学 随机化 👍 209 👎 0

"""
import random
from typing import List
import collections


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def __init__(self, nums: List[int]):
        self.num_dict = collections.defaultdict(list)
        for i, cur_num in enumerate(nums):
            self.num_dict[cur_num].append(i)

    def pick(self, target: int) -> int:
        if self.num_dict.get(target):
            rand = random.randint(0, len(self.num_dict[target])-1)
            return self.num_dict[target][rand]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# leetcode submit region end(Prohibit modification and deletion)
s = Solution([1, 2, 3, 3, 3])
print(s.pick(3))
print(s.pick(1))
print(s.pick(3))
