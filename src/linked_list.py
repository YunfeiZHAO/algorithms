""" linked list """
from typing import Optional


class ListNode:
    """ A node of linked list """
    def __init__(self, data: int):
        self.data = data
        self.next = None

    def add_list(self, list_data: list[int]) -> 'ListNode':
        """ Add a list of data to the linked list
            Args:
                list_data: list of integers to add
            Returns:
                self, the head of the linked list
        """
        current = self
        for data in list_data:
            current.next = ListNode(data)
            current = current.next
        return self

    def to_list(self) -> list[int]:
        """ Convert linked list to a list of integers
            Returns:
                A list of integers representing the linked list
        """
        result = []
        current = self
        while current:
            result.append(current.data)
            current = current.next
        return result


def findMergeNode(head1, head2):
    """ two head of Non null head of linked list, there is a merge point 
        of two linked lists. return its value.
    """
    p1 = head1
    p2 = head2

    while p1 != p2:
        p1 = p1.next if p1 else head2
        p2 = p2.next if p2 else head1

    return p1.data


def hasCycle(self, head: Optional[ListNode]) -> bool:
    """ check if linked list has cycle
        Args:
            head: head of linked list
        Returns:
            True if has cycle, False otherwise
        https://leetcode.com/problems/linked-list-cycle/
        The idea is the Floyd's Tortoise and Hare algorithm.
        We use two pointers, one moves one step at a time (slow), and the other moves two steps at a time (fast).
        If there is a cycle, the fast pointer will eventually meet the slow pointer.
    """
    slow = fast = head
    while fast and fast.next:
        slow=slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def detectCycle(head):
    """ Detect the start node of the cycle in a linked list.
        Args:
            head: head of linked list
        Returns:
            The node where the cycle begins, or None if there is no cycle.
        https://leetcode.com/problems/linked-list-cycle-ii/

        If they meet, it means there is a cycle.
        fast moved 2V, slow moved V, so the distance between them is V.
        2V - V = n*C, where n is a number and C is the length of the cycle.
        If we move one pointer to the head and keep the other at the meeting point, for example the slow pointer,
        when the it reach the start of the cycle, it will go V + k steps, where k is the number of steps from the start of the cycle to the meeting point.
        The faster pointer will also go 2V + k steps, so they will meet at the start of the cycle.
    """
    slow = fast = head

    # Step 1: Detect if cycle exists
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # Cycle detected
            break
    else:
        return None  # No cycle

    # Step 2: Find the cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow  # This is the cycle start node


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """ Remove the nth node from the end of the linked list
        Args:
            head: head of linked list
            n: the position from the end of the linked list to remove
        Returns:
            The head of the modified linked list
        https://leetcode.com/problems/remove-nth-node-from-end-of-list/
        Idea is to use two pointers. The first pointer moves n+1 steps ahead, then both pointers move one step at a time until
        the first pointer reaches the end of the list.
        At that point, the second pointer will be at the node just before the one we want to remove.
    """
    dummy = ListNode(0)
    dummy.next = head

    p1, p2 = dummy, dummy
    for _ in range(n+1):
        p2 = p2.next
    while p2:
        p2 = p2.next
        p1 = p1.next
    p1.next = p1.next.next
    return dummy.next


def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    """reverse a list
    https://neetcode.io/problems/reverse-a-linked-list
    """
    prev = None
    cur = head
    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    return prev


if __name__ == "__main__":
    # head = ListNode(1)
    # head.add_list([2, 3, 4, 5])
    # print(head.to_list())
    # removeNthFromEnd(head, 2)
    # print(head.to_list())

    head = ListNode(1)
    print(head.to_list())
    head = removeNthFromEnd(head, 1)
    print(head.to_list())
