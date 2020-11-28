class Funzione:
    def __init__(self,name,a,b):
        self.name=name
        self.a=a
        self.b=b
        if (self.a>self.b):
            raise Exception("L'inizio dell'inervallo ha un valore superiore alla sua fine\n")
    
    def nome(self):
        print("\nFunzione da ",self.a," a ",self.b,"\n")
    
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
        print("\nCalcolo valore più vicino allo zero")
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
                

class Polinomio(Funzione):
    def __init__(self,a,b,n,coeff):
        super().__init__("Polinomio",a,b)
        #Un polinomio di grado n avrà n+1 coefficienti
        self.n=n+1
        if (self.n<=0):
            raise Exception("Il grado deve essere maggiore di 0\n")
        #Creo una lista con i cofficienti
        self.coeff=coeff
    def specifica(self):
        #La traslazione dall'origine la metto esternamente per belvedere
        self.coeff[0]=float(input("Inserire la traslazione dall'origine\n"))
        for i in range(1,self.n):
            #Assegno ad ogni casella assegno un coefficiente, seguendo un ordine di grado crescente
            print("Inserire il coefficiente angolare di x^{}".format(i))
            self.coeff.append(float(input()))
    def nome(self):
        Funzione.nome(self)
        #Esplicito la funzione generata dall'utente
        print("Il polinomio è y = {}".format(self.coeff[0]),end=" ")
        for i in range(1,self.n):
            print("+ {}(x^{})".format(self.coeff[i],i),end=" ")
        print("\n")
    def eval(self,x):
        somm=0
        #Per ogni x il risultato della funzione sarà la somma di ogni termine del polinomio, quindi uso un ciclo per calcolarli tutti e assegnarli ad un unica variabile da ritornare
        for i in range(self.n):
            somm=somm + (self.coeff[i]*(x**i))
        return somm


class Integrale(Polinomio):
    def __init__(self,a,b,n,coeff):
        super().__init__(a,b,n,coeff)
    
    def IntervalEval(self,x,dx):
        if (x<float(self.a)):
            print("La x scelta è fuori dall'intervallo\n")
            print(0)
        else:
            if (x>float(self.b)):
                print("La x scelta è fuori dall'intervallo\nCalcolo area sottesa in intervallo originale\n")
                x=self.b
            i=self.a
            area=[]
            while(i<x):
                fx = Polinomio.eval(self,i)
                area.append(fx*dx)
                i += dx
            print("L'area sottesa dalla curva nell'intervallo da {} a {} equivale a {}".format(self.a,x,sum(area)))


#Faccio inserire all'utente il range in cui calcolare la funzione, il grado del polinomio e la quantità di valori calcolati
calcolo=Integrale(float(input("Inserire range in cui eseguire i calcoli\n")),float(input()),int(input("Di che grado sarà il polinomio?\n")),[0])
calcolo.specifica()
scelta=int(input("Seleziona: \n1 per calcolare il valore più vicino a 0 di un polinomio\n2 per calcolare l'area sottesa dal polinomio\n"))
if (scelta==1):
    calcoo.minimo(float(input("Specificare delta x per stabilire la precisione di calcolo\n")))
else:
    calcolo.IntervalEval(float(input("Fino a che valore vuoi calcolare l'area?\n")),float(input("Con quale densità di calcolo?\n")))
