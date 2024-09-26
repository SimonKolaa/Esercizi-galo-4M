class Veicolo:
    # Attributo di classe
    numero_veicoli = 0
    
    def __init__(self, tipo, marca):
        self.tipo = tipo
        self.marca = marca
        # incrementa il numero di veicoli ogni volta che viene creato un nuovo oggetto
        Veicolo.numero_veicoli += 1

    def get_numero_veicoli():
        return Veicolo.numero_veicoli

print(Veicolo.get_numero_veicoli())
auto1 = Veicolo("Auto", "Toyota")
auto2 = Veicolo("Moto", "Honda")
print(Veicolo.get_numero_veicoli())