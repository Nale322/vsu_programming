class Matrix:

    def __init__(self):
        self.strok = None
        self.stolb = None
        self.elem = []

    def input_this(self):
        self.strok = int(input())
        self.stolb = int(input())
        for _ in range(self.stolb):
            self.elem.append([int(input()) for b in range(self.strok)])

    def print(self):
        for i in self.elem:
            print(*i)


a = Matrix()
a.input_this()
a.print()
