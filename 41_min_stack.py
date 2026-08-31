class MinStack:
    def __init__(self):
        self.stack = list([])
        self.mins = list([])

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(val)
            self.mins.append(val)
        else:
            if val > self.mins[-1]:
                self.stack.append(val)
            else:
                self.stack.append(val)
                self.mins.append(val)
        
    def pop(self) -> None:
        if len(self.stack) == 0:
            return None
        elif len(self.stack) == 1:
            self.stack.pop()
            self.mins.pop()
        else:
            if self.stack[-1] > self.mins[-1]:
                self.stack.pop()
            else:
                self.stack.pop()
                self.mins.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.mins) == 0:
            return None
        else:
            return self.mins[-1]


if __name__ == "__main__":
    x = MinStack()

    x.push(1)
    x.push(2)
    x.push(3)
    x.push(4)
    x.push(0)
    x.push(10)

    print(x.top())
    print(x.getMin())

    x.pop()

    print("\n")

    print(x.top())
    print(x.getMin())

    x.push(-1)

    print("\n")

    print(x.top())
    print(x.getMin())

    x.push(3)

    print("\n")

    print(x.top())
    print(x.getMin())