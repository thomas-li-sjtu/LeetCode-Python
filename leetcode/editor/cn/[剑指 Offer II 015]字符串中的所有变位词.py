"""
给定两个字符串 s 和 p，找到 s 中所有 p 的 变位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。 

 变位词 指字母相同，但排列不同的字符串。 

 

 示例 1： 

 
输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的变位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的变位词。
 

 示例 2： 

 
输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的变位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的变位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的变位词。
 

 

 提示: 

 
 1 <= s.length, p.length <= 3 * 10⁴ 
 s 和 p 仅包含小写字母 
 

 

 注意：本题与主站 438 题相同： https://leetcode-cn.com/problems/find-all-anagrams-in-a-
string/ 
 Related Topics 哈希表 字符串 滑动窗口 👍 29 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target_dict = {}
        target_length = len(p)
        for char in p:
            if target_dict.get(char):
                target_dict[char] += 1
            else:
                target_dict[char] = 1

        res = []
        window_dict = {key: 0 for key, _ in target_dict.items()}
        left, right = 0, 0
        while right < len(s):
            if window_dict.get(s[right]) is not None:
                window_dict[s[right]] += 1
                if right - left + 1 == target_length:
                    flag = True
                    for key, value in window_dict.items():
                        if value != target_dict[key]:
                            flag = False
                            break
                    if flag:
                        res.append(left)
                    window_dict[s[left]] -= 1
                    left += 1
                right += 1
            else:
                right += 1
                left = right
                for key, _ in window_dict.items():
                    window_dict[key] = 0

        return res
# leetcode submit region end(Prohibit modification and deletion)
