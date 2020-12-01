from datetime import datetime
class Mod:
    
    def fit(self,data):
        pass
    
    def predict(self,data):
        pass

def stampa(a):
    print("I valori sono:\n",a,"\n")

def statistiche(a):
    print("La sommatoria equivale a:",sum(a))
    #La media è la sommatoria fratto la lunghezza
    print("\nLa media equivale a:",sum(a)/len(a))
    #Uso le funzioni di python
    print("\nIl valore minimo equivale a {} mentre il massimo equivale a {}".format(min(a),max(a)))

def somma_vettoriale(a,b):
    if (len(a)!=len(b)):
        print("Le 2 liste hanno dimensioni diverse\n")
    else:
        for i in range(len(a)):
            a[i]=a[i]+b[i]
        print("\nI valori della somma vettoriale sono:\n",a,"\n")

def prodotto_vettoriale(a,b):
    if (type(a)==list and type(b)==list and len(a)==len(b)):
        for i in range(len(a)):
            a[i]=a[i]*b[i]
        print("\nI valori del prodotto vettoriale sono:\n",a,"\n")
    else:
        print("ATTENZIONE: non sono riuscito a calcolare il prodotto vettoriale\n")
class Inc(Mod):
    def fit(self,data):
        raise Exception("Questo modello non provede un fit\n")

    def predict(self,prev_months,volte):
        som=0
        i=1
        while (i < (len(prev_months))):
            som += (prev_months[i]-prev_months[i-1])
            i += 1
        som=som/(len(prev_months)-1)
        n=0
        while (n<volte):
            prev_months.append(prev_months[-1]+som)
            n += 1
        return prev_months


#Apro il file
file_origin=open("Shampoo.txt","r")
#Leggo il contenuto
file=file_origin.readlines()
#Inizializzo la lista dove metterò i valori
valori=[]
tempo=[]
i=1
#Leggo il file linea per linea
for linea in file:
    elemento=linea.split(',')
        #Sommo solo se i dati hanno valore effettivo
    if (elemento[0]!='Date'):
        #Separo data e numero
        data=elemento[0]
        numero=elemento[1]
        #Assegno i valori ad un array
        try:
            valori.append(float(numero))
        except TypeError:
            print("La riga {} non contiene valori numerici ma {}".format(i,linea))
    i=i+1
pok=[]
for i in range(len(valori)):
    pok.append(int(1))

#Stampo i valori richiesti
stampa(valori)
statistiche(valori)
somma_vettoriale(valori,pok)
prodotto_vettoriale(valori,pok)
fun=Inc()
print(fun.predict(valori,3))