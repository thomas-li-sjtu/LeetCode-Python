"""
给定一个字符串数组 strs ，将 变位词 组合在一起。 可以按任意顺序返回结果列表。 

 注意：若两个字符串中每个字符出现的次数都相同，则称它们互为变位词。 

 

 示例 1: 

 
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]] 

 示例 2: 

 
输入: strs = [""]
输出: [[""]]
 

 示例 3: 

 
输入: strs = ["a"]
输出: [["a"]] 

 

 提示： 

 
 1 <= strs.length <= 10⁴ 
 0 <= strs[i].length <= 100 
 strs[i] 仅包含小写字母 
 

 

 注意：本题与主站 49 题相同： https://leetcode-cn.com/problems/group-anagrams/ 
 Related Topics 数组 哈希表 字符串 排序 👍 32 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from collections import Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # # 超时
        # res = []
        # backup = strs
        # flag = [False] * len(strs)
        # strs = [Counter(list(i)) for i in strs]
        # for i in range(len(strs)):
        #     cur = []
        #     for j in range(i, len(strs)):
        #         if strs[i] == strs[j] and not flag[j]:
        #             cur.append(backup[j])
        #             flag[j] = True
        #     if cur:
        #         res.append(cur)
        # return res

        dicts = {}
        for t in strs:
            # 将字符串序列化 作为字典的key
            g = ''.join(sorted(t))
            if g not in dicts.keys():
                dicts[g] = [t]
            else:
                dicts[g].append(t)
        return list(dicts.values())
# leetcode submit region end(Prohibit modification and deletion)
