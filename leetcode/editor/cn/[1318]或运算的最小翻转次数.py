"""
给你三个正整数 a、b 和 c。 

 你可以对 a 和 b 的二进制表示进行位翻转操作，返回能够使按位或运算 a OR b == c 成立的最小翻转次数。 

 「位翻转操作」是指将一个数的二进制表示任何单个位上的 1 变成 0 或者 0 变成 1 。 

 

 示例 1： 

 

 输入：a = 2, b = 6, c = 5
输出：3
解释：翻转后 a = 1 , b = 4 , c = 5 使得 a OR b == c 

 示例 2： 

 输入：a = 4, b = 2, c = 7
输出：1
 

 示例 3： 

 输入：a = 1, b = 2, c = 3
输出：0
 

 

 提示： 

 
 1 <= a <= 10^9 
 1 <= b <= 10^9 
 1 <= c <= 10^9 
 
 Related Topics 位运算 👍 39 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        bin_a = str(bin(a))[2:]
        bin_b = str(bin(b))[2:]
        bin_c = str(bin(c))[2:]

        max_len = max(len(bin_a), len(bin_b), len(bin_c))
        if len(bin_a) < max_len:
            bin_a = "0" * (max_len - len(bin_a)) + bin_a
        if len(bin_b) < max_len:
            bin_b = "0" * (max_len - len(bin_b)) + bin_b
        if len(bin_c) < max_len:
            bin_c = "0" * (max_len - len(bin_c)) + bin_c

        print(bin_a, bin_b, bin_c)

        def convert(char1, char2, char3):
            convert_dict = {
                (0, 0, 0): 0,
                (0, 0, 1): 1,
                (0, 1, 0): 1,
                (0, 1, 1): 0,
                (1, 0, 0): 1,
                (1, 0, 1): 0,
                (1, 1, 0): 2,
                (1, 1, 1): 0,
            }
            return convert_dict[(int(char1), int(char2), int(char3))]

        res = 0
        for i in range(max_len):
            res += convert(bin_a[i], bin_b[i], bin_c[i])

        return res
# leetcode submit region end(Prohibit modification and deletion)
