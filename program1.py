class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


if __name__ == "__main__":
    l1 = LinkedList()

    
    l1.insert_at_end(10)
    l1.insert_at_end(20)
    l1.insert_at_end(30)

    print("Linked List after inserting at end:")
    l1.display()


    l1.insert_at_beginning(5)

    print("Linked List after inserting at beginning:")
    l1.display()      
    

