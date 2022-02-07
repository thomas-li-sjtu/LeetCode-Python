# 如果字符串中不含有任何 'aaa'，'bbb' 或 'ccc' 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。 
# 
#  给你三个整数 a，b ，c，请你返回 任意一个 满足下列全部条件的字符串 s： 
# 
#  
#  s 是一个尽可能长的快乐字符串。 
#  s 中 最多 有a 个字母 'a'、b 个字母 'b'、c 个字母 'c' 。 
#  s 中只含有 'a'、'b' 、'c' 三种字母。 
#  
# 
#  如果不存在这样的字符串 s ，请返回一个空字符串 ""。 
# 
#  
# 
#  示例 1： 
# 
#  输入：a = 1, b = 1, c = 7
# 输出："ccaccbcc"
# 解释："ccbccacc" 也是一种正确答案。
#  
# 
#  示例 2： 
# 
#  输入：a = 2, b = 2, c = 1
# 输出："aabbc"
#  
# 
#  示例 3： 
# 
#  输入：a = 7, b = 1, c = 0
# 输出："aabaa"
# 解释：这是该测试用例的唯一正确答案。 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= a, b, c <= 100 
#  a + b + c > 0 
#  
#  Related Topics 贪心 字符串 堆（优先队列） 
#  👍 79 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        # 每次都使用两个当前余下最多的那种字符f，然后选择次多的字符s作为间隔
        # 当出现f与s出现的次数一致时，这里的间隔使用两个s，否则使用一个s
        import heapq

        res = []
        heap = []
        if a > 0:
            heapq.heappush(heap, [-a, 'a'])
        if b > 0:
            heapq.heappush(heap, [-b, 'b'])
        if c > 0:
            heapq.heappush(heap, [-c, 'c'])
        while heap:
            if len(heap) == 1:
                cnt, char = heap[0]
                res.append(char)
                if cnt <= -2:
                    res.append(char)

                break

            else:
                cnt1, char1 = heapq.heappop(heap)
                cnt2, char2 = heapq.heappop(heap)
                if cnt1 == cnt2:
                    res.append(char1)
                    res.append(char2)
                    if cnt1 <= -2:
                        res.append(char1)
                        res.append(char2)
                        cnt1 += 1
                        cnt2 += 1
                    cnt1 += 1
                    cnt2 += 1
                else:
                    res.append(char1)
                    if cnt1 <= -2:
                        res.append(char1)
                        cnt1 += 1
                    cnt1 += 1
                    res.append(char2)
                    cnt2 += 1

                if cnt1 < 0:
                    heapq.heappush(heap, [cnt1, char1])
                if cnt2 < 0:
                    heapq.heappush(heap, [cnt2, char2])

        return ''.join(res)

# leetcode submit region end(Prohibit modification and deletion)
