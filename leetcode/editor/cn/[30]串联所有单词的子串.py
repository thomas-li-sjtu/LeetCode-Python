"""
给定一个字符串 s 和一些 长度相同 的单词 words 。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。 

 注意子串要与 words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑 words 中单词串联的顺序。 

 

 示例 1： 

 
输入：s = "barfoothefoobarman", words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
 

 示例 2： 

 
输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
输出：[]
 

 示例 3： 

 
输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
输出：[6,9,12]
 

 

 提示： 

 
 1 <= s.length <= 10⁴ 
 s 由小写英文字母组成 
 1 <= words.length <= 5000 
 1 <= words[i].length <= 30 
 words[i] 由小写英文字母组成 
 
 Related Topics 哈希表 字符串 滑动窗口 👍 720 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        char_dict = {}
        word_dict = {}
        for i in words:
            for char in i:
                if char_dict.get(char):
                    char_dict[char] += 1
                else:
                    char_dict[char] = 1
        for i in words:
            if word_dict.get(i):
                word_dict[i] += 1
            else:
                word_dict[i] = 1
        window_length = sum([len(i) for i in words])
        word_length = len(words[0])
        left, right = 0, 0
        res = []

        cur_dict = {}
        while right < len(s):
            if cur_dict.get(s[right]):
                cur_dict[s[right]] += 1
            else:
                cur_dict[s[right]] = 1

            if right-left + 1 < window_length:
                right += 1
                continue

            if right-left+1 == window_length:
                flag = True
                for key, value in char_dict.items():
                    if cur_dict.get(key) and cur_dict[key] == value:
                        continue
                    else:
                        flag = False
                        break
                if not flag:
                    right += 1
                    cur_dict[s[left]] -= 1
                    left += 1
                else:
                    cur_word_dict = {}
                    cur_string = s[left: right+1]
                    for i in range(0, window_length, word_length):
                        if cur_word_dict.get(cur_string[i: i+word_length]):
                            cur_word_dict[cur_string[i: i+word_length]] += 1
                        else:
                            cur_word_dict[cur_string[i: i + word_length]] = 1

                    word_flag = True
                    for key, value in word_dict.items():
                        if cur_word_dict.get(key) and cur_word_dict[key] == value:
                            continue
                        else:
                            word_flag = False
                            break
                    if word_flag:
                        res.append(left)
                    cur_dict[s[left]] -= 1
                    left += 1
                    right += 1
        return res

# leetcode submit region end(Prohibit modification and deletion)
