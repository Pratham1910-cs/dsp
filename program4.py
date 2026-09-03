class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self._head = None

    def append(self, data):
        new_node = Node(data)

        if self._head is None:
            self._head = new_node
            new_node.next = new_node
            return

        current = self._head
        while current.next is not self._head:
            current = current.next

        current.next = new_node
        new_node.next = self._head

    def delete(self, key):
        if self._head is None:
            return False

        previous = self._head
        current = self._head.next

        if self._head.data == key:
            if self._head.next is self._head:
                self._head = None
            else:
                while previous.next is not self._head:
                    previous = previous.next
                self._head = self._head.next
                previous.next = self._head
            return True

        while current is not self._head:
            if current.data == key:
                previous.next = current.next
                return True
            previous = current
            current = current.next

        return False

    def iterate(self):
        if self._head is None:
            return

        current = self._head
        while True:
            yield current.data
            current = current.next
            if current is self._head:
                break

    def itrerate(self):
        return self.iterate()


if __name__ == "__main__":
    circular_list = CircularLinkedList()
    for value in (10, 20, 30):
        circular_list.append(value)

    print("Circular list:", " -> ".join(map(str, circular_list.iterate())))
    circular_list.delete(20)
    print("After deleting 20:", " -> ".join(map(str, circular_list.iterate())))