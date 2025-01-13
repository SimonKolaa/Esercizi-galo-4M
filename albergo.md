```mermaid
Class Camera:
- numero: int
- tipo: str
- disponibilità: bool
+ __init__(numero: int, tipo: str, disponibilità: bool)

Class Albergo:
- camere: list
- prenotazioni: list
+ __init__(camere: list, prenotazioni: list)
+ aggiungi_camera(camera: Camera)
+ prenota_camera(numero: int)
+ camere_disponibili(): list
```

Albergo 1-* Camera: contiene
Albergo 1-* Prenotazione: può contenere



 