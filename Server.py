import socket
import threading
import time

from Processo import Processo


# funcao que rebe o valor do saque
# e chamar a funcao que inicia o processo de realizar saque
def recev_conta_valor_saque(conexao, conta_bancaria):
    # daqui para baixo, encapsular em uma funcao
    conta_valor = conexao.recv(1024).decode()
    print(">>", conta_valor)

    time.sleep(4)
    send_valor_saldo(conexao, conta_bancaria, conta_valor)


def send_valor_saldo(conexao, conta_bancaria, conta_valor):
    # transformar a string em uma lista com a conta como 1 valor e o valor_saque como 2 valor
    listaVal = conta_valor.split()

    # se o valor do saque for um valor numerico
    if listaVal[1].isnumeric():

        conta = listaVal[0]
        valor_saque = int(listaVal[1])

        # realizar o saque e retornar o saldo
        conta_bancaria.cordenador(valor_saque)

        # dar o send()
        txt = str(conta)
        saldo = str(f"{txt} seu saldo: {conta_bancaria.get_saldo()}")
        conexao.send(saldo.encode())

        print('fechado')
        conexao.close()

    else:
        a = "Valores invalidos!"
        print(a)
        conexao.send(a.encode())



def start(server):
    try:
        server.bind(('localhost', 5052))
        server.listen()

        print("servidor iniciado!")
        print("\naguardando uma conexão..")

    except:
        return print("""
        erro ao iniciar o servidor...
        a conexão ainda nao foi feixada pela sua maquina 
        aguarde um momento e tente denovo""")


    conta_bancaria = Processo('clau123', 1000)

    while True:
        try:
            # aceita a conexão
            conexao, endereco = server.accept()
            print(f"\nconectado a {endereco}")

            thread = threading.Thread(target=recev_conta_valor_saque, args=[conexao, conta_bancaria])
            thread.start()

        except:
            return print("Erro ao se conectar com o cliente")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

start(server)

