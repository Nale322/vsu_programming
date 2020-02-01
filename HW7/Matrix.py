class Matrix:

    def __init__(self):
        self.strok = None
        self.stolb = None
        self.elem = []
        

    def inputthis(self):
        self.strok = int(input())
        self.stolb = int(input())
        self.elem.append([[input() for a in range(self.stolb)] for b in range(self.strok)])
    
    def writeln(self):
        for row in self.elem:
            for elem in row:
                print(elem, end=' ')
                print()

a = Matrix()
a.inputthis()
a.writeln()
