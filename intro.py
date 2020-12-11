
class CSVFile:
    #Dichiaro variabile nome
    def __init__(self,name,valori):
        self.name=name
        self.valori=valori
    #Dichiaro funzione
    def get_data(self):
        #Apro il file di testo
        file_origin=open(self.name,"r")
        #Creo Array valori
        self.valori=[]
        #Leggo le linee del testo
        file=file_origin.readlines()
        #Comincio a leggere i valori
        for linea in file:
            elemento=linea.split(',')
            #Sommo solo se i dati hanno valore effettivo
            if elemento[0]!='Date':
                 #Separo data e numero
                numero=elemento[1]
                #Assegno i valori ad un array
                self.valori.append(float(numero))
        #Stampo i valori e la loro somma
        print(self.valori)
    def predict(self,volte):
        self.get_data()
        print("\n")
        som=0
        i=1
        n=0
        while (n<volte):
            while (i < (len(self.valori))):
                som += (self.valori[i]-self.valori[i-1])
                i += 1
            som=som/(len(self.valori)-1)
            self.valori.append(self.valori[-1]+som)
            n += 1
            i=1
            som=0
        print(self.valori)
        return self.valori
    def fit(self):
        self.get_data()
        i=1
        som=0
        while (i < (len(self.valori))):
            som += (self.valori[i]-self.valori[i-1])
            i += 1
        print("\n L'incremento medio è: ",som/(len(self.valori)-1))
        return som/(len(self.valori)-1)

#Assegno la variabile
lol=CSVFile("Shampoo.txt",0)
#Stampo l'elenco
lol.fit()
lol.predict(1)
