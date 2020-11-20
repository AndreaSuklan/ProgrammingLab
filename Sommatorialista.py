#Apro il file
file_origin=open("Shampoo.txt","r")
#Leggo il contenuto
file=file_origin.readlines()
#Inizializzo la lista dove metterò i valori
valori=[]
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
        except:
            print("La riga {} contiene un errore sconosciuto; ovvero {}".format(i,linea))
    i=i+1

#Stampo i valori e la loro somma
print("I valori sono:\n",valori,"\n")
print("La sommatoria equivale a ",sum(valori))