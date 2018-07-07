class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def traverse(self):
        node = self
        while node != None:
            print(node.val)
            node = node.next


def main():
    node1 = Node(12)
    node2 = Node(24)
    node3 = Node(3)
    node4 = Node(100)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    node1.traverse()


if __name__ == "__main__":
    main()
