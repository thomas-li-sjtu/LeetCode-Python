"""
给定一个长度为 n 的整数数组 nums ，其中 nums 是范围为 [1，n] 的整数的排列。还提供了一个 2D 整数数组 sequences ，其中 
sequences[i] 是 nums 的子序列。 
检查 nums 是否是唯一的最短 超序列 。最短 超序列 是 长度最短 的序列，并且所有序列 sequences[i] 都是它的子序列。对于给定的数组 
sequences ，可能存在多个有效的 超序列 。 

 
 例如，对于 sequences = [[1,2],[1,3]] ，有两个最短的 超序列 ，[1,2,3] 和 [1,3,2] 。 
 而对于 sequences = [[1,2],[1,3],[1,2,3]] ，唯一可能的最短 超序列 是 [1,2,3] 。[1,2,3,4] 是可能的超序列
，但不是最短的。 
 

 如果 nums 是序列的唯一最短 超序列 ，则返回 true ，否则返回 false 。 
子序列 是一个可以通过从另一个序列中删除一些元素或不删除任何元素，而不改变其余元素的顺序的序列。 

 

 示例 1： 

 
输入：nums = [1,2,3], sequences = [[1,2],[1,3]]
输出：false
解释：有两种可能的超序列：[1,2,3]和[1,3,2]。
序列 [1,2] 是[1,2,3]和[1,3,2]的子序列。
序列 [1,3] 是[1,2,3]和[1,3,2]的子序列。
因为 nums 不是唯一最短的超序列，所以返回false。
 

 示例 2： 

 
输入：nums = [1,2,3], sequences = [[1,2]]
输出：false
解释：最短可能的超序列为 [1,2]。
序列 [1,2] 是它的子序列：[1,2]。
因为 nums 不是最短的超序列，所以返回false。
 

 示例 3： 

 
输入：nums = [1,2,3], sequences = [[1,2],[1,3],[2,3]]
输出：true
解释：最短可能的超序列为[1,2,3]。
序列 [1,2] 是它的一个子序列：[1,2,3]。
序列 [1,3] 是它的一个子序列：[1,2,3]。
序列 [2,3] 是它的一个子序列：[1,2,3]。
因为 nums 是唯一最短的超序列，所以返回true。 

 

 提示： 

 
 n == nums.length 
 1 <= n <= 10⁴ 
 nums 是 [1, n] 范围内所有整数的排列 
 1 <= sequences.length <= 10⁴ 
 1 <= sequences[i].length <= 10⁴ 
 1 <= sum(sequences[i].length) <= 10⁵ 
 1 <= sequences[i][j] <= n 
 sequences 的所有数组都是 唯一 的 
 sequences[i] 是 nums 的一个子序列 
 

 

 注意：本题与主站 444 题相同：https://leetcode-cn.com/problems/sequence-reconstruction/ 
 Related Topics 图 拓扑排序 数组 👍 27 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        # 需要确定两个相邻的数字，a, a + 1，在seqs中，必然要有一个序列是[ ?, ?, a, a+1，？] —— 如果seqs里面有一个序列是[1, 3, 5]，这个序列是无用的, 因为seq里面的数字不相邻
        # 因此，只需要遍历seqs，判断所有的(1, 2), (2, 3), ... (n-2, n-1), (n-1, n)是否在seqs的序列里面

        if len(nums) == 1:
            for seq in sequences:
                if not seq:
                    continue
                elif len(seq) > 1:
                    return False
                else:
                    for i in seq:
                        if i != 1:
                            return False
            return True
        else:
            size = len(nums)
            index = [0]*size
            for i in range(size):
                index[nums[i]-1] = i  # 给定一个nums的元素，确定其在nums的下标
            flag = [False]*(size-1)
            for seq in sequences:
                if len(seq) == 1:
                    if seq[0] > size:
                        return False
                    else:
                        continue
                for i in range(len(seq)-1):
                    if seq[i] > size or seq[i+1] > size:
                        return False

                    index_a, index_b = index[seq[i]-1], index[seq[i+1]-1]
                    if index_a >= index_b:
                        return False
                    if index_a + 1 == index_b:
                        flag[index_a] = True

            for i in flag:
                if not i:
                    return False
            return True

# leetcode submit region end(Prohibit modification and deletion)
