"""
给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按任何顺序返回答案。 

 有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。 

 例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 
"192.168@1.1" 是 无效 IP 地址。 

 

 示例 1： 

 
输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]
 

 示例 2： 

 
输入：s = "0000"
输出：["0.0.0.0"]
 

 示例 3： 

 
输入：s = "1111"
输出：["1.1.1.1"]
 

 示例 4： 

 
输入：s = "010010"
输出：["0.10.0.10","0.100.1.0"]
 

 示例 5： 

 
输入：s = "10203040"
输出：["10.20.30.40","102.0.30.40","10.203.0.40"]
 

 

 提示： 

 
 0 <= s.length <= 3000 
 s 仅由数字组成 
 

 

 注意：本题与主站 93 题相同：https://leetcode-cn.com/problems/restore-ip-addresses/ 
 Related Topics 字符串 回溯 👍 34 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        def check(word):
            length = len(word)
            if word[0] == '0':
                if length == 1:
                    return True
                else:
                    return False
            for i in word:
                if not i.isdigit():
                    return False
            if int(word) > 255:
                return False
            return True

        def back(start, end, cur_res):
            if start == end and len(cur_res) == 4:
                res.append(".".join(cur_res[:]))
            else:
                for i in range(start, end):
                    if check(s[start: i+1]):
                        cur_res.append(s[start: i+1])
                        back(i+1, end, cur_res)
                        cur_res.pop()

        if len(s) > 12:
            return []
        res = []
        back(0, len(s), [])
        return res

# leetcode submit region end(Prohibit modification and deletion)
