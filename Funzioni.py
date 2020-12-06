import matplotlib.pyplot as plt
from math import e
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
        #plt.plot(x,f)
        #plt.show()
    #Metto il calcolo dell'integrale direttamente dentro la classe funzione in modo da renderlo generale
    def integrale(self,dx):
        print("\nCalcolo l'area sottesa:\n")
        self.nome()
        x=self.b
        i=self.a
        area=[]
        y=[]
        xo=[]
        while(i<x):
            fx=self.eval(i)
            y.append(self.eval(i))
            xo.append(i)
            area.append(fx*dx)
            i += dx
        print("L'area sottesa dalla curva nell'intervallo da {} a {} equivale a {}".format(self.a,x,sum(area)))
        #plt.plot(xo,y)
        #plt.show()
    
    def eval(self,x):
        pass

    def __iter__(self):
        #Richiedo la densità di calcolo dell'integrale
        self.dx = float(input("Decidere densità calcolo\n"))
        #Voglio restituire la sommatoria parziale del calcolo
        self.som = 0
        return self

    def __next__(self):
        #Blocco l'terzaione se si esce dall'intervallo della funzione originaria
        if ((self.a) >= self.b):
            print("Il valore dell'integrale è stato calcolate per inter all'interno dell'intervallo scelto\n")
            raise StopIteration
        else:
            #Parto dal primo punto dell'intervallo
            x = self.a
            #Ed aggiungo ogni volta la differenza fra i valori di x
            self.a += self.dx
            #Ne calcolo l'area e la salvo nella somma parziale
            self.som += self.eval(x)*self.dx
            #Riporto la somma
            return self.som
                
class Esponenziale(Funzione):
    def __init__(self,a,b,base):
        super().__init__("Esponenziale",a,b)
        self.base=base
    
    def nome(self):
        print("La funzione è y = {}^x\n".format(self.base))

    def eval(self,x):
        return self.base**x


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

'''
#Faccio inserire all'utente il range in cui calcolare la funzione, il grado del polinomio e la quantità di valori calcolati
if (int(input("Seleziona:\n 1 se si vuole analizzare un polinomio\n 2 se si vuole analizzare un esponenziale\n"))==1):
    calcolo=Polinomio(float(input("Inserire range in cui eseguire i calcoli\n")),float(input()),int(input("Di che grado sarà il polinomio?\n")),[0])
    calcolo.specifica()
    scelta=int(input("Seleziona: \n1 per calcolare il valore più vicino a 0 di un polinomio\n2 per calcolare l'area sottesa dal polinomio\n"))
    if (scelta==1):
        calcolo.minimo(float(input("Specificare delta x per stabilire la precisione di calcolo\n")))
    else:
        calcolo.Integrale(float(input("Con quale densità di calcolo vuoi individuare l'area sottesa dalla curva?\n")))
else:
    o=Esponenziale(float(input("Inserire range in cui eseguire i calcoli\n")),float(input()),float(input("Inserire base esponenziale\n")))
    if (int(input("Seleziona: \n 1 per calcolare il valore più vicino a 0 della funzione\n 2 per calcolare l'area sottesa dala funzione\n"))==1):
        o.minimo(float(input("Specificare delta x per stabilire la precisione di calcolo\n")))
    else:
        o.integrale(float(input("Specificare delta x per stabilire la precisione di calcolo\n")))
'''

fun=Esponenziale(-2,2,2)
fun=iter(fun)
for i in range(6):
    print(next(fun))