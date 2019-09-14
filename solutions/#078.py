from heapq import heappush, heappop


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_lists(linked_lists):
    merged = list()
    head = Node(None)
    tail_pointer = head

    for llist in linked_lists:
        heappush(merged, (llist.val, llist))
    while merged:
        next_node = heappop(merged)[1]
        if next_node.next:
            heappush(merged, (next_node.next.val, next_node))
        tail_pointer.next = next_node
        tail_pointer = tail_pointer.next

    return head.next


def list_to_nodes(linked_lists):
    next_node = None
    for value in linked_lists[::-1]:
        node = Node(value)
        node.next = next_node
        next_node = node

    return next_node


def nodes_to_list(root):
    node = root
    nodes = list()
    while node:
        nodes.append(node.val)
        node = node.next
    return nodes


def main():
    assert nodes_to_list(merge_lists([list_to_nodes([1, 4, 6]),
                                      list_to_nodes([1, 3, 7])])) == [1, 1, 3, 4, 6, 7]
    assert nodes_to_list(merge_lists([list_to_nodes([1, 4, 6]),
                                      list_to_nodes([2, 3, 9]),
                                      list_to_nodes([1, 3, 7])])) == [1, 1, 2, 3, 3, 4, 6, 7, 9]
