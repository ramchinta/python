'''Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. Boundary includes left boundary,
 leaves, and right boundary in order without duplicate nodes.  (The values of the nodes may still be duplicates.)

Left boundary is defined as the path from root to the left-most node. Right boundary is defined as the path from root to the right-most node.
If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary.
Note this definition only applies to the input binary tree, and not applies to any subtrees.

The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists.
If not, travel to the right subtree. Repeat until you reach a leaf node.

The right-most node is also defined by the same way with left and right exchanged.

Example 1

Input:
  1
   \
    2
   / \
  3   4

Ouput:
[1, 3, 4, 2]

Explanation:
The root doesn't have left subtree, so the root itself is left boundary.
The leaves are node 3 and 4.
The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
So order them in anti-clockwise without duplicates and we have [1,3,4,2].


Example 2

Input:
    ____1_____
   /          \
  2            3
 / \          /
4   5        6
   / \      / \
  7   8    9  10

Ouput:
[1,2,4,7,8,9,10,6,3]

Explanation:
The left boundary are node 1,2,4. (4 is the left-most node according to definition)
The leaves are node 4,7,8,9,10.
The right boundary are node 1,3,6,10. (10 is the right-most node).
So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leftBoundary(self, root, res):
        if not root:
            return
        if not root.left and not root.right:
            return
        res.append(root.val)
        if root.left != None:
            self.leftBoundary(root.left, res)
        else:
            self.leftBoundary(root.right, res)

    def rightBoundary(self, root, res):
        if not root:
            return
        if not root.left and not root.right:
            return
        if root.right != None:
            self.rightBoundary(root.right, res)
        else:
            self.rightBoundary(root.left, res)
        res.append(root.val)

    def leave(self, root, res):
        if not root:
            return
        if not root.left and not root.right:
            res.append(root.val)
            return
        self.leave(root.left, res)
        self.leave(root.right, res)

    def boundaryOfBinaryTreeNaive(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        if root.left or root.right:
            res.append(root.val)
        self.leftBoundary(root.left, res)
        self.leave(root, res)
        self.rightBoundary(root.right, res)
        return res

    def helper(self, root, leftFlag, rightFlag, res):
        if not root: return
        if not root.left and not root.right:
            res.append(root.val)
            return
        if leftFlag:
            res.append(root.val)
        self.helper(root.left, (leftFlag and root.left), (rightFlag and not root.right), res)
        self.helper(root.right, (leftFlag and not root.left), (rightFlag and root.right), res)
        if rightFlag:
            res.append(root.val)

    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res

        res.append(root.val)
        self.helper(root.left, True, False, res)
        self.helper(root.right, False, True, res)
        return res