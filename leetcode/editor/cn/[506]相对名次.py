# 给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold Medal",
#  "Silver Medal", "Bronze Medal"）。 
# 
#  (注：分数越高的选手，排名越靠前。) 
# 
#  示例 1: 
# 
#  
# 输入: [5, 4, 3, 2, 1]
# 输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# 解释: 前三名运动员的成绩为前三高的，因此将会分别被授予 “金牌”，“银牌”和“铜牌” ("Gold Medal", "Silver Medal" and 
# "Bronze Medal").
# 余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。 
# 
#  提示: 
# 
#  
#  N 是一个正整数并且不会超过 10000。 
#  所有运动员的成绩都不相同。 
#  
#  Related Topics 数组 排序 堆（优先队列） 
#  👍 93 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        # 维护一个 nums -> 索引的映射。之后对 paris 进行降序排列即可
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        rank = sorted([(s, i) for i, s in enumerate(score)], reverse=True)
        for idx, tup in enumerate(rank):
            if idx in [0, 1, 2]:
                score[tup[1]] = medals[idx]
            else:
                score[tup[1]] = str(idx + 1)
        return score

# leetcode submit region end(Prohibit modification and deletion)
