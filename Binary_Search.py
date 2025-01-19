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

    def binarySearch(self, item):
        b = 0
        e = len(self.value) - 1
        ret = -1
        while b <= e:
            mid = (b + e) // 2
            if self.value[mid] == item:
                ret = mid
                break
            elif self.value[mid] < item:
                b = mid + 1
            else:
                e = mid - 1
        if ret != -1:
            print(f"Item found at index number {ret}")
        else:
            print("Item not found")


a = Stack()
l = int(input("Enter Stack limit: "))  
for i in range(l):
    e = int(input("Enter value: "))  
    a.push(e)

print("Stack content:", a.value)


print("Pop operation result:", a.pop())


o = int(input("Enter one item from the stack to search: "))
a.binarySearch(o)