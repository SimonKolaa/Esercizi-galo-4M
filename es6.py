class Pagamento:
    def __init__(self, processa_pagamento):
        self.processa_pagamento = processa_pagamento

    def processa_pagamento(self):
        self.processa_pagamento()
        
        class CartaCredito(Pagamento):
            def processa_pagamento(self):
                print("pagamento con carta di credito")
                self.processa_pagamento()
                
                class PayPal(Pagamento):
                    def processa_pagamento(self):
                        print("pagamento con PayPal")
                        self.processa_pagamento()
       class Pagamento:                 
    def Pagamento(self):
        return f'Pagamento: {self.processa_pagamento()}'