from lista import LinkedList

def demo_lista():
    L = LinkedList()
    
    while True:
        print("\n1. wstaw na początek listy")
        print("2. wstaw na koniec listy")
        print("3. wypisz listę")
        print("4. koniec")
        
        wybor = input("Wybierz opcję: ")
        
        if wybor == '1':
            produkt = input("Podaj nazwę produktu: ")
            L.push_front(produkt)
        elif wybor == '2':
            produkt = input("Podaj nazwę produktu: ")
            L.push_back(produkt)
        elif wybor == '3':
            print("Zawartość listy: ", end="")
            current = L.head
            elementy = []
            while current:
                elementy.append(str(current.data))
                current = current.next
            print(" -> ".join(elementy) if elementy else "Pusta")
        elif wybor == '4':
            break
        else:
            print("Nieznana opcja ")

def find(L, x):
    count = 0
    current = L.head
    while current:
        if current.data == x:
            count += 1
        current = current.next
    return count


def delete(L, x):
    current = L.head
    while current:
        next_node = current.next
        if current.data == x:
            L.erase(current)
        current = next_node


def sort(dane):
    L = LinkedList()
    for x in dane:
        if L.is_empty():
            L.push_front(x)
        elif x <= L.head.data:
            L.push_front(x)
        elif x >= L.tail.data:
            L.push_back(x)
        else:
            current = L.head
            while current.next and current.next.data < x:
                current = current.next
            L.insert_after_node(current, x)
    return L

def merge(lista1, lista2):
    merged = LinkedList()
    curr1 = lista1.head
    curr2 = lista2.head

    while curr1 is not None and curr2 is not None:
        if curr1.data <= curr2.data:
            merged.push_back(curr1.data)
            curr1 = curr1.next
        else:
            merged.push_back(curr2.data)
            curr2 = curr2.next

    while curr1 is not None:
        merged.push_back(curr1.data)
        curr1 = curr1.next

    while curr2 is not None:
        merged.push_back(curr2.data)
        curr2 = curr2.next

    return merged
