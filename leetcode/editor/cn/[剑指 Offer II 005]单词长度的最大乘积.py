"""
给定一个字符串数组 words，请计算当两个字符串 words[i] 和 words[j] 不包含相同字符时，它们长度的乘积的最大值。假设字符串中只包含英语的小
写字母。如果没有不包含相同字符的一对字符串，返回 0。 

 

 示例 1: 

 
输入: words = ["abcw","baz","foo","bar","fxyz","abcdef"]
输出: 16 
解释: 这两个单词为 "abcw", "fxyz"。它们不包含相同字符，且长度的乘积最大。 

 示例 2: 

 
输入: words = ["a","ab","abc","d","cd","bcd","abcd"]
输出: 4 
解释: 这两个单词为 "ab", "cd"。 

 示例 3: 

 
输入: words = ["a","aa","aaa","aaaa"]
输出: 0 
解释: 不存在这样的两个单词。
 

 

 提示： 

 
 2 <= words.length <= 1000 
 1 <= words[i].length <= 1000 
 words[i] 仅包含小写字母 
 

 

 注意：本题与主站 318 题相同：https://leetcode-cn.com/problems/maximum-product-of-word-
lengths/ 
 Related Topics 位运算 数组 字符串 👍 86 👎 0

"""
from typing import List
from itertools import permutations


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        mask_list = []
        for index, word in enumerate(words):
            cur_bin = 0
            for char in word:
                char_idx = ord(char)-ord('a')
                cur_bin = cur_bin | (1 << char_idx)
            mask_list.append((cur_bin, len(word)))

        for w1, w2 in permutations(mask_list, 2):
            if w1[0] & w2[0] == 0:
                res = max(res, w1[1]*w2[1])

        return res
# leetcode submit region end(Prohibit modification and deletion)
