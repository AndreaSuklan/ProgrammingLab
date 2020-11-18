#Definisco la classe Persona
class Persona:
    #Inizializzo le variabili(Attributi)
    def __init__(self,ruolo,nome,cognome,age,):
        self.ruolo=ruolo
        self.nome=nome
        self.cognome=cognome
        self.age=age
    #Definisco le funzioni interne(Metodi)
    def bonjour(self):
        if (self.ruolo == 'Docente UNITS' and self.age > 40):
            print(self.ruolo,':',self.nome,self.cognome,"(anni >40)",)
        else:
            print(self.ruolo,':',self.nome,self.cognome,'(anni {})'.format(self.age))
pass
#Definisco sottoclasse Docente
class Docente(Persona):
    def __init__(self, nome, cognome,age,corso):
        #Posso utilizzare i dati della superclasse Persona
        super().__init__('Docente UNITS', nome, cognome,age)
        self.corso=corso
    def bonjour(self): 
        #Anche le sue funzioni
        Persona.bonjour(self)
        for i in range(len(self.corso)):
            print('> Docente del corso:', self.corso[i])
        print("\n")
pass
#Definisco sottoclasse Tecnico
class TecnicoAmministrativo(Persona):
    def __init__(self,nome,cognome,age,edificio):
        super().__init__('Tecnico UNITS:',nome,cognome,age)
        self.edificio=edificio
    def bonjour(self):
        Persona.bonjour(self)
        for i in range(len(self.edificio)):
            print("> Tecnico dell'edificio: ", self.edificio[i])
        print("\n")
pass
#Definisco sottoclasse Studente
class Studente(Persona):
    def __init__(self, nome, cognome,age,corso):
        #Posso utilizzare i dati della superclasse Persona
        super().__init__('Studente UNITS', nome, cognome,age)
        self.corso=corso
    def bonjour(self): 
        #Anche le sue funzioni
        Persona.bonjour(self)
        for i in range(len(self.corso)):
            print('> Studente del corso:', self.corso[i])
        print("\n")
pass
#Definisco la funzione
def docente_copre_studente(docente,studente):
    k=0
    #Un pò di interfaccia utente
    print("\nProfessore che esamino\n")
    print("---------o-------\n")
    docente.bonjour()
    print("---------o-------\n")
    print("Studente che esamino\n")
    studente.bonjour()
    print("---------o-------\n")
    print("Ricerca in corso...\n")
    print("---------o-------\n")
    for i in range(len(docente.corso)):
        for j in range(len(studente.corso)):
            if (docente.corso[i] == studente.corso[j]):
                print(docente.corso[i],"== Vero\n")
                k=k+1
    print("---------o-------\n")
    if (k == len(studente.corso)):
        print("Il professore {} {} copre tutti i corsi di {} {}\n".format(docente.nome,docente.cognome,studente.nome,studente.cognome))
    else:
        print("Il professore {} {} non copre tutti i corsi di {} {}\n".format(docente.nome,docente.cognome,studente.nome,studente.cognome))
    print("---------o-------\n")
pass

Gianni=Docente("Gianni","Micheli",37,["Informatica","Analisi","Laboratorio"])
Lollo=Docente("Lollo","Pollo",12,["Informatica","Analisi","Latino"])
Giorgio=Docente("Giorgio","Milano",57,["Latino","Analisi","Laboratorio"])
Marco=TecnicoAmministrativo("Marco","Maraldo",30,["H3","C9"])
Poco=Studente("Poco","Furbo",57,["Informatica","Analisi","Latino"])
docente_copre_studente(Gianni,Poco)
docente_copre_studente(Lollo,Poco)
