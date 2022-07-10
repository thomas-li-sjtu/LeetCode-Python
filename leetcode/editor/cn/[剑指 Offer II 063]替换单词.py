"""
在英语中，有一个叫做 词根(root) 的概念，它可以跟着其他一些词组成另一个较长的单词——我们称这个词为 继承词(successor)。例如，词根an，跟随着
单词 other(其他)，可以形成新的单词 another(另一个)。 

 现在，给定一个由许多词根组成的词典和一个句子，需要将句子中的所有继承词用词根替换掉。如果继承词有许多可以形成它的词根，则用最短的词根替换它。 

 需要输出替换之后的句子。 

 

 示例 1： 

 
输入：dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the 
battery"
输出："the cat was rat by the bat"
 

 示例 2： 

 
输入：dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
输出："a a b c"
 

 示例 3： 

 
输入：dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa a aaaa aaa aaa aaa 
aaaaaa bbb baba ababa"
输出："a a a a a a a a bbb baba a"
 

 示例 4： 

 
输入：dictionary = ["catt","cat","bat","rat"], sentence = "the cattle was rattled 
by the battery"
输出："the cat was rat by the bat"
 

 示例 5： 

 
输入：dictionary = ["ac","ab"], sentence = "it is abnormal that this solution is 
accepted"
输出："it is ab that this solution is ac"
 

 

 提示： 

 
 1 <= dictionary.length <= 1000 
 1 <= dictionary[i].length <= 100 
 dictionary[i] 仅由小写字母组成。 
 1 <= sentence.length <= 10^6 
 sentence 仅由小写字母和空格组成。 
 sentence 中单词的总量在范围 [1, 1000] 内。 
 sentence 中每个单词的长度在范围 [1, 1000] 内。 
 sentence 中单词之间由一个空格隔开。 
 sentence 没有前导或尾随空格。 
 

 

 注意：本题与主站 648 题相同： https://leetcode-cn.com/problems/replace-words/ 
 Related Topics 字典树 数组 哈希表 字符串 👍 23 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.child = {}
        self.is_word = False


class Solution:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode(0)

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence = sentence.split(" ")
        for word in dictionary:
            self.insert(word)
        for index, word in enumerate(sentence):
            cur_node = self.root
            end = -1
            for i, char in enumerate(word):
                if cur_node.is_word:
                    end = i
                    break
                else:
                    if cur_node.child.get(char):
                        cur_node = cur_node.child[char]
                    else:
                        break
            print(end)
            if end != -1:
                sentence[index] = word[:end]
        return " ".join(sentence)

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
# leetcode submit region end(Prohibit modification and deletion)
