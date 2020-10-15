class Node:
    def _init_(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def _init_(self, head):
        self.head = head

    def length(self):
        current = self.head
        if current is not None:
            count = 1

            while current.next is not None:
                count += 1
                current = current.next
            return count
        else:
            return 0

    def insert(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = linked_list.head
            linked_list.head = new_node
        else:
            current = linked_list.head
            k = 1
            while current.next is not None and k < position:
                current = current.next
                k += 1
            new_node.next = current.next
            current.next = new_node

    def correr_k_veces(self, k):
        if k >= self.length():
            k = k % self.length()

        i = 1
        while i <= k:
            current = self.head
            while current.next.next is not None:
                current = current.next

            current.next.next = self.head
            self.head = current.next
            current.next = None
            i += 1

    def show_list(self):
        current = linked_list.head
        while current is not None:
            print(current.data, end=", ")
            current = current.next
        print()


linked_list = SinglyLinkedList(Node(1))

for i in range(2, 6):
    linked_list.insert(i, i-1)


print("Lista:")
linked_list.show_list()

linked_list.correr_k_veces(10000008)
print("Lista corrida K veces:")
linked_list.show_list()
