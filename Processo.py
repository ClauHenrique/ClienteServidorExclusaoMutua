import random
import time


class Processo:
    def __init__(self, conta, saldo):
        self.conta = conta
        self.saldo = saldo
        self.processo_ativo = False
        self.fila_processos = []
        self.id_processo_ativo = 0

    def sacar_valor(self, valor, id_processo):
        #   remover esse processo da fila
        del self.fila_processos[0]

        self.id_processo_ativo = id_processo

        self.processo_ativo = True

        print(f"processo id: {id_processo} -> {self.processo_ativo}")
        print("consumindo recurso...")

        # algumas dessas informacoes ao invez de printar
        # serão mandadas para o cliente conexao.send()
        self.saldo -= valor
        print(">>> o saldo é: ", self.saldo)
        time.sleep(5)

        self.processo_ativo = False
        print(f"processo {id_processo} -> {self.processo_ativo}")
        print(f"_____o processo id: {id_processo} ja terminou_______\n\n")

    # funcao usada para criar um processo e gerar um id para ele
    def solicita_recurso(self, valor_saque):
        id_processo = random.randint(1, 100)

        print(f"\no processo id: {id_processo} solicita ser executado\n")

        self.fila_processos.append({"id": id_processo, "valor_saque": valor_saque})

    def get_saldo(self):
        return self.saldo

    def get_fila(self):
        return self.fila_processos

    # regiao critica
    # o processo so consome recurso se a variavel estiver disponivel para isso
    # no nosso caso, o processo so é executado se tivermos saldo o suficiente
    def cordenador(self, valor_saque):
        repetir_msg = 0

        # # o primeiro passo é chamar a funcao de solicita_recurso para inserir um processo na fila
        self.solicita_recurso(valor_saque)

        while len(self.fila_processos) > 0:
            try:
                time.sleep(1)
                if self.processo_ativo != True:

                    # se o valor saque do processo da vez que esta na fila, nao deixar o saldo em negativo,
                    # entao podemos proseguir
                    valor_saque_fila = self.fila_processos[0]["valor_saque"]
                    if self.saldo - valor_saque_fila >= 0:

                        # a funcao sacar_valor sempre pega o id e o valor_saque
                        # do elemento da vez o primeiro elemento da fila
                        pegar_valor_saque_fila_processo = self.fila_processos[0]["valor_saque"]
                        pegar_id_processo_fila_processo = self.fila_processos[0]["id"]

                        self.sacar_valor(pegar_valor_saque_fila_processo, pegar_id_processo_fila_processo)
                        time.sleep(2)
                        repetir_msg = 0

                    else:
                        print("\nsaldo insuficiente!\na operacao não pode ser realizada pelo processo!\n")
                        #   remover esse processo da fila
                        del self.fila_processos[0]
                        break

                else:
                    # essa msg deve aparecer apenas uma vez para cada processo barrado
                    if repetir_msg == 0:
                        print(f'\nprocesso id: {self.id_processo_ativo} esta realizando uma operacao!!!!!')
                        print("aguardando liberacao...\n")
                        repetir_msg = 1

            except:
                print("erro inesperado")

