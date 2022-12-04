import numpy as np

class Jogo:
    def __init__(self):
        self.matrizRecompensa = np.array([
                                [0, -1, 1, 1, -1], 
                                [1, 0, -1, -1, 1],
                                [-1, 1, 0, 1, -1],
                                [-1, 1, -1, 0, 1],
                                [1, -1, 1, -1, 0]])
    
    def verificaPartida(self, jogadaPython, jogadaJava):
        valor = self.matrizRecompensa[jogadaPython][jogadaJava]
        if valor < 0: 
            print('Vitória do Java \n\n')
            return "Java Vencedor"
        elif valor > 0: 
            print('Vitória do Python \n\n') 
            return "Python Vencedor"
        else: 
            print('Empate! \n\n')
            return "Empate"
        
    def resumoPartidas(self, resultadosArray):
        dicionario = {i:resultadosArray.count(i) for i in resultadosArray}
        return dicionario