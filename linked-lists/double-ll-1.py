class DoubleLinkedNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def traverseForward(self):
        node = self
        while node:
            print(node.val)
            node = node.next


def remove_duplicates(node):
    seen = {}
    node = node
    while node:
        if node.val in seen:
            print("Removed", node.val)
            node.prev.next = node.next
            node.prev = None
            node.next = None

        seen[node.val] = True
        node = node.next


def main():
    node1 = DoubleLinkedNode(100)
    node2 = DoubleLinkedNode(20)
    node3 = DoubleLinkedNode(88)
    node4 = DoubleLinkedNode(20)

    node1.next = node2
    node2.next = node3
    node2.prev = node1
    node3.prev = node2
    node4.prev = node3
    node3.next = node4

    print("Traversing forward Node1")
    node1.traverseForward()

    print("Traversing forward Node2")
    node2.traverseForward()

    print("-> Removing duplicates from node1 head")
    remove_duplicates(node1)
    print("New Linked List")
    node1.traverseForward()


if __name__ == "__main__":
    main()
