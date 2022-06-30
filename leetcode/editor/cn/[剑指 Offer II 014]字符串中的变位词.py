"""
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的某个变位词。 

 换句话说，第一个字符串的排列之一是第二个字符串的 子串 。 

 

 示例 1： 

 
输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").
 

 示例 2： 

 
输入: s1= "ab" s2 = "eidboaoo"
输出: False
 

 

 提示： 

 
 1 <= s1.length, s2.length <= 10⁴ 
 s1 和 s2 仅包含小写字母 
 

 

 注意：本题与主站 567 题相同： https://leetcode-cn.com/problems/permutation-in-string/ 
 Related Topics 哈希表 双指针 字符串 滑动窗口 👍 50 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_dict = {}
        target_length = len(s1)
        for char in s1:
            if target_dict.get(char):
                target_dict[char] += 1
            else:
                target_dict[char] = 1

        window_dict = {key: 0 for key, _ in target_dict.items()}
        left, right = 0, 0
        while right < len(s2):
            if window_dict.get(s2[right]) is not None:
                window_dict[s2[right]] += 1
                if right - left + 1 == target_length:
                    flag = True
                    for key, value in window_dict.items():
                        if value != target_dict[key]:
                            flag = False
                            break
                    if flag:
                        return True
                    window_dict[s2[left]] -= 1
                    left += 1
                right += 1
            else:
                right += 1
                left = right
                for key, _ in window_dict.items():
                    window_dict[key] = 0

        return False
# leetcode submit region end(Prohibit modification and deletion)
