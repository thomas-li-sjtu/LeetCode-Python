"""
给你一个正整数 n ，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，并且其值大于 n 。如果不存在这样的正整数，则返回 -1 。 

 注意 ，返回的整数应当是一个 32 位整数 ，如果存在满足题意的答案，但不是 32 位整数 ，同样返回 -1 。 

 

 示例 1： 

 
输入：n = 12
输出：21
 

 示例 2： 

 
输入：n = 21
输出：-1
 

 

 提示： 

 
 1 <= n <= 2³¹ - 1 
 
 Related Topics 数学 双指针 字符串 👍 204 👎 0

"""
import heapq


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = [int(num) for num in str(n)[::-1]]
        stack = []
        for i, num in enumerate(s):
            if not stack or num >= stack[-1]:
                stack.append(num)
            else:
                cur = 0
                while cur < len(stack):
                    if stack[cur] > num:  # 找到遍历过的、比num大的数字中最小的那个
                        s[i] = stack[cur]
                        stack[cur] = num
                        stack.sort(reverse=True)
                        for j, new in enumerate(stack):  # 把遍历过的数字排序
                            s[j] = new
                        news = [str(num) for num in s]
                        ret = int(''.join(reversed(news)))
                        return ret if ret < 2 ** 31 else -1
                    else:
                        cur += 1
        return -1


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.nextGreaterElement(230241))
