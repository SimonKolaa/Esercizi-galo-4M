class Dipendente:
    def __init__(self, nome, stipendio):
        self.nome = nome
        self.stipendio = stipendio

class Manager(Dipendente):
    def __init__(self, nome, stipendio, numero_di_team):
        super().__init__(nome, stipendio)
        self.numero_dipendenti = numero_di_team
  
class Sviluppatore(Dipendente):
    def __init__(self, nome, stipendio, linguaggio_di_programmazione):
        super().__init__(nome, stipendio)
        self.linguaggio = linguaggio_di_programmazione