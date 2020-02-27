'''
Given the root of a binary tree, consider all root to leaf paths: paths from the root to any leaf.  (A leaf is a node with no children.)

A node is insufficient if every such root to leaf path intersecting this node has sum strictly less than limit.

Delete all insufficient nodes simultaneously, and return the root of the resulting binary tree.



Example 1:


Input: root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1

Output: [1,2,3,4,null,null,7,8,9,null,14]
Example 2:


Input: root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22

Output: [5,4,8,11,null,17,4,7,null,null,null,5]


Example 3:


Input: root = [1,2,-3,-5,null,4,null], limit = -1

Output: [1,null,-3,4]


Note:

The given tree will have between 1 and 5000 nodes.
-10^5 <= node.val <= 10^5
-10^9 <= limit <= 10^9
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def find_delete_nodes(self, node, sum_, limit):
        delete = [0, 0]
        sum_ += node.val

        if (node.left != None):
            delete[0] = self.find_delete_nodes(node.left, sum_, limit)

            if (delete[0] == 1):
                node.left = None

        if (node.right != None):
            delete[1] = self.find_delete_nodes(node.right, sum_, limit)

            if (delete[1] == 1):
                node.right = None

        if (delete[0] == 2 or delete[1] == 2):
            return 2
        elif (delete[0] == 1 and delete[1] == 1):
            return 1
        elif (delete[0] == 0 and delete[1] == 0):
            if (sum_ < limit):
                return 1
            else:
                return 2
        else:
            return 1

    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        delete = self.find_delete_nodes(root, 0, limit)

        if (delete == 1):
            return None
        else:
            return root

#