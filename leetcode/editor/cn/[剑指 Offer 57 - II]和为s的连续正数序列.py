"""
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。 

 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。 

 

 示例 1： 

 输入：target = 9
输出：[[2,3,4],[4,5]]
 

 示例 2： 

 输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
 

 

 限制： 

 
 1 <= target <= 10^5 
 

 
 Related Topics 数学 双指针 枚举 👍 446 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # 滑动窗口暴力算
        res = []
        for i in range(1, target//2+1):
            cur = i
            tmp_res = [cur]
            cur_sum = cur
            while cur_sum < target:
                cur += 1
                tmp_res.append(cur)
                cur_sum += cur
            if cur_sum == target:
                res.append(tmp_res)
        return res
# leetcode submit region end(Prohibit modification and deletion)
