
# Regras gerais:

    #Ações: sacar, deposito, extrato;
    #Somente um usuario;
    #3 saques diarios, valor maximo do saque R$500;
    #Verificar se existe saldo em conta, exibindo: "Não será possivel o saque por falta de saldo";
    #Saques devem ser guardado em variaveis e devem ser listada no extratos de saque;
    #Extrato devem listar todos os deposito e saques da conta;
    #O extrato devem exibir o saldo atual da conta, formato: R$xxx.xx, exemplo: R$1500.45.

import func_banking 
import os 
import colorama

menu = """
       #############################
       |    Menu de operação       | 
       |                           |
       |      [1]Depositar         |
       |      [2]Saque             |
       |      [3]Saldo             |
       |      [4]Extrato           |
       |      [5]Sair              |
       |      []Menu               |
       #############################
Pressione qualquer tecla para voltar ao menu.    
    """

balance = 0
limit = 500
extract  = []
number_of_withdrawals = 1
withdrawal_limits = 3


print(menu)
while True:
    choice = input("\nPrezado cliente, escolha uma opção:")
    if choice not in ('1', '2', '3', '4', '5'): 
        func_banking.return_to_menu()
        print(menu)

    elif choice == '1':
        extract, balance  = func_banking.validates_deposited_vestment(extract, balance)

    elif choice == '2':
        number_of_withdrawals, balance, extract = func_banking.validate_withdrawal_parameter(number_of_withdrawals, balance, extract)    

    elif choice == '3':  
        print("saldo atual: R$ %.2f" % balance)    

    elif choice == '4':
       func_banking.bank_statement(extract, balance)

    elif choice == '5':
        print("\nObrigado. Encerrando nossa atividade.\n")
        break    
    
    else:
        print("Opção inválida. Por favor, escolha uma opção válida de 1 a 5.")    

