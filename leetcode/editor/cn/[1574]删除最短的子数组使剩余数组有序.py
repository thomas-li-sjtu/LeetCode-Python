"""
给你一个整数数组 arr ，请你删除一个子数组（可以为空），使得 arr 中剩下的元素是 非递减 的。 

 一个子数组指的是原数组中连续的一个子序列。 

 请你返回满足题目要求的最短子数组的长度。 

 

 示例 1： 

 
输入：arr = [1,2,3,10,4,2,3,5]
输出：3
解释：我们需要删除的最短子数组是 [10,4,2] ，长度为 3 。剩余元素形成非递减数组 [1,2,3,3,5] 。
另一个正确的解为删除子数组 [3,10,4] 。 

 示例 2： 

 
输入：arr = [5,4,3,2,1]
输出：4
解释：由于数组是严格递减的，我们只能保留一个元素。所以我们需要删除长度为 4 的子数组，要么删除 [5,4,3,2]，要么删除 [4,3,2,1]。
 

 示例 3： 

 
输入：arr = [1,2,3]
输出：0
解释：数组已经是非递减的了，我们不需要删除任何元素。
 

 示例 4： 

 
输入：arr = [1]
输出：0
 

 

 提示： 

 
 1 <= arr.length <= 10^5 
 0 <= arr[i] <= 10^9 
 
 Related Topics 栈 数组 双指针 二分查找 单调栈 👍 78 👎 0

"""
from typing import List
import bisect


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # 先从左到右搜索非递减子数组，然后从右向左搜索非递减子数组，整个数组被切分成立了left, mid, right3个部分。
        # 因为只删除1个子数组，所以答案是mid要被删除，然后再加上mid两边的若干个元素，直至剩余的部分都是非递减的。
        # 搜索mid两边的元素数，需要
        # 1、遍历left的每个元素，在right中搜索大于等于它的，记录此时的中间数组的大小
        # 2、遍历right的每个元素，在left中搜索小于它的，记录此时的两端的子数组大小；

        origin_arr = arr[:]
        increment, decrement = [], []
        length = len(arr)
        tmp_num = arr[0]
        for i in range(length):
            if arr[i] >= tmp_num:
                increment.append(arr[i])
                tmp_num = arr[i]
                arr[i] = -1
            else:
                break
        for i in range(length - 1, -1, -1):
            if arr[i] != -1:
                tmp_num = arr[i]
                break
        for i in range(length - 1, -1, -1):
            if arr[i] <= tmp_num and arr[i] != -1:
                decrement.append(arr[i])
                tmp_num = arr[i]
                arr[i] = -1
            else:
                break
        decrement.reverse()
        if len(increment) == length:
            return 0
        # if len(decrement) == 1:
        #     return length - 1
        ans = length
        print(increment)
        print(decrement)

        left, right = len(increment) - 1, length - len(decrement)
        # print(left, right)
        for i in range(left+1):
            j = bisect.bisect_left(origin_arr, origin_arr[i], right)
            ans = min(j - i - 1, ans)
            # print(ans)
        for i in range(right, length):
            j = bisect.bisect_left(origin_arr, origin_arr[i], 0, left + 1)
            ans = min(ans, i - j)
            # print(ans)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.findLengthOfShortestSubarray(arr=[1, 2, 3, 10, 4, 2, 3, 5]))
print(s.findLengthOfShortestSubarray(arr=[5, 4, 3, 2, 1]))
print(s.findLengthOfShortestSubarray(arr=[1,3,2,4]))
