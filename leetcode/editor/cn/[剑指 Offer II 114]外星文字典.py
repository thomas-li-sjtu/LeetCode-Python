"""
现有一种使用英语字母的外星文语言，这门语言的字母顺序与英语顺序不同。 

 给定一个字符串列表 words ，作为这门语言的词典，words 中的字符串已经 按这门新语言的字母顺序进行了排序 。 

 请你根据该词典还原出此语言中已知的字母顺序，并 按字母递增顺序 排列。若不存在合法字母顺序，返回 "" 。若存在多种可能的合法字母顺序，返回其中 任意一种 顺
序即可。 

 字符串 s 字典顺序小于 字符串 t 有两种情况： 

 
 在第一个不同字母处，如果 s 中的字母在这门外星语言的字母顺序中位于 t 中字母之前，那么 s 的字典顺序小于 t 。 
 如果前面 min(s.length, t.length) 字母都相同，那么 s.length < t.length 时，s 的字典顺序也小于 t 。 
 

 

 示例 1： 

 
输入：words = ["wrt","wrf","er","ett","rftt"]
输出："wertf"
 

 示例 2： 

 
输入：words = ["z","x"]
输出："zx"
 

 示例 3： 

 
输入：words = ["z","x","z"]
输出：""
解释：不存在合法字母顺序，因此返回 "" 。
 

 

 提示： 

 
 1 <= words.length <= 100 
 1 <= words[i].length <= 100 
 words[i] 仅由小写英文字母组成 
 

 

 注意：本题与主站 269 题相同： https://leetcode-cn.com/problems/alien-dictionary/ 
 Related Topics 深度优先搜索 广度优先搜索 图 拓扑排序 数组 字符串 👍 120 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from collections import defaultdict


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # 遍历words统计所有出现的字母
        # 遍历words中相邻的每对，统计这两对字典序不同的原因（第一个出现不同的地方，如果都一样且前面的长，可以直接返回）
        # 从所有没有入度的字母开始，拓扑遍历所有转移（因为转移是满足字典序的，入度为0时加入的话，所有字典序比它小的都已经加入了，可以加入）

        graph, word_set = defaultdict(list), set()
        for w in words:
            word_set = word_set.union(set(w))

        degreee = [0] * 26
        for i in range(1, len(words)):
            word1, word2 = words[i - 1], words[i]
            for char_a, char_b in zip(word1, word2):
                if char_a != char_b:
                    graph[char_a].append(char_b)  # char_a 在 char_b 前面
                    degreee[ord(char_b) - ord('a')] += 1
                    break
            else:
                if len(word1) > len(word2):
                    return ""

        start = [k for k in word_set if degreee[ord(k) - ord('a')] == 0]
        for ch in start:
            for next_char in graph[ch]:
                v = ord(next_char) - ord('a')
                degreee[v] -= 1
                if degreee[v] == 0:
                    start.append(next_char)
        return "".join(start) if len(start) == len(word_set) else ""

# leetcode submit region end(Prohibit modification and deletion)
