import socket
from jogador import Jogador
from jogo import Jogo

dicionarioJogada = {
    0: "Pedra",
    1: "Papel",
    2: "Tesoura",
    3: "Lagarto",
    4: "Spock"
}

def client_program():
    host = socket.gethostname()  
    port = 5000

    client_socket = socket.socket()  
    client_socket.connect((host, port))  

    jogador = Jogador()
    jogo = Jogo()
    contador = 0
    jogadaOponente = 1
    resultadosArray = []

    while contador < 15:
        jogada = jogador.escolheJogada(contador, jogadaOponente)
        jogadaPython = str(jogada) + "\r\n"                         # prepara jogada para ser enviada
        client_socket.send(jogadaPython.encode())                   # envia jogada
        jogadaOponente = int(client_socket.recv(1024).decode()  )   # recebe jogada do oponente e atualiza jogadaOponente

        print("     Partida ", (contador+1), "\n")
        print('Jogada Python: ', dicionarioJogada[jogada])
        print('Jogada Java: ', dicionarioJogada[jogadaOponente], "\n")
        
        resultadoPartida = jogo.verificaPartida(jogada, jogadaOponente)      # verifica vencedor da partida
        resultadosArray.append(resultadoPartida)                             # guarda resultados das partidas

        contador +=1

    print("Resumo:  ", jogo.resumoPartidas(resultadosArray))
  
    client_socket.close()  


if __name__ == '__main__':
    client_program()
