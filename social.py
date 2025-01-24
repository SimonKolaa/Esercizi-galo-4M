class Utente:
    def __init__(self, nome_utente: str, email: str, password: str, profilo: str):
        self.nome_utente = nome_utente
        self.email = email 
        self.password = password
        self.profilo = profilo

    def get_nome_utente(self) -> str:
        return self.nome_utente

    def get_email(self) -> str:
        return self.email

    def get_password(self) -> str:
        return self.password

    def get_profilo(self) -> str:
        return self.profilo

    def get_dettagli(self):
        return {
            "nome_utente": self.nome_utente,
            "email": self.email,
            "profilo": self.profilo
        }

    def aggiorna_profilo(self, profilo: str):
        self.profilo = profilo

class Foto:
    def __init__(self, ID: str, titolo: str, descrizione: str, data_caricamento: str, utente: str, album: str):
        self.ID = ID
        self.titolo = titolo
        self.descrizione = descrizione
        self.data_caricamento = data_caricamento
        self.utente = utente
        self.album = album

    def get_ID(self) -> str:
        return self.ID

    def get_titolo(self) -> str:
        return self.titolo

    def get_descrizione(self) -> str:
        return self.descrizione

    def get_data_caricamento(self) -> str:
        return self.data_caricamento

    def get_utente(self) -> str:
        return self.utente

    def get_album(self) -> str:
        return self.album

    def get_dettagli(self):
        return {
            "ID": self.ID,
            "titolo": self.titolo,
            "descrizione": self.descrizione,
            "data_caricamento": self.data_caricamento,
            "utente": self.utente,
            "album": self.album
        }

    def aggiorna_foto(self, titolo: str, descrizione: str):
        self.titolo = titolo
        self.descrizione = descrizione

class Album:
    def __init__(self, titolo: str, descrizione: str, utente: str, foto: list):
        self.titolo = titolo
        self.descrizione = descrizione
        self.utente = utente
        self.foto = foto

    def get_titolo(self) -> str:
        return self.titolo

    def get_descrizione(self) -> str:
        return self.descrizione

    def get_utente(self) -> str:
        return self.utente

    def get_foto(self) -> list:
        return self.foto

    def get_dettagli(self):
        return {
            "titolo": self.titolo,
            "descrizione": self.descrizione,
            "utente": self.utente,
            "foto": self.foto
        }

    def aggiorna_album(self, titolo: str, descrizione: str):
        self.titolo = titolo
        self.descrizione = descrizione

if __name__ == "__main__":
    utente = Utente("user1", "user1@email.com", "password123", "profile1")
    album = Album("Album1", "My first album", utente.get_nome_utente(), [])
    foto = Foto("1", "First photo", "My description", "2024-03-14", utente.get_nome_utente(), album.get_titolo())