class Viaggio:
    def __init__(self,nome_viaggio,data_partenza,data_ritorno,localita,resort,prezzo,partecipanti,responsabile_viaggio):
        self.nome_viaggio=nome_viaggio
        self.data_partenza=data_partenza
        self.data_ritorno=data_ritorno
        self.localita=localita
        self.resort=resort
        self.prezzo=prezzo
        self.partecipanti=partecipanti
        self.responsabile_viaggio=responsabile_viaggio
    def __str__(self):
        return "Il viaggio {} con partenza il {} e ritorno il {} verso {} nel resort {} al prezzo di {} a cui partecipano {} sotto la supervisione di {}".format(self.nome_viaggio,self.data_partenza,self.data_ritorno,self.localita,self.resort,self.prezzo,self.partecipanti,self.responsabile_viaggio)
    def guadagno(self):
        print(float(self.prezzo)*0.57)

class Invernale(Viaggio):
    def __init__(self,nome_viaggio,data_partenza,data_ritorno,localita,resort,prezzo,partecipanti,responsabile_viaggio,skipass,impianti_sciistici):
        super().__init__(nome_viaggio,data_partenza,data_ritorno,localita,resort,prezzo,partecipanti,responsabile_viaggio)
        self.skipass=skipass
        self.impianti1_sciistici=impianti_sciistici
    def __str__(self):
        return "Il viaggio {} con partenza il {} e ritorno il {} verso {} nel resort {} al prezzo di {} a cui partecipano {} sotto la supervisione di {} con lo skipass di prezzo{} all'impianto {}".format(self.nome_viaggio,self.data_partenza,self.data_ritorno,self.localita,self.resort,self.prezzo,self.partecipanti,self.responsabile_viaggio,self.skipass,self.impianti1_sciistici)

class Estiva(Viaggio):
    def __init__(self,nome_viaggio,data_partenza,data_ritorno,localita,resort,prezzo,partecipanti,responsabile_viaggio,distanza,escursioni_marine):
        super().__init__(nome_viaggio,data_partenza,data_ritorno,localita,resort,prezzo,partecipanti,responsabile_viaggio)
        self.distanza=distanza
        self.escursioni_marine=escursioni_marine
    def __str__(self):
        return "Il viaggio {} con partenza il {} e ritorno il {} verso {} nel resort {} al prezzo di {} a cui partecipano {} sotto la supervisione di {} ad una distanza {} dal mare  facenti {} escursioni marine".format(self.nome_viaggio,self.data_partenza,self.data_ritorno,self.localita,self.resort,self.prezzo,self.partecipanti,self.responsabile_viaggio,self.distanza,self.escursioni_marine)

maldive=Viaggio(input(),input(),input(),input(),input(),input(),input(),input())
print(maldive)
maldive.guadagno()