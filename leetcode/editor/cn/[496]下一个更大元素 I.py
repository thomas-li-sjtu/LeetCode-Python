# 给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。 
# 
#  请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。 
# 
#  nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
# 输出: [-1,3,-1]
# 解释:
#     对于 num1 中的数字 4 ，你无法在第二个数组中找到下一个更大的数字，因此输出 -1 。
#     对于 num1 中的数字 1 ，第二个数组中数字1右边的下一个较大数字是 3 。
#     对于 num1 中的数字 2 ，第二个数组中没有下一个更大的数字，因此输出 -1 。 
# 
#  示例 2: 
# 
#  
# 输入: nums1 = [2,4], nums2 = [1,2,3,4].
# 输出: [3,-1]
# 解释:
#     对于 num1 中的数字 2 ，第二个数组中的下一个较大数字是 3 。
#     对于 num1 中的数字 4 ，第二个数组中没有下一个更大的数字，因此输出 -1 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums1.length <= nums2.length <= 1000 
#  0 <= nums1[i], nums2[i] <= 104 
#  nums1和nums2中所有整数 互不相同 
#  nums1 中的所有整数同样出现在 nums2 中 
#  
# 
#  
# 
#  进阶：你可以设计一个时间复杂度为 O(nums1.length + nums2.length) 的解决方案吗？ 
#  Related Topics 栈 数组 哈希表 单调栈 
#  👍 605 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 利用栈的知识，依次让第二个数组里面元素入栈，如果碰到要入栈的数比栈顶元素大的情况，则运用hashMap(key,value)，
        # hashMap存储的是一个键值对，我们将此时比栈顶大的数作为‘值’，此时的栈顶作为‘键’存储到hashMap中，并将这个大的数入栈，最后依次循环直至完成遍历第二个数组
        dic = {}
        stack = [nums2[0]]
        for i in range(1, len(nums2)):
            while stack and stack[-1] < nums2[i]:
                dic[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        return [dic[i] if dic.get(i) else -1 for i in nums1]

# leetcode submit region end(Prohibit modification and deletion)
