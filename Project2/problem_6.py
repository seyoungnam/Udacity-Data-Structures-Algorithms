class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)
        return

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node.next = node
        return size


def union(llist_1, llist_2):
    set1, set2 = set(), set()
    sets = [set1, set2]
    for i, llist in enumerate([llist_1, llist_2]):
        if llist.head is None:
            continue
        node = llist.head
        while node:
            sets[i].add(node.value)
            node = node.next

    eles = set1 | set2
    answer = LinkedList()
    for value in eles:
        answer.append(value)
    return answer if answer.head is not None else "No union exists."
        


def intersection(llist_1, llist_2):
    set1, set2 = set(), set()
    sets = [set1, set2]
    for i, llist in enumerate([llist_1, llist_2]):
        if llist.head is None:
            continue
        node = llist.head
        while node:
            sets[i].add(node.value)
            node = node.next

    eles = set1 & set2
    answer = LinkedList()
    for value in eles:
        answer.append(value)
    return answer if answer.head is not None else "No intersection exists."


if __name__ == "__main__":
    # test case 1
    print("Test case 1")

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print (union(linked_list_1,linked_list_2))                  # 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> 
    print (intersection(linked_list_1,linked_list_2))           # 4 -> 21 -> 6 -> 

    # test case 2 - edge case
    print("Test case 2")

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = []
    element_2 = []

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print (union(linked_list_3,linked_list_4))                  # No union exists.
    print (intersection(linked_list_3,linked_list_4))           # No intersection exists.

    # test case 3 - edge case
    print("Test case 3")

    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    element_1 = []
    element_2 = [46,2,4,71,6]

    for i in element_1:
        linked_list_5.append(i)

    for i in element_2:
        linked_list_6.append(i)

    print (union(linked_list_5,linked_list_6))                 # 2 -> 4 -> 6 -> 71 -> 46 -> 
    print (intersection(linked_list_5,linked_list_6))          # No intersection exists.
