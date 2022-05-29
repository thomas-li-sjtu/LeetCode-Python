"""
你有一些球的库存 inventory ，里面包含着不同颜色的球。一个顾客想要 任意颜色 总数为 orders 的球。 

 这位顾客有一种特殊的方式衡量球的价值：每个球的价值是目前剩下的 同色球 的数目。比方说还剩下 6 个黄球，那么顾客买第一个黄球的时候该黄球的价值为 6 。这笔
交易以后，只剩下 5 个黄球了，所以下一个黄球的价值为 5 （也就是球的价值随着顾客购买同色球是递减的） 

 给你整数数组 inventory ，其中 inventory[i] 表示第 i 种颜色球一开始的数目。同时给你整数 orders ，表示顾客总共想买的球数目。
你可以按照 任意顺序 卖球。 

 请你返回卖了 orders 个球以后 最大 总价值之和。由于答案可能会很大，请你返回答案对 10⁹ + 7 取余数 的结果。 

 

 示例 1： 

 
输入：inventory = [2,5], orders = 4
输出：14
解释：卖 1 个第一种颜色的球（价值为 2 )，卖 3 个第二种颜色的球（价值为 5 + 4 + 3）。
最大总和为 2 + 5 + 4 + 3 = 14 。
 

 示例 2： 

 
输入：inventory = [3,5], orders = 6
输出：19
解释：卖 2 个第一种颜色的球（价值为 3 + 2），卖 4 个第二种颜色的球（价值为 5 + 4 + 3 + 2）。
最大总和为 3 + 2 + 5 + 4 + 3 + 2 = 19 。
 

 示例 3： 

 
输入：inventory = [2,8,4,10,6], orders = 20
输出：110
 

 示例 4： 

 
输入：inventory = [1000000000], orders = 1000000000
输出：21
解释：卖 1000000000 次第一种颜色的球，总价值为 500000000500000000 。 500000000500000000 对 109 + 7 
取余为 21 。
 

 

 提示： 

 
 1 <= inventory.length <= 10⁵ 
 1 <= inventory[i] <= 10⁹ 
 1 <= orders <= min(sum(inventory[i]), 10⁹) 
 
 Related Topics 贪心 数组 数学 二分查找 排序 堆（优先队列） 👍 62 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True)  # 如果不reverse，就要从后往前遍历了
        sell = 0
        ans = 0

        def get(start, cnt, repeat, times):  # 处理不满的一轮
            ful, left = divmod(times, repeat)
            # 并列项数的整数倍部分按照等差数列求和公式，余数乘上卖出整数倍之后的价值
            return (2 * start - ful + 1) * ful * repeat // 2 + (start - ful) * left

        p = 0
        while p < len(inventory):
            while p < len(inventory) - 1 and inventory[p] == inventory[p + 1]:  # 重复项合并处理
                p += 1
            # cnt为每种当前价值最高的球能卖出的数量，注意如果没有下一项，cnt就是当前项本身
            cnt = inventory[p] - inventory[p + 1] if p < len(inventory) - 1 else inventory[p]

            if (p + 1) * cnt + sell <= orders:  # 注意数组的下标从0开始，所以并列价值最高的项数是p+1
                # 等差数列求和公式，尾项是是当前项减去cnt再加1，不要忘了乘上并列的数量
                ans = (ans + (2 * inventory[p] - cnt + 1) * (p + 1) * cnt // 2) % (10 ** 9 + 7)
                sell += (p + 1) * cnt
            else:
                # 这种情况对应这轮已经不满，这时可以直接return了
                return (ans + get(inventory[p], cnt, p + 1, orders - sell)) % (10 ** 9 + 7)
            p += 1
        return ans  # 如果没有这一行，orders=sum(inventory)的情况就缺少返回值


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.maxProfit(inventory=[1000000000], orders=1000000000))
