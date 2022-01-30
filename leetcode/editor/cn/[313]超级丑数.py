# 超级丑数 是一个正整数，并满足其所有质因数都出现在质数数组 primes 中。 
# 
#  给你一个整数 n 和一个整数数组 primes ，返回第 n 个 超级丑数 。 
# 
#  题目数据保证第 n 个 超级丑数 在 32-bit 带符号整数范围内。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 12, primes = [2,7,13,19]
# 输出：32 
# 解释：给定长度为 4 的质数数组 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,
# 28,32] 。 
# 
#  示例 2： 
# 
#  
# 输入：n = 1, primes = [2,3,5]
# 输出：1
# 解释：1 不含质因数，因此它的所有质因数都在质数数组 primes = [2,3,5] 中。
#  
#  
# 
#  
#  
#  
#  提示： 
# 
#  
#  1 <= n <= 106 
#  1 <= primes.length <= 100 
#  2 <= primes[i] <= 1000 
#  题目数据 保证 primes[i] 是一个质数 
#  primes 中的所有值都 互不相同 ，且按 递增顺序 排列 
#  
#  
#  
#  
#  Related Topics 数组 哈希表 数学 动态规划 堆（优先队列） 
#  👍 296 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        m = len(primes)
        pt = [0]*m  # 指针
        out = [0] * n
        out[0] = 1
        candidate = [out[last_ugly_pointer] * prime for prime, last_ugly_pointer in zip(primes, pt)]

        for i in range(1, n):
            out[i] = min(candidate)
            for j in range(m):
                if out[i] == out[pt[j]] * primes[j]:
                    pt[j] += 1
                    candidate[j] = out[pt[j]] * primes[j]
        return out[-1]

# leetcode submit region end(Prohibit modification and deletion)
