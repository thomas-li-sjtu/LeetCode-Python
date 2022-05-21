"""
在代号为 C-137 的地球上，Rick 发现如果他将两个球放在他新发明的篮子里，它们之间会形成特殊形式的磁力。Rick 有 n 个空的篮子，第 i 个篮子的位


置在 position[i] ，Morty 想把 m 个球放到这些篮子里，使得任意两球间 最小磁力 最大。 

 已知两个球如果分别位于 x 和 y ，那么它们之间的磁力为 |x - y| 。 

 给你一个整数数组 position 和一个整数 m ，请你返回最大化的最小磁力。 

 

 示例 1： 

 

 输入：position = [1,2,3,4,7], m = 3
输出：3
解释：将 3 个球分别放入位于 1，4 和 7 的三个篮子，两球间的磁力分别为 [3, 3, 6]。最小磁力为 3 。我们没办法让最小磁力大于 3 。
 

 示例 2： 

 输入：position = [5,4,3,2,1,1000000000], m = 2
输出：999999999
解释：我们使用位于 1 和 1000000000 的篮子时最小磁力最大。
 

 

 提示： 

 
 n == position.length 
 2 <= n <= 10^5 
 1 <= position[i] <= 10^9 
 所有 position 中的整数 互不相同 。 
 2 <= m <= position.length 
 
 Related Topics 数组 二分查找 排序 👍 104 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # 先排序，二分枚举相邻两球之间的间距，只需要统计当前间距下能放下多少个小球，记为 cnt，若 cnt >= m，说明此间距符合条件
        # 继续二分查找，最终找到符合条件的最大间距
        position.sort()

        def check(f):
            pre = position[0]
            cnt = 1
            for pos in position[1:]:  # 按照间距f放置小球
                if pos - pre >= f:
                    cnt += 1
                    pre = pos
            return cnt >= m

        left, right = 1, position[-1]
        while left < right:
            mid = (left + right + 1) >> 1
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left

# 二分查找两个模板

# boolean check(int x) {}
#
# int search(int left, int right) {
#     while (left < right) {
#         int mid = (left + right) >> 1;  # int mid = (left + right + 1) >> 1;
#         if (check(mid)) right = mid;    # if (check(mid)) left = mid;
#         else left = mid + 1;            # else right = mid - 1;
#     }
#     return left;
# }


# leetcode submit region end(Prohibit modification and deletion)
