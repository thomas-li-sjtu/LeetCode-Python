"""
给定一个字符串 s ，请将 s 分割成一些子串，使每个子串都是 回文串 ，返回 s 所有可能的分割方案。 

 回文串 是正着读和反着读都一样的字符串。 

 

 示例 1： 

 
输入：s = "google"
输出：[["g","o","o","g","l","e"],["g","oo","g","l","e"],["goog","l","e"]]
 

 示例 2： 

 
输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
 

 示例 3： 

 
输入：s = "a"
输出：[["a"]] 

 

 提示： 

 
 1 <= s.length <= 16 
 s 仅由小写英文字母组成 
 

 

 注意：本题与主站 131 题相同： https://leetcode-cn.com/problems/palindrome-partitioning/ 
 Related Topics 深度优先搜索 广度优先搜索 图 哈希表 👍 32 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def check(word):
            left, right = 0, len(word) - 1
            while left < right:
                if word[left] == word[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True

        def back(start, end, cur_res):
            if start == end:
                res.append(cur_res[:])
            else:
                for i in range(start, end):
                    if check(s[start: i + 1]):
                        cur_res.append(s[start: i + 1])
                        back(i + 1, end, cur_res)
                        cur_res.pop()
                    else:
                        continue

        res = []
        back(0, len(s), [])
        return res
# leetcode submit region end(Prohibit modification and deletion)
