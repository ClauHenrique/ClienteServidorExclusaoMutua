import socket

def start(cliente):
    try:
        cliente.connect(("localhost", 5052))
        try:
            parar = False
            while parar == False:

                conta_cliente = str(input("digite a sua conta: "))

                valor_saque = str(input("digite o valor do saque: "))

                if valor_saque.isnumeric():

                    listaValores = conta_cliente + " " + valor_saque

                    cliente.send(listaValores.encode())

                    data = cliente.recv(1024)

                    # so fechamos a conexão se tivermos alguma resposta do servidor
                    if len(data.decode()) > 0:
                        print(f"o resultado e: \n{data.decode()}")
                        cliente.close()
                        parar = True

                else:
                    print("Valores invalidos\ndigite apenas valores inteiros!\ndigite outro valor")
        except:
            return print("erro ao se conectar ao servidor")

    except:
        return print("erro ao se conectar ao servidor")


cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
start(cliente)

