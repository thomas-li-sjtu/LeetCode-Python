# 给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。打乱后，数组的所有排列应该是 等可能 的。 
# 
#  实现 Solution class: 
# 
#  
#  Solution(int[] nums) 使用整数数组 nums 初始化对象 
#  int[] reset() 重设数组到它的初始状态并返回 
#  int[] shuffle() 返回数组随机打乱后的结果 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入
# ["Solution", "shuffle", "reset", "shuffle"]
# [[[1, 2, 3]], [], [], []]
# 输出
# [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]
# 
# 解释
# Solution solution = new Solution([1, 2, 3]);
# solution.shuffle();    // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。例如，返回 [3, 
# 1, 2]
# solution.reset();      // 重设数组到它的初始状态 [1, 2, 3] 。返回 [1, 2, 3]
# solution.shuffle();    // 随机返回数组 [1, 2, 3] 打乱后的结果。例如，返回 [1, 3, 2]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 200 
#  -106 <= nums[i] <= 106 
#  nums 中的所有元素都是 唯一的 
#  最多可以调用 5 * 104 次 reset 和 shuffle 
#  
#  Related Topics 数组 数学 随机化 
#  👍 270 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # 洗牌算法：从 [x,n−1] 中随机出一个位置与 x 位置进行值交换，当所有位置都进行这样的处理后，便得到了一个公平的洗牌方案

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        :rtype: List[int]
        """
        import random

        res = self.nums[:]
        for i, num in enumerate(res):
            rand = random.randint(i, len(res)-1)
            res[i], res[rand] = res[rand], res[i]

        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# leetcode submit region end(Prohibit modification and deletion)
