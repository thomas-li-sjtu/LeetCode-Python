"""
字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。 

 

 示例 1: 

 输入: 
first = "pale"
second = "ple"
输出: True 

 

 示例 2: 

 输入: 
first = "pales"
second = "pal"
输出: False
 
 Related Topics 双指针 字符串 👍 144 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        point1, point2 = 0, 0
        counter = 0

        while point1 < len(first) and point2 < len(second):
            if first[point1] == second[point2]:
                point1 += 1
                point2 += 1
                continue
            else:
                counter += 1
                if counter > 1:
                    return False
                if len(first) == len(second):
                    point1 += 1
                    point2 += 1
                elif len(first) < len(second):
                    point2 += 1
                else:
                    point1 += 1

        if (
                len(first) == 0 and len(second) == 1
                or len(second) == 0 and len(first) == 1
                or len(first) == 0 and len(second) == 0
        ):
            return True
        if point1 != len(first) or point2 != len(second):
            if counter == 0 and (
                    point1 == len(first) and point2 == len(second) - 1
                    or point1 == len(first) - 1 and point2 == len(second)
            ):
                return True
            return False
        return True


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.oneEditAway("a", "ab"))
print(s.oneEditAway("", "a"))
