#Apro il file
file_origin=open("Shampoo.txt","r")
#Leggo il contenuto
file=file_origin.readlines()
#Inizializzo la lista dove metterò i valori
valori=[]
#Lehho il file linea per linea
for linea in file:
    elemento=linea.split(',')
    #Sommo solo se i dati hanno valore effettivo
    if elemento[0]!='Date':
        #Separo data e numero
        data=elemento[0]
        numero=elemento[1]
        #Assegno i valori ad un array
        valori.append(float(numero))
#Stampo i valori e la loro somma
print(valori)
print(sum(valori))