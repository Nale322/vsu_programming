class Matrix:

    def __init__(self):
        self.strok = None
        self.stolb = None
        self.elem = []
        

    def inputthis(self):
        self.strok = int(input())
        self.stolb = int(input())
        for _ in range(self.stolb):
            self.elem.append([int(input()) for b in range(self.strok)])
    
    def writeln(self):
        for i in range(self.strok):
            print(self.elem[i])

a = Matrix()
a.inputthis()
a.writeln()
