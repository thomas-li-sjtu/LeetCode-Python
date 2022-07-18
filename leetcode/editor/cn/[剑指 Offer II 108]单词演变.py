"""
在字典（单词列表） wordList 中，从单词 beginWord 和 endWord 的 转换序列 是一个按下述规格形成的序列： 

 
 序列中第一个单词是 beginWord 。 
 序列中最后一个单词是 endWord 。 
 每次转换只能改变一个字母。 
 转换过程中的中间单词必须是字典 wordList 中的单词。 
 

 给定两个长度相同但内容不同的单词 beginWord 和 endWord 和一个字典 wordList ，找到从 beginWord 到 endWord 的 
最短转换序列 中的 单词数目 。如果不存在这样的转换序列，返回 0。 

 

 示例 1： 

 
输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot",
"log","cog"]
输出：5
解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。
 

 示例 2： 

 
输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot",
"log"]
输出：0
解释：endWord "cog" 不在字典中，所以无法进行转换。 

 

 提示： 

 
 1 <= beginWord.length <= 10 
 endWord.length == beginWord.length 
 1 <= wordList.length <= 5000 
 wordList[i].length == beginWord.length 
 beginWord、endWord 和 wordList[i] 由小写英文字母组成 
 beginWord != endWord 
 wordList 中的所有字符串 互不相同 
 

 

 注意：本题与主站 127 题相同： https://leetcode-cn.com/problems/word-ladder/ 
 Related Topics 广度优先搜索 哈希表 字符串 👍 18 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 建图，超时
        # node_map = {word: [] for word in wordList}
        # node_map[beginWord] = []
        # visited = set()
        #
        # def is_connected(word1, word2):
        #     cnt = 0
        #     for i, j in zip(word1, word2):
        #         if i != j:
        #             cnt += 1
        #         if cnt > 1:
        #             return False
        #     return True
        #
        # for key, _ in node_map.items():
        #     for word in wordList:
        #         if key == word:
        #             continue
        #         if is_connected(key, word):
        #             node_map[key].append(word)
        #
        # cur_queue = [(i, 1) for i in node_map[beginWord]]
        # for cur_word in node_map[beginWord]:
        #     visited.add(cur_word)
        # while cur_queue:
        #     cur_word, cur_step = cur_queue.pop(0)
        #     if cur_word == endWord:
        #         return cur_step + 1
        #     else:
        #         for word in node_map[cur_word]:
        #             if word not in visited:
        #                 cur_queue.append((word, cur_step + 1))
        #                 visited.add(word)
        #
        # return 0

        # 不建图，直接暴力bfs
        import queue
        q = queue.Queue()
        q.put(beginWord)
        visit = {beginWord}
        length = len(beginWord)
        step = 1
        while not q.empty():
            step += 1
            for i in range(q.qsize()):
                word1 = q.get()
                for word2 in wordList:
                    if word2 not in visit:
                        c = 0
                        for i in range(length):
                            if word1[i] != word2[i]:
                                c += 1
                        if c == 1:
                            if word2 == endWord:
                                return step
                            else:
                                q.put(word2)
                                visit.add(word2)
        return 0


# leetcode submit region end(Prohibit modification and deletion)
