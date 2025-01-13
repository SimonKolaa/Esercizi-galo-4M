class Camera:
    def __init__(self, numero, prezzo, prenotata):
        self.numero = numero
        self.prezzo = prezzo
        self.prenotata = prenotata

class Albergo:
    def __init__(self):
        self.camere = []
    def aggiungi_camera(self, camera):
        self.camere.append(camera)

    def prenota_camera(self, numero):
        for camera in self.camere:
            if camera.numero == numero:
                if camera.prenotata:
                    print("camera non disponibile")
                else:
                    camera.prenotata = True
                    print("prenotazione effettuata")
                return
        print("camera non trovata")

    def camere_disponibili(self):
        for camera in self.camere:
            if not camera.prenotata:
                print(f"camera {camera.numero} - {camera.prezzo}€")

    def prenotazioni_effettuate(self):
        for camera in self.camere:
            if camera.prenotata:
                print(f"camera {camera.numero} - {camera.prezzo}€")
