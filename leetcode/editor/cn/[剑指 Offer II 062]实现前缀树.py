"""
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检
查。 

 请你实现 Trie 类： 

 
 Trie() 初始化前缀树对象。 
 void insert(String word) 向前缀树中插入字符串 word 。 
 boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
 
 boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，
返回 false 。 
 

 

 示例： 

 
输入
inputs = ["Trie", "insert", "search", "search", "startsWith", "insert", 
"search"]
inputs = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出
[null, null, true, false, true, null, true]

解释
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True
 

 

 提示： 

 
 1 <= word.length, prefix.length <= 2000 
 word 和 prefix 仅由小写英文字母组成 
 insert、search 和 startsWith 调用次数 总计 不超过 3 * 10⁴ 次 
 

 

 

 注意：本题与主站 208 题相同：https://leetcode-cn.com/problems/implement-trie-prefix-tree/ 
 Related Topics 设计 字典树 哈希表 字符串 👍 24 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.child = {}
        self.is_word = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode(0)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur_node = self.root
        for i in word:
            if cur_node.child.get(i):
                cur_node = cur_node.child[i]
            else:
                new_node = TreeNode(i)
                cur_node.child[i] = new_node
                cur_node = new_node
        cur_node.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur_node = self.root
        for i in word:
            if cur_node.child.get(i):
                cur_node = cur_node.child[i]
            else:
                return False
        if cur_node.is_word:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur_node = self.root
        for i in prefix:
            if cur_node.child.get(i):
                cur_node = cur_node.child[i]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# leetcode submit region end(Prohibit modification and deletion)
