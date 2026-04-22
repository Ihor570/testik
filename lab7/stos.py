from lista import LinkedList

def push(stack, a):
    stack.push_front(a)

def size(stack):
    return stack.size()

def empty(stack):
    return stack.is_empty()

def top(stack):
    if not empty(stack):
        return stack.head.data
    return None

def pop(stack):
    if not empty(stack):
        stack.pop_front()

def demo_stos():
    stos = LinkedList()
    print("\n**************** stos ****************")
    print("Wypelnianie stosu")

    for liczba in range(1, 20, 2):
        push(stos, liczba)
        print(liczba, end=' ')

    print(" <- wierzchołek stosu")
    print(f"size() -> {size(stos)}")
    print("Opróżnianie stosu")
    while not empty(stos):
        print(top(stos), end=" ")
        pop(stos)

if __name__ == "__main__":
    demo_stos()