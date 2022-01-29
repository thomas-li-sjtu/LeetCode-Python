# 给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。 
# 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：[3,2,3]
# 输出：[3] 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1]
# 输出：[1]
#  
# 
#  示例 3： 
# 
#  
# 输入：[1,1,1,3,3,2,2,2]
# 输出：[1,2] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 5 * 104 
#  -109 <= nums[i] <= 109 
#  
# 
#  
# 
#  进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题。 
#  Related Topics 数组 哈希表 计数 排序 
#  👍 554 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # num_dict = {}
        # n = len(nums)
        # for num in nums:
        #     if num_dict.get(num):
        #         num_dict[num] += 1
        #     else:
        #         num_dict[num] = 1
        # return [key for key, value in num_dict.items() if value > n//3]

        # 摩尔投票
        a, b = -1, -1
        count_a, count_b = 0, 0
        for i in nums:
            if i == a and count_a > 0:
                count_a += 1
            elif i == b and count_b > 0:
                count_b += 1
            elif count_a == 0:
                a, count_a = i, 1
            elif count_b == 0:
                b, count_b = i, 1
            else:
                count_a -= 1
                count_b -= 1
            # if count_a == 0:  这个顺序不行！！
            #     a, count_a = i, 1
            # elif i == a and count_a > 0:
            #     count_a += 1
            # elif count_b == 0:
            #     b, count_b = i, 1
            # elif i == b and count_b > 0:
            #     count_b += 1
            # elif i != a and i != b:
            #     count_a -= 1
            #     count_b -= 1
        real_a, real_b = 0, 0
        for i in nums:
            if i == a:
                real_a += 1
            if i == b:
                real_b += 1
        out = []
        if real_a > len(nums) // 3:
            out.append(a)
        if real_b > len(nums) // 3 and a != b:
            out.append(b)
        return out
# leetcode submit region end(Prohibit modification and deletion)
