import os

class Film:
    def __init__(self, titolo, regista, anno, genere, valutazione):
        self.titolo = titolo
        self.regista = regista
        self.anno = anno
        self.genere = genere
        self.valutazione = valutazione

class Libreria:
    def __init__(self):
        self.films = []

    def aggiungi_film(self, film):
        self.films.append(film)

    def cerca_film(self, titolo, regista):
        risultati = []
        for film in self.films:
            if titolo and titolo in film.titolo:
                risultati.append(film)
            if regista and regista in film.regista:
                risultati.append(film)

    def visualizza_films(self):
        for film in self.films:
            print(film.titolo, film.regista, film.anno, film.genere, film.valutazione)

    #def valutazione_media(self):       
    # voto = 0
    #for film in self.films:
    #        voto += film.valutazione
    
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    libreria = Libreria()
    while True:
        print('1. Aggiungi film')
        print('2. Cerca film')
        print('3. Visualizza films')
        print('4. Valutazione media')
        print('5. Esci')
        scelta = input('Scelta: ')
        if scelta == '1':
            titolo = input('Titolo: ')
            regista = input('Regista: ')
            anno = input('Anno: ')
            genere = input('Genere: ')
            valutazione = input('Valutazione: ')
            film = Film(titolo, regista, anno, genere, valutazione)
            libreria.aggiungi_film(film)
        elif scelta == '2':
            titolo = input('Titolo:')
            regista = input('Regista:')
            libreria.cerca_film(titolo, regista)





#Gestione di una libreria di film. Ogni film ha un titolo, un regista, un anno di uscita, un genere (azione, commedia, drammatico, horror, documentario) e una valutazione (da 1 a 10). Il sistema deve permettere di:
#Aggiungere nuovi film alla libreria.
#Cercare film per titolo o regista.
#Visualizzare tutti i film presenti nella libreria.
#Calcolare la valutazione media dei film.
#Il sistema deve includere due classi principali:
#: rappresenta un singolo film nella libreria.
#: gestisce i film e le operazioni associate.
