"""
给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。 

 换句话说，s1 的排列之一是 s2 的 子串 。 

 

 示例 1： 

 
输入：s1 = "ab" s2 = "eidbaooo"
输出：true
解释：s2 包含 s1 的排列之一 ("ba").
 

 示例 2： 

 
输入：s1= "ab" s2 = "eidboaoo"
输出：false
 

 

 提示： 

 
 1 <= s1.length, s2.length <= 10⁴ 
 s1 和 s2 仅包含小写字母 
 
 Related Topics 哈希表 双指针 字符串 滑动窗口 👍 621 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}
        for i in s1:
            if s1_dict.get(i):
                s1_dict[i] += 1
            else:
                s1_dict[i] = 1
        left, right = 0, 0
        if len(s2) < len(s1):
            return False
        window_dict = {key: 0 for key, _ in s1_dict.items()}
        while left < len(s2) and right < len(s2):
            if s1_dict.get(s2[right]):
                window_dict[s2[right]] += 1
            right += 1
            if right - left > len(s1):
                if window_dict.get(s2[left]):
                    window_dict[s2[left]] -= 1
                left += 1
            if right - left == len(s1):
                flag = 1
                for key, value in s1_dict.items():
                    if window_dict.get(key) and window_dict[key] == s1_dict[key]:
                        continue
                    else:
                        flag = 0
                        break
                if flag:
                    return True

        return False
# leetcode submit region end(Prohibit modification and deletion)
