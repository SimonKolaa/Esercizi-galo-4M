class Persona:
    def __init__(self, nome, citta, eta):
        self.nome = nome
        self.citta = citta
        self.eta = eta

    def descrizione(self):
        print(f"{self.nome} ha {self.eta} anni e abita a {self.citta}.")

    def saluta(self):
        print(f"Ciao, mi chiamo {self.nome}.")


Persona1 = Persona("Dario", "San Giovanni in Marignano", 26)
Persona1.descrizione()
Persona1.saluta()