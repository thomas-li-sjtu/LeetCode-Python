"""
输入一个字符串，打印出该字符串中字符的所有排列。 

 

 你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。 

 

 示例: 

 输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
 

 

 限制： 

 1 <= s 的长度 <= 8 
 Related Topics 字符串 回溯 👍 566 👎 0

"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permutation(self, s: str) -> List[str]:
        res = []
        s = list(s)

        def permute(string: list, start: int, length: int):
            if start == length:
                res.append("".join(string))
            for index in range(start, length):
                string[index], string[start] = string[start], string[index]
                permute(string, start+1, length)
                string[index], string[start] = string[start], string[index]

        permute(s, start=0, length=len(s))
        return list(set(res))

# leetcode submit region end(Prohibit modification and deletion)
