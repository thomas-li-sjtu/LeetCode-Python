"""
给你三个正整数 n、index 和 maxSum 。你需要构造一个同时满足下述所有条件的数组 nums（下标 从 0 开始 计数）： 

 
 nums.length == n 
 nums[i] 是 正整数 ，其中 0 <= i < n 
 abs(nums[i] - nums[i+1]) <= 1 ，其中 0 <= i < n-1 
 nums 中所有元素之和不超过 maxSum 
 nums[index] 的值被 最大化 
 

 返回你所构造的数组中的 nums[index] 。 

 注意：abs(x) 等于 x 的前提是 x >= 0 ；否则，abs(x) 等于 -x 。 

 

 示例 1： 

 输入：n = 4, index = 2,  maxSum = 6
输出：2
解释：数组 [1,1,2,1] 和 [1,2,2,1] 满足所有条件。不存在其他在指定下标处具有更大值的有效数组。
 

 示例 2： 

 输入：n = 6, index = 1,  maxSum = 10
输出：3
 

 

 提示： 

 
 1 <= n <= maxSum <= 10⁹ 
 0 <= index < n 
 
 Related Topics 贪心 二分查找 👍 37 👎 0

"""
import math

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        # 如果采取模拟，数组会类似山型，index处最高，两侧递减
        # 参考https://leetcode.cn/problems/maximum-value-at-a-given-index-in-a-bounded-array/solution/shu-xue-gong-shi-tui-dao-zhi-jie-qiu-jie-ja54/
        def cal(a, b, c):
            # 一元二次方程求解
            return ((-b) + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

        left, right = index, n - index - 1
        min_side, max_side = sorted((left, right))
        # 第一阶段：双向扩张 -> ((1) + (1 + 2 * min_side)) * (1 + min_side) / 2
        s1 = n + (1 + min_side) ** 2
        if s1 >= maxSum:
            return 1 + int(math.sqrt(maxSum - n))
        # 第二阶段：单向扩张 -> ((1 + 2 * min_side + 1) + (1 + min_side + max_side)) * (max_side - min_side) / 2
        s2 = (3 + 3 * min_side + max_side) * (max_side - min_side) // 2
        if s1 + s2 >= maxSum:
            return 2 + int(cal(0.5, min_side + 1.5, -1.5 * min_side - 1.5 * min_side * min_side - maxSum + s1))
        # 第三阶段：扩张终止
        return 2 + max_side + (maxSum - s1 - s2) // n

# leetcode submit region end(Prohibit modification and deletion)
