class Matrix:

    def __init__(self):
        self.strok = None
        self.stolb = None
        self.elem = []
        

    def inputthis(self):
        self.strok = int(input())
        self.stolb = int(input())
        for a in range(self.column):
            self.elem.append([int(input()) for b in range(self.strok)])
    
    def writeln(self):
        print(self.elem, end=' ')

a = Matrix()
a.inputthis()
a.writeln()
