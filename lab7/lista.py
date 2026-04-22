class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size_ = 0

    def __iter__(self):
        current = self.head

        while current:
            yield current.data
            current = current.next

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.size_

    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size_ += 1
        if self.tail is None:
            self.tail = new_node

    def push_back(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size_ += 1

    def pop_front(self):
        if self.is_empty(): return None
        data = self.head.data
        self.head = self.head.next
        if self.head is None: self.tail = None
        self.size_ -= 1
        return data

    def pop_back(self):
        if self.is_empty():
            return None

        data = self.tail.data  # Już wiemy, co zwrócimy dzięki self.tail

        # Przypadek 1: Tylko jeden element na liście
        if self.head == self.tail:
            self.head = self.tail = None
        else:     # Przypadek 2: Szukamy przedostatniego elementu
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next

            # Odłączamy ostatni element
            temp.next = None
            self.tail = temp

        self.size_ -= 1
        return data

    def display(self):
        print(*(x for x in self))

    def insert(self, index, data):
        if index < 0 or index > self.size_:
            print(f"Index poza zakresem: {index}")
            return None

        # Jeśli wstawiamy na początek, użyjmy gotowej metody
        if index == 0:
            self.push_front(data)
            return self.head

        # Jeśli wstawiamy na koniec, użyjmy gotowej metody
        if index == self.size_:
            self.push_back(data)
            return self.tail

        # Wstawianie w środku
        new_node = Node(data)
        prev_node = self.get_node(index - 1)

        new_node.next = prev_node.next
        prev_node.next = new_node

        self.size_ += 1
        return new_node

    def insert_after_node(self, node, data):
        if not node:
            print("Błąd: Nie można wstawić elementu po nieistniejącym węźle (None).")
            return None

        new_node = Node(data)

        # 1. Nowy węzeł musi przejąć to, co było po 'node'
        new_node.next = node.next

        # 2. 'node' teraz wskazuje na nasz nowy węzeł
        node.next = new_node

        # 3. Zwiększamy licznik rozmiaru
        self.size_ += 1

        # 4. Jeśli wstawialiśmy po starym ogonie, nowy węzeł zostaje nowym ogonem
        if node is self.tail:
            self.tail = new_node

        return new_node

    def get_node(self, index):
        if index < 0 or index >= self.size_:
            print(f"Błąd: Indeks {index} poza zakresem (size: {self.size_})")
            return None

        # Optymalizacja: jeśli pytamy o ostatni element, zwróć tail od razu O(1)
        if index == self.size_ - 1:
            return self.tail

        # Standardowe szukanie O(n)
        node = self.head
        for _ in range(index):
            node = node.next
        return node

    def erase(self, node):
        if self.head is None or node is None:
            return None
        if node == self.head:
            self.pop_front()
            return self.head
        if node == self.tail:
            self.pop_back()
            return None
        # Szukamy węzła, po którym następuje 'node'
        current = self.head
        while current.next is not None and current.next != node:
            current = current.next

        # Jeśli wyszliśmy z pętli i znaleźliśmy node
        if current.next == node:
            current.next = node.next
            self.size_ -= 1
            return current.next

        # Jeśli nie znaleziono węzła na liście
        return None

    def front(self):
        return self.head

    def back(self):
        return self.tail

    def clear(self):
        self.head = None
        self.tail = None
        self.size_ = 0

    def __str__(self):
        if self.is_empty():
            return "[]"

        # Wykorzystujemy to, że nasza klasa jest już iterowalna!
        # Tworzymy listę napisów z elementów i łączymy je przecinkami.
        elements = ", ".join(str(data) for data in self)
        return f"{elements}"