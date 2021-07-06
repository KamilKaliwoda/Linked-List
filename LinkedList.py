from copy import deepcopy


class Element:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self) -> bool:
        return self.head is None

    def destroy(self) -> None:
        self.head = None

    def add(self, value) -> None:
        if self.head is None:
            self.head = Element(value)
        else:
            copy = self.head
            self.head = Element(value)
            self.head.next = copy

    def remove(self) -> None:
        if self.is_empty():
            raise ValueError("List is already empty.")
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next

    def length(self) -> int:
        if self.is_empty():
            return 0
        elif self.head.next is None:
            return 1
        else:
            counter = 0
            copy = self.head
            while copy:
                counter += 1
                copy = copy.next
            return counter

    def get(self) -> [Element, None]:
        if self.is_empty():
            raise ValueError("List is empty.")
        else:
            return deepcopy(self.head.data)

    def display(self) -> None:
        result = "["
        copy = self.head
        while copy.next:
            result = result + str(copy.data) + ", "
            copy = copy.next
        result = result + str(copy.data) + "]"
        print(result)

    def add_to_end(self, value) -> None:
        if self.is_empty():
            self.head = Element(value)
        else:
            reference = self.head
            while reference.next:
                reference = reference.next
            reference.next = Element(value)

    def remove_from_end(self) -> None:
        length = self.length()
        if length == 0:
            raise ValueError("List is already empty.")
        elif length == 1:
            self.head = None
        else:
            reference = self.head
            while reference.next.next:
                reference = reference.next
            reference.next = None

    def take(self, n: int) -> [Element, None]:
        length = self.length()
        if n >= length:
            copy = LinkedList()
            reference = self.head
            while reference:
                copy.add_to_end(reference.data)
                reference = reference.next
            return copy
        elif n < 0:
            raise ValueError("Invalid argument.")
        else:
            copy = LinkedList()
            reference = self.head
            for i in range(n):
                copy.add_to_end(reference.data)
                reference = reference.next
            return copy

    def drop(self, n: int) -> [Element, None]:
        length = self.length()
        if n >= length:
            return LinkedList()
        elif n < 0:
            raise ValueError("Invalid argument.")
        else:
            copy = LinkedList()
            reference = self.head
            for i in range(n):
                reference = reference.next
            while reference:
                copy.add_to_end(reference.data)
                reference = reference.next
            return copy

    def reverse(self) -> [Element, None]:
        if self.is_empty():
            return
        else:
            copy = LinkedList()
            while not self.is_empty():
                copy.add(self.head.data)
                self.remove()
            self.head = copy.head





