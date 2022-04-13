"""
字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。 

 

 示例： 

 
输入：S = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
 

 

 提示： 

 
 S的长度在[1, 500]之间。 
 S只包含小写字母 'a' 到 'z' 。 
 
 Related Topics 贪心 哈希表 双指针 字符串 👍 704 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letter_dict = {}
        for i, char in enumerate(s):
            if letter_dict.get(char):
                letter_dict[char].append(i)
            else:
                letter_dict[char] = [i]

        area = []
        for i in letter_dict.values():
            area.append([i[0], i[-1]])
        area = sorted(area, key=lambda x: x[0])
        left, right = area[0][0], area[0][1]

        res = []
        for i in range(1, len(area)):
            new_left, new_right = area[i][0], area[i][1]
            if left <= new_left <= new_right <= right:
                continue
            elif left <= new_left <= right <= new_right:
                right = new_right
            elif new_left <= left <= right <= new_right:
                left, right = new_left, new_right
            elif left <= right < new_left <= new_right:
                res.append(right-left+1)
                left, right = new_left, new_right
        res.append(right-left+1)
        return res
# leetcode submit region end(Prohibit modification and deletion)
