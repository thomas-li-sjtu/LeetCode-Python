# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, 
# ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。 
# 
#  说明：你不能倾斜容器。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49 
# 解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。 
# 
#  示例 2： 
# 
#  
# 输入：height = [1,1]
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：height = [4,3,2,1,4]
# 输出：16
#  
# 
#  示例 4： 
# 
#  
# 输入：height = [1,2,1]
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == height.length 
#  2 <= n <= 105 
#  0 <= height[i] <= 104 
#  
#  Related Topics 贪心 数组 双指针 
#  👍 3100 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 在初始时，左右指针分别指向数组的左右两端，它们可以容纳的水量为 min(1, 7) * 8 = 8
        #
        # 此时需要移动一个指针。移动哪一个呢？直觉告诉我们，应该移动对应数字较小的那个指针

        left, right = 0, len(height)-1
        most = -1
        while left < right:
            most = max((right-left)*min(height[left], height[right]), most)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return most

# leetcode submit region end(Prohibit modification and deletion)
