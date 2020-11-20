class Funzione:
    def __init__(self,a,b,x):
        self.a=a
        self.b=b
        self.x=x
    def eval(self,x):
    pass
class Retta(Funzione):
    def __init__(self,nome,a,b,m,q):
        super().__init__("Retta",a,b)
        self.m=m
        self.q=q
    def eval(self,x):
        return self.m*x+self.q
    pass