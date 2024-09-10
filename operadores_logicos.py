saldo = 1000
saque = 200
limite = 100
conta_especial = True

# Operador lógico E precisa de V e V para entregar uma V com saída.
saida1 = saldo >= saque and saque <= limite
print(saida1)

# Operador lógico OU precisa de apenas um V para entregar uma V com saída.
saida2 = saldo >= saque or saque <= limite
print(saida2)

# Operação de negação
contatos_emergencia = []

not 1000 > 1500 # True

not contatos_emergencia # True

not "saque 1500;" # False

not "" # True

# Operação lógica dificil de identificar a primeira vista
exp = saldo >= saque and saque <= limite or conta_especial and  saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and  saldo >= saque)
print(exp_2)

# refatorando a expressão lógica para que o código fique mais simples de ler.

saque_conta_normal = (saldo >= saque and saque <= limite)
print(saque_conta_normal)

saque_conta_especial = (conta_especial and  saldo >= saque)
print(saque_conta_especial)