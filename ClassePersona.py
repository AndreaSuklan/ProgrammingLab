#Definisco la classe Persona
class Persona:
    #Inizializzo le variabili(Attributi)
    def __init__(self,ruolo,nome,cognome):
        self.ruolo=ruolo
        self.nome=nome
        self.cognome=cognome
    #Definisco le funzioni interne(Metodi)
    def bonjour(self):
        print(self.ruolo,': ',self.nome,self.cognome)
pass
#Definisco sottoclasse Docente
class Docente(Persona):
    def __init__(self, nome, cognome, corso):
        #Posso utilizzare i dati della superclasse Persona
        super().__init__('Docente UNITS', nome, cognome)
        self.corso=corso
    def bonjour(self): 
        #Anche le sue funzioni
        Persona.bonjour(self) 
        print('> Docente del corso(i):', self.corso,"\n")
pass
#Definisco sottoclasse Tecnico
class TecnicoAmministrativo(Persona):
    def __init__(self,nome,cognome,edificio):
        super().__init__('Tecnico UNITS:',nome,cognome)
        self.edificio=edificio
    def bonjour(self):
        Persona.bonjour(self)
        print("> Tecnico dell(gli)'edificio(i): ",self.edificio,"\n")
pass
#Definisco sottoclasse Studente
class Studente(Persona):
    def __init__(self, nome, cognome, corso):
        #Posso utilizzare i dati della superclasse Persona
        super().__init__('Studente UNITS', nome, cognome)
        self.corso=corso
    def bonjour(self): 
        #Anche le sue funzioni
        Persona.bonjour(self)
        print('> Studente del corso(i):', self.corso,"\n")
pass
Gianni=Docente("Gianni","Micheli",["Informatica","Analisi","Laboratorio"])
Gianni.bonjour()
Marco=TecnicoAmministrativo("Marco","Maraldo",["H3","C9"])
Marco.bonjour()
Poco=Studente("Poco","Furbo",["Informatica","Analisi","Latino"])
Poco.bonjour()