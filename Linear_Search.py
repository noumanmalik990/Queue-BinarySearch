class Stack:
    def _init_(self):
        self.value = []

    def push(self, x):
        self.value.append(x)

    def pop(self):
        if self.value == []:
            return "Stack is Empty"
        top = self.value[-1]
        self.value = self.value[:-1]
        return top

    def linearSearch(self, item):
        found = False
        for i in range(len(self.value)):
            if self.value[i] == item:
                print(f"Item found at index number {i}")
                found = True
                break
        if not found:
            print("Item not found")


a = Stack()
l = int(input("Enter Stack limit: "))  
for i in range(l):
    e = int(input("Enter value: "))  
    a.push(e)

print("Stack content:", a.value)


print("Pop operation result:", a.pop())


o = int(input("Enter one item from the stack to search: "))
a.linearSearch(o)