'''Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.



Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.


Note:

The number of nodes in the given list will be between 1 and 100.'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:   #Time Complexity : O(N) where N is the number of nodes in the given list. and Space Complexity O(1)the space used by slow aand fast
    def middleNode(self, head):
        slow = fast = head
        while fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


class Solution(object): #Time Complexity : O(N) where N is the number of nodes in the given list. and Space Complexity O(N)the space used by A
    def middleNode(self, head):
        A = [head]
        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A) // 2]

'''Test Case:
input : [1,2,3,4,5,6,7,8,9,10]
output: [6,7,8,9,10] '''
