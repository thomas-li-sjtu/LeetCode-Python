# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。 
# 
#  高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-10,-3,0,5,9]
# 输出：[0,-3,9,-10,null,5]
# 解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：
# 
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,3]
# 输出：[3,1]
# 解释：[1,3] 和 [3,1] 都是高度平衡二叉搜索树。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 104 
#  -104 <= nums[i] <= 104 
#  nums 按 严格递增 顺序排列 
#  
#  Related Topics 树 二叉搜索树 数组 分治 二叉树 
#  👍 877 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # 二叉搜索树（BST）中序遍历就是升序序列
        # 高度平衡二叉树：选择数组的中间元素作为根节点
        def dfs(left, right):
            if left > right:
                return None

            root_index = left + (right - left) // 2
            root = TreeNode(nums[root_index])

            root.left = dfs(left, root_index-1)
            root.right = dfs(root_index+1, right)

            return root
        return dfs(0, len(nums)-1)

# leetcode submit region end(Prohibit modification and deletion)
