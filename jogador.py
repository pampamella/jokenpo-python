
class Jogador:
    def __init__(self):
        self.primeiraJogada = 0
    
    def escolheJogada(self, contador, oponenteAnterior=1):
        if(contador == 0):
            return self.primeiraJogada
        else:
            return int(oponenteAnterior)
        
