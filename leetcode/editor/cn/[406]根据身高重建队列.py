"""
假设有打乱顺序的一群人站成一个队列，数组 people 表示队列中一些人的属性（不一定按顺序）。每个 people[i] = [hi, ki] 表示第 i 个人
的身高为 hi ，前面 正好 有 ki 个身高大于或等于 hi 的人。 

 请你重新构造并返回输入数组 people 所表示的队列。返回的队列应该格式化为数组 queue ，其中 queue[j] = [hj, kj] 是队列中第 
j 个人的属性（queue[0] 是排在队列前面的人）。 

 

 
 

 示例 1： 

 
输入：people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
输出：[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
解释：
编号为 0 的人身高为 5 ，没有身高更高或者相同的人排在他前面。
编号为 1 的人身高为 7 ，没有身高更高或者相同的人排在他前面。
编号为 2 的人身高为 5 ，有 2 个身高更高或者相同的人排在他前面，即编号为 0 和 1 的人。
编号为 3 的人身高为 6 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。
编号为 4 的人身高为 4 ，有 4 个身高更高或者相同的人排在他前面，即编号为 0、1、2、3 的人。
编号为 5 的人身高为 7 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。
因此 [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] 是重新构造后的队列。
 

 示例 2： 

 
输入：people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
输出：[[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
 

 

 提示： 

 
 1 <= people.length <= 2000 
 0 <= hi <= 10⁶ 
 0 <= ki < people.length 
 题目数据确保队列可以被重建 
 
 Related Topics 贪心 数组 排序 👍 1181 👎 0

"""
from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 一般这种数对，还涉及排序的，根据第一个元素正向排序，根据第二个元素反向排序，或者根据第一个元素反向排序，根据第二个元素正向排序，往往能够简化解题过程
        # 如果身高比他更高的人已经排好队了，这个人加入当前队列的位置就可以根据k值确定
        # 因此，身高较高的人应该先加入，先对队列按身高降序排序。此外，对于相同身高的人，k值较小的人位置在前，优先加入
        if len(people) <= 1:
            return people
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        new_people = [people[0]]  # 这个人是从前往后、从上往下看到的第一个人
        for i in people[1:]:
            new_people.insert(i[1], i)
        return new_people
# leetcode submit region end(Prohibit modification and deletion)
