# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [1], k = 1
# 输出: [1] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 105 
#  k 的取值范围是 [1, 数组中不相同的元素的个数] 
#  题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的 
#  
# 
#  
# 
#  进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。 
#  Related Topics 数组 哈希表 分治 桶排序 计数 快速选择 排序 堆（优先队列） 
#  👍 995 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 桶排序
        # 使用哈希表统计频率，统计完成后，创建一个数组，将频率作为数组下标，对于出现频率不同的数字集合，存入对应的数组下标即可
        freq_dict = {}
        for i in nums:
            if freq_dict.get(i):
                freq_dict[i] += 1
            else:
                freq_dict[i] = 1
        bucket = [[] for _ in range(len(nums))]
        for key, value in freq_dict.items():
            bucket[value-1].append(key)
        out, counter = [], 0
        for i in range(len(bucket)-1, -1, -1):
            if bucket[i]:
                out.extend(bucket[i])
                counter += len(bucket[i])
                if counter == k:
                    break
        return out

        # 或者：
        # 哈希表建立数字和其出现次数的映射，遍历一遍数组统计元素的频率
        # 维护一个元素数目为 k 的最小堆
        # 每次都将新的元素与堆顶元素（堆中频率最小的元素）进行比较
        # 如果新的元素的频率比堆顶端的元素大，则弹出堆顶端的元素，将新的元素添加进堆中
        # 最终，堆中的 k 个元素即为前 k 个高频元素
# leetcode submit region end(Prohibit modification and deletion)
