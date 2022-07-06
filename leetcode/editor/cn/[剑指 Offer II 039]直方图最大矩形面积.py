"""
给定非负整数数组 heights ，数组中的数字用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。 

 求在该柱状图中，能够勾勒出来的矩形的最大面积。 

 

 示例 1: 

 

 
输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10
 

 示例 2： 

 

 
输入： heights = [2,4]
输出： 4 

 

 提示： 

 
 1 <= heights.length <=10⁵ 
 0 <= heights[i] <= 10⁴ 
 

 

 注意：本题与主站 84 题相同： https://leetcode-cn.com/problems/largest-rectangle-in-
histogram/ 
 Related Topics 栈 数组 单调栈 👍 50 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # # 双指针
        # max_area = 0
        # n = len(heights)
        # for i in range(n):
        #     left = i - 1
        #     right = i + 1
        #     if n * heights[i] > max_area:  # 剪枝
        #         while left >= 0 and heights[left] >= heights[i]:
        #             left -= 1
        #         while right <= n - 1 and heights[right] >= heights[i]:
        #             right += 1
        #         max_area = max(max_area, (right - left - 1) * heights[i])
        # return max_area

        # 找到每个柱形条左边和右边最近的比自己低的矩形条，用宽度乘上当前柱形条的高度作为备选答案
        # 用 left 数组维护左边界值，right 数组维护右边界值，分别存储小于当前值的最大的元素
        h = heights
        stk = []
        n = len(h)
        left = [0 for i in range(n)]
        right = [0 for i in range(n)]

        for i in range(n):
            while len(stk) > 0 and h[stk[-1]] >= h[i]:
                stk.pop()
            if len(stk) == 0:
                left[i] = 0
            else:
                left[i] = stk[-1] + 1
            stk.append(i)

        stk = []
        for i in range(n - 1, -1, -1):
            while len(stk) > 0 and h[stk[-1]] >= h[i]:
                stk.pop()
            if len(stk) == 0:
                right[i] = n + 1
            else:
                right[i] = stk[-1] + 1
            stk.append(i)

        ans = -2 ** 31
        for i in range(n):
            ans = max(ans, h[i] * (right[i] - left[i] - 1))

        return ans

# leetcode submit region end(Prohibit modification and deletion)
