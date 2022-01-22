# Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼
# 写检查。 
# 
#  请你实现 Trie 类： 
# 
#  
#  Trie() 初始化前缀树对象。 
#  void insert(String word) 向前缀树中插入字符串 word 。 
#  boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false
#  。 
#  boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否
# 则，返回 false 。 
#  
# 
#  
# 
#  示例： 
# 
#  
# 输入
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# 输出
# [null, null, true, false, true, null, true]
# 
# 解释
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // 返回 True
# trie.search("app");     // 返回 False
# trie.startsWith("app"); // 返回 True
# trie.insert("app");
# trie.search("app");     // 返回 True
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= word.length, prefix.length <= 2000 
#  word 和 prefix 仅由小写英文字母组成 
#  insert、search 和 startsWith 调用次数 总计 不超过 3 * 104 次 
#  
#  Related Topics 设计 字典树 哈希表 字符串 
#  👍 1030 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class TreeNode(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,
                     "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0,
                     "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
                     "y": 0, "z": 0}
        self.end_of_word = None


class Trie(object):

    def __init__(self):
        self.origin_node = TreeNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        tmp_node = self.origin_node
        for index, char in enumerate(word):
            if tmp_node.next[char] == 0:
                node = TreeNode(val=char)
                tmp_node.next[char] = node
            tmp_node = tmp_node.next[char]
            if index == len(word)-1:
                tmp_node.end_of_word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        tmp_node = self.origin_node
        for index, char in enumerate(word):
            if tmp_node.next[char] == 0:
                return False
            else:
                tmp_node = tmp_node.next[char]
            if index == len(word)-1 and not tmp_node.end_of_word:
                return False
        return True

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        tmp_node = self.origin_node
        for char in prefix:
            if tmp_node.next[char] == 0:
                return False
            else:
                tmp_node = tmp_node.next[char]
        return True




# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# leetcode submit region end(Prohibit modification and deletion)
