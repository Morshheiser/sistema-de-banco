import os

#return to menu
def return_to_menu():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

#code block for deposit

def validates_deposited_amount(extract, balance, deposit):
    if deposit:
        extract.append("Deposito: R$ %.2f" % deposit)
        balance = balance + deposit
        print("Deposito realizado com sucesso.")
        print("Saldo atual: R$ %.2f" % balance) 
    else:
        print("Não é possivel realizar a operação.")
    return(extract, balance)

def  requesting_deposit_value():
    while True:
        str_deposit_value = input("Qual valor do depósito:")
        if str_deposit_value.replace('.', '').isdigit():
            deposit_value = float(str_deposit_value)
            if deposit_value > 0:
                return deposit_value
            else:
                print("Valor informado inválido.")
        else:
            print("Valor informado inválido.")

def validates_deposited_vestment(extract, balance):
    deposit = requesting_deposit_value()
    extract, balance =validates_deposited_amount(extract, balance, deposit)
    return extract, balance

#code block for withdrawal operations

def validates_withdrawn_value(balance, extract, withdrawn_value, number_of_withdrawals):
    
    if withdrawn_value <= balance and withdrawn_value <= 500 and withdrawn_value > 0:
        extract.append("Saque: R$ %.2f" % withdrawn_value)
        balance = balance - withdrawn_value
        number_of_withdrawals += 1
    return extract, balance, number_of_withdrawals

def requesting_amount_withdrawn(balance):
    while True:
        value_drawn_str = input("Qual valor do saque:")
        if value_drawn_str.replace('.', '').isdigit():
            withdrawn_value = float(value_drawn_str)
            if withdrawn_value > 0:
                if withdrawn_value <= 500 and withdrawn_value < balance:
                    return withdrawn_value
                else:
                    withdrawal_limit = 500
                    print("Limite por saque: R$ %.2f" % withdrawal_limit)
                    print("Saldo insuficiente para operação.")  
        else:
            print("Entrada inválida. Digite apenas números e saldo positivo.")
    

def validate_withdrawal_parameter(number_of_withdrawals, balance, extract):
    if number_of_withdrawals <= 3 and balance > 0:
        withdrawn_value = 0
        withdrawn_value = requesting_amount_withdrawn(balance)
        if withdrawn_value > 0:
            extract, balance, number_of_withdrawals = validates_withdrawn_value(balance, extract, withdrawn_value, number_of_withdrawals)    
        print("Saldo atual: R$ %.2f" % balance)
    elif number_of_withdrawals > 3:
        print("\nPrezado cliente, seu limite de 3 saques diario foi alcançado")
        print("Aguarde 24 horas para realizar outra operação de saque.")
    elif balance <= 0:
        print("Saldo insuficiente para operação.")
        print("Saldo atual: R$ %.2f" % balance)
    return (number_of_withdrawals, balance, extract)

#code block for extracting operations

def bank_statement(extract, balance):
    print("\n########## Extrato ##########")
    for operation in extract:
        print(operation)
    print("Saldo atual: R$ %.2f" % balance)
    print("#############################")