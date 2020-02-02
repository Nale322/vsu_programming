class Matrix:

    def __init__(self):
        self.strok = None
        self.stolb = None
        self.elem = []

    def I_n_P_u_t_T_h_I_s(self):
        self.strok = int(input())
        self.stolb = int(input())
        for _ in range(self.stolb):
            self.elem.append([int(input()) for b in range(self.strok)])

    def P_r_I_n_T(self):
        for i in range(len(self.elem)):
            print(*self.elem[i])


a = Matrix()
a.I_n_P_u_t_T_h_I_s()
a.P_r_I_n_T()
