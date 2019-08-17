class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def removeConsecutiveSumTo0(node):
    start = node
    end = None
    while start:
        removed = False
        total = 0
        end = start
        while end:
            total += end.value
            if total == 0:
                removed = True
                start = end
                break
            else:
                end = end.next

        if removed:
            


node = Node(10)
node.next = Node(5)
node.next.next = Node(-3)
node.next.next.next = Node(-3)
node.next.next.next.next = Node(1)
node.next.next.next.next.next = Node(4)
node.next.next.next.next.next.next = Node(-4)
node = removeConsecutiveSumTo0(node)
while node:
    print(node.value)
    node = node.next
# 10
