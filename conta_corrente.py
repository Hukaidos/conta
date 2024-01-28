from datetime import datetime

class Conta:
    def __init__(self, nome, numero_conta, agencia, saldo_inicial=0.0):
        self.dados_conta = {
            'nome': nome,
            'numero_conta': numero_conta,
            'agencia': agencia,
            'saldo': saldo_inicial,
            'data_criacao': datetime.now()
        }

    def depositar(self, quantia):
        if quantia > 0:
            self.dados_conta['saldo'] += quantia
            print(f"Depósito de R${quantia:.2f} realizado com sucesso.")
        else:
            print("Quantia inválida para depósito.")

    def sacar(self, quantia):
        taxa_operacao = 0.5  # Taxa de operação de 0,5%

        if quantia > 0 and self.dados_conta['saldo'] >= (quantia + quantia * taxa_operacao):
            self.dados_conta['saldo'] -= (quantia + quantia * taxa_operacao)
            print(f"Saque de R${quantia:.2f} realizado com sucesso.")
        else:
            print("Quantia inválida para saque.")

    def ver_saldo(self):
        print(f"Saldo atual: R${self.dados_conta['saldo']:.2f}")

    def mostrar_informacoes_pessoais(self):
        print("\nInformações da Conta:")
        for chave, valor in self.dados_conta.items():
            print(f"{chave.capitalize()}: {valor}")
        print()

conta_usuario = None 

while True:
    print('''
========================================
            Banco online
========================================
(1) - Cadastrar sua conta
(2) - Depositar
(3) - Sacar
(4) - Ver Saldo
(5) - Mostrar informações pessoais.
(0) - Sair
    ''')
    
    escolha = int(input("Digite uma opção: "))

    if escolha == 0:
        break
    elif escolha == 1:
        nome_usuario = str(input("Digite seu nome: "))
        numero_conta_usuario = int(input("Digite o número da conta: "))
        agencia_usuario = int(input("Digite a agência: "))
        saldo_inicial_usuario = float(input("Digite o saldo inicial: "))

        conta_usuario = Conta(nome=nome_usuario, numero_conta=numero_conta_usuario, agencia=agencia_usuario, saldo_inicial=saldo_inicial_usuario)

        print("Conta cadastrada com sucesso\n")
    elif escolha == 2:
        if conta_usuario:
            quantia = float(input("Digite o valor para depósito: "))
            conta_usuario.depositar(quantia)
        else:
            print("Por favor, crie uma conta primeiro.\n")
    elif escolha == 3:
        if conta_usuario:
            quantia = float(input("Digite o valor para saque: "))
            conta_usuario.sacar(quantia)
        else:
            print("Por favor, crie uma conta primeiro.\n")
    elif escolha == 4:
        if conta_usuario:
            conta_usuario.ver_saldo()
        else:
            print("Por favor, crie uma conta primeiro.\n")
    elif escolha == 5:
        if conta_usuario:
            conta_usuario.mostrar_informacoes_pessoais()
        else:
            print("Por favor, crie uma conta primeiro.\n")
    else:
        print("Opção inválida. Tente novamente.\n")

print('Sistema fechado')
