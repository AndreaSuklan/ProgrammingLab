class Funzione:
    def __init__(self,name,a,b):
        self.name=name
        self.a=a
        self.b=b
    
    def nome(self):
        print("Funzione da ",self.a," a ",self.b)
    
    def valori(self,message,values):
        troppo=False
        if (type(values) is list and len(values)>10):
            troppo=True
            values=values[1:10]
            values=values+["..."]
        if (not troppo):
            print("---o---o---o---")
        else:
            print("---o---o---o---(Vengono mostrati solo i primi 10 valori)")
        print(message,"->",values)
        print("---o---o---o---\n")
        
    def minimo(self,dex):
        print("Calcolo valore più vicino allo zero")
        self.nome()
        x1=self.a
        x2=self.b
        i=0
        f=[]
        absf=[]
        x=[]
        while ((x1+dex*i)<=x2):
            xo=x1+dex*i
            fxo=self.eval(xo)
            x.append(xo)
            f.append(fxo)
            absf.append(abs(fxo))
            i=i+1
        self.valori("Dominio x",x)
        self.valori("Funzione f(x)",f)
        self.valori("Valori assoluti f(x)",absf)
        xmin=0
        for i in range(len(absf)):
            if (absf[i]<absf[xmin]):
                xmin=i
        print("L'f(x) più vicino a zero è {} con x = {} ".format(f[xmin],x[xmin]))
    
    def eval(self,x):
        pass


class Retta(Funzione):
    def __init__(self,a,b,m,q):
        super().__init__("Retta",a,b)
        self.m=m
        self.q=q
    
    def nome(self):
        Funzione.nome(self)
        print("La retta è y = {}x + {}\n".format(self.m,self.q))
    
    def eval(self,x):
        return self.m *x + self.q

class Parabola(Funzione):
    def __init__(self,a,b,c0,c1,c2):
        super().__init__("Parabola",a,b)
        self.c0=c0
        self.c1=c1
        self.c2=c2
    
    def nome(self):
        Funzione.nome(self)
        print("La parabola è y  = {}(x^2) + {}x + {}\n".format(self.c0,self.c1,self.c2))
    
    def eval(self,x):
        return self.c0*(x**2)+self.c1*x+self.c2


scelta=float(input("Digita:\n1 per analizzare una retta\n2 per analizzare una parabola\n"))
if (scelta==1):
    retta=Retta(float(input("Inserire range in cui calcolare il valore più vicino a zero\n")),float(input()),float(input("Inserire coefficiente angolare e traslazione dall'origine della retta\n")),float(input()))
    retta.minimo(float(input("Specificare delta x per stabilire la precisione di calcolo\n")))
if (scelta==2):
    parabola=Parabola(float(input("Inserire range in cui calcolare il valore più vicino a zero\n")),float(input()),float(input("Inserire coefficienti c0,c1 e c2\n")),float(input()),float(input()))
    parabola.minimo(float(input("Specificare delta x per stabilire la precisione di calcolo\n")))