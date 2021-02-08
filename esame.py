class ExamException(Exception):
    pass

class CSVTimeSeriesFile:
    #Dichiaro variabile nome
    def __init__(self,name):
        self.name=name
    #Dichiaro funzione
    def get_data(self):
        #Apro il file di testo
        try:
            file_origin=open(self.name,"r")
        except:
            raise ExamException("Errore, lista non leggibile")
        #Creo lista valori
        valori=[]
        #Leggo le linee del testo
        file=file_origin.readlines()
        #Comincio a leggere i valori
        for linea in file:
            elemento=linea.split(',')
            #Assegno solo se i dati hanno valore effettivo
            #Separo epoch e temperatura
            try :
                epoch = int(float(elemento[0]))
                if (epoch < 0):
                    continue
                temperatura=float(elemento[1])
            except:
                continue
            #Assegno i valori ad un array
            valori.append([epoch,temperatura])
        # Conrollo che gli epoch siano ordinati
        for i in range(len(valori)):
            for j in range(i+1,len(valori)):
                if (valori[i][0] >= valori[j][0]):
                    raise ExamException("Errore, lista valori temporali non ordinata o con duplicati")
        return valori

def daily_stats(time_series):
    stats=[]
    k=0
    # Escludo i valori nulli
    while (k < len(time_series)):
        if (time_series[k][1] == None or time_series[k][0] == None):
            k = k+1
        else:
            # Inizializzo l'inizio e la fine del giorno
            inizio = time_series[k][0] - (time_series[k][0] % 86400)
            fine = inizio + 86400
            # Azzero la sommatoria ed il contatore per la media
            som = 0
            count = 0
            # Inizializzo massimo e minimo per il conronto in seguito
            mino=time_series[k][1]
            mass=time_series[k][1]
            # Suddivido i vari giorni per calcolarene i valori
            while (k < len(time_series) and time_series[k][0] < fine):
                if (time_series[k][1]<mino):
                    mino=time_series[k][1]
                if (time_series[k][1]>mass):
                    mass=time_series[k][1]
                som += time_series[k][1]
                count += 1
                k = k+1
            som = som/count
            # Creo una lista con i dati da inserire in quella finale
            var=[mino,mass,som]
            stats.append(var)
    return stats


time_series_file=CSVTimeSeriesFile(name="data.csv")
time_series=time_series_file.get_data()
"""for i in range(len(time_series)):
    print(time_series[i],"\n")"""
stats=daily_stats(time_series)
for i in range(len(stats)):
    print(stats[i],"\n")
print(len(stats))