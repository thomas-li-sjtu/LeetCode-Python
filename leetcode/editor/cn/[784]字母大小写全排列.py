"""
给定一个字符串 s ，通过将字符串 s 中的每个字母转变大小写，我们可以获得一个新的字符串。 

 返回 所有可能得到的字符串集合 。以 任意顺序 返回输出。 

 

 示例 1： 

 
输入：s = "a1b2"
输出：["a1b2", "a1B2", "A1b2", "A1B2"]
 

 示例 2: 

 
输入: s = "3z4"
输出: ["3z4","3Z4"]
 

 

 提示: 

 
 1 <= s.length <= 12 
 s 由小写英文字母、大写英文字母和数字组成 
 
 Related Topics 位运算 字符串 回溯 👍 369 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        alpha_pos = [i for i in range(len(s)) if s[i].isalpha()]
        res = []

        alpha_combine = [self.combine(alpha_pos, i) for i in range(len(alpha_pos) + 1)]
        for combine_list in alpha_combine:
            for pos_list in combine_list:
                copy_s = list(s)
                for pos in pos_list:
                    if copy_s[pos].isupper():
                        copy_s[pos] = copy_s[pos].lower()
                    elif copy_s[pos].islower():
                        copy_s[pos] = copy_s[pos].upper()
                    else:
                        raise IndexError
                res.append("".join(copy_s))

        return res

    def combine(self, array, k):  # 从array中选k个
        paths = []
        res = []

        def backtrack(index):
            if len(paths) == k:
                res.append(paths[:])
                return
            for i in range(index, len(array)):
                paths.append(array[i])
                backtrack(i + 1)
                paths.pop()

        backtrack(0)
        return res


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.letterCasePermutation("ab1234"))
print(s.letterCasePermutation("a1b2"))
