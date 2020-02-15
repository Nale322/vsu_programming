class Matrix:

    def __init__(self):
        self.strok = None
        self.stolb = None
        self.elem = []

    def input_this(self):
        self.strok = int(input())
        self.stolb = int(input())
        self.elem = [[int(input()) for x in range(self.stolb)]
                    for x in range(self.strok)]

    def __str__(self):
        return '\n'.join(' '.join(str(i) for i in x) for x in self.elem)


a = Matrix()
a.input_this()
print(a)
