from tkinter import messagebox

global clientes, saldo
saldo = 0
clientes = {}

def obter_cliente(cliente):
    global clientes
    clientes = cliente

def sacar(valor):
    global saldo

    if valor > saldo:
        return messagebox.showinfo("Aviso", "Não foi possível sacar por falta de saldo")
    elif valor == 0:
        messagebox.showinfo("Aviso", "Não é possivel sacar igual a 0")
    else:
        saldo -= valor
        messagebox.showinfo("Aviso", "Operação Efetuada")
    return saldo

def depositar(valor):
    global saldo 
    if valor == 0:
        messagebox.showinfo("Aviso", "Não é possivel depositar valor igual a 0")
    saldo += valor
    messagebox.showinfo("Aviso", "Operação Efetuada")
    return saldo

def operacao(valor, operacao, cpf, conta):
    global saldo, clientes
    conta = int(conta)
    for cliente in clientes:
        try:
            if cpf == cliente["CPF"]:
                for numConta in cliente["Conta"]:
                    if conta == numConta["numConta"] and cpf == cliente["CPF"]:
                        saldo = numConta["Saldo"]
                        if operacao == 1:
                            if not numConta["Depositos"]:
                                numConta["Depositos"] = []
                                numConta["Depositos"].append(f"Deposito de: R$ {valor:.2f}")
                            depositar(valor)
                        elif operacao == 2:
                            if valor <= 500:
                                if numConta["qtdeSaques"] < 3:
                                    if not numConta["Saques"]:
                                        numConta["Saques"] = []
                                    numConta["Saques"].append(f"Saque de: R$ {valor:.2f}")
                                    sacar(valor)
                                    numConta["qtdeSaques"] += 1
                                else:
                                    messagebox.showinfo("Aviso", "Limite diário de saques atingido")
                            else:
                                messagebox.showinfo("Aviso", "Limite por saque é de 500 reais") 
                        numConta["Saldo"] = saldo
            print(cliente)           
        except:
            messagebox.showinfo("Aviso", "Verifique as informações fornecidas e tente novamente") 
def get_cliente():
    return clientes

