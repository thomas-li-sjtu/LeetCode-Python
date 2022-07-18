"""
如果交换字符串 X 中的两个不同位置的字母，使得它和字符串 Y 相等，那么称 X 和 Y 两个字符串相似。如果这两个字符串本身是相等的，那它们也是相似的。 

 例如，"tars" 和 "rats" 是相似的 (交换 0 与 2 的位置)； "rats" 和 "arts" 也是相似的，但是 "star" 不与 
"tars"，"rats"，或 "arts" 相似。 

 总之，它们通过相似性形成了两个关联组：{"tars", "rats", "arts"} 和 {"star"}。注意，"tars" 和 "arts" 是在同一组
中，即使它们并不相似。形式上，对每个组而言，要确定一个单词在组中，只需要这个词和该组中至少一个单词相似。 

 给定一个字符串列表 strs。列表中的每个字符串都是 strs 中其它所有字符串的一个 字母异位词 。请问 strs 中有多少个相似字符串组？ 

 字母异位词（anagram），一种把某个字符串的字母的位置（顺序）加以改换所形成的新词。 

 

 示例 1： 

 
输入：strs = ["tars","rats","arts","star"]
输出：2
 

 示例 2： 

 
输入：strs = ["omv","ovm"]
输出：1
 

 

 提示： 

 
 1 <= strs.length <= 300 
 1 <= strs[i].length <= 300 
 strs[i] 只包含小写字母。 
 strs 中的所有单词都具有相同的长度，且是彼此的字母异位词。 
 

 

 注意：本题与主站 839 题相同：https://leetcode-cn.com/problems/similar-string-groups/ 
 Related Topics 深度优先搜索 广度优先搜索 并查集 数组 字符串 👍 16 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        # 每个字符串是一个点，存在相似关键则存在一个边
        # 建图（关系）然后广度遍历图记录有多少个连通分量

        def is_similar(str1, str2):
            if len(str1) != len(str2):
                return False
            else:
                cnt = 0
                for i, j in zip(str1, str2):
                    if i != j:
                        cnt += 1
                    if cnt > 2:
                        return False
                return True

        similar_dict = {i: set() for i in strs}
        visited = set()

        for i in range(len(strs)):
            for j in range(len(strs)):
                if i == j:
                    continue
                if is_similar(strs[i], strs[j]):
                    similar_dict[strs[i]].add(strs[j])

        res = 0
        for string in strs:
            if string not in visited:
                res += 1
                visited.add(string)
                queue = list(similar_dict[string])
                while queue:
                    cur_str = queue.pop(0)
                    visited.add(cur_str)
                    for new_str in list(similar_dict[cur_str]):
                        if new_str not in visited:
                            queue.append(new_str)
                            visited.add(new_str)

        return res

# leetcode submit region end(Prohibit modification and deletion)
