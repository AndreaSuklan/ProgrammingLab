
class CSVFile:
    #Dichiaro variabile nome
    def __init__(self,name):
        self.name=name
    #Dichiaro funzione
    def get_data(self):
        #Apro il file di testo
        file_origin=open(self.name,"r")
        #Creo Array valori
        valori=[]
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
                valori.append(float(numero))
        #Stampo i valori e la loro somma
        print(valori)
#Assegno la variabile
lol=CSVFile("Shampoo.txt")
#Stampo l'elenco
lol.get_data()