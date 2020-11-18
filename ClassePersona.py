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
        print('> Docente del corso(i):', self.corso,"\n")
pass
#Definisco sottoclasse Tecnico
class TecnicoAmministrativo(Persona):
    def __init__(self,nome,cognome,age,edificio):
        super().__init__('Tecnico UNITS:',nome,cognome,age)
        self.edificio=edificio
    def bonjour(self):
        Persona.bonjour(self)
        print("> Tecnico dell(gli)'edificio(i): ",self.edificio,"\n")
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
        print('> Studente del corso(i):', self.corso,"\n")
pass
Gianni=Docente("Gianni","Micheli",37,["Informatica","Analisi","Laboratorio"])
Gianni.bonjour()
Giorgio=Docente("Giorgio","Milano",57,["Latino","Analisi","Laboratorio"])
Giorgio.bonjour()
Marco=TecnicoAmministrativo("Marco","Maraldo",30,["H3","C9"])
Marco.bonjour()
Poco=Studente("Poco","Furbo",57,["Informatica","Analisi","Latino"])
Poco.bonjour()