class Matrix:

    def __init__(self):
        self.strok = None
        self.stolb = None
        self.elem = []
        self.matrix = []
        

    def inputthis(self):
        self.strok = int(input())
        self.stolb = int(input())
        self.matrix = [[input() for a in range(self.stolb)] for b in range(self.strok)]
    
    def writeln(self):
        matrix = self.matrix
        for im in range(len(matrix)):
            print(matrix[im])

a = Matrix()
a.inputthis()
a.writeln()