""" O que são Estruturas Condicionais em python?

    As estruturas condicionais permite o desvio de fluxo de controle, quando determinadas expressões
lógicas são atendidas.

if

    Para criar uma estrutura condicional simples, composta por um único desvio, podemos utilizar a palavra
reservada 'if'. O comando irá testar a expressão lógica, e em caso de retorno verdadeiro as ações presentes
no bloco de código do if serão executadas.

Exemplo:

saldo = 2000

saque =   float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando o saque!")

if saldo < saque:
    print("Saldo Insuficiente!")

if/else

    Para criar uma extrurura condicional com dois eventos, podemos utilizar as palavras
reservadas if e else. Caso a expressão lógica testada no if  for verdadeira, então o bloco
de código do if será executado. Caso contrário o bloco de código do else será executado.

Exemplo:

saldo = 2000

saque =   float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando o saque!")

else:
    print("Saldo Insuficiente!")

if/elif/else

Em alguns cenários queremos mais dois desvios, para isso podemos utilizar a palavra reservada
elif. O elif é composto por uma nova expressão lógica, que será testada e caso retorne verdadeiro o
bloco de código do elif será executado. Não existe um número máximo de elifs que podemos utilizar,
porém evite criar grandes extruturas condicionais, pois eles aumentam a complexidade do código.

Exemplo:

import sys
opcao = int(input("Informe uma opção: [1] Sacar [2] Extrato \n"))

if opcao == 1:
    valor = float(input("Informe o valor do saque: "))
    saque = valor
    print(f'você sacou {saque}!')

elif opcao == 2:
    print("Exibindo o Extrato...")

else:
    sys.exit("Opção Invalida")

if aninhados

Podemos criar estruturas condicionais aninhadas, para isso basta adicionar estruturas
if/elif/else dentro do bloco de código de estruturas if/elif/else.

Exemplo:
conta_normal = False 
conta_universitaria = True
conta_especial = True

saldo = 2000
saque = 1500
cheque_especial = 450

if conta_nornal:

    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso de cheque especial!")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente.")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

elif conta_especial:
    print("Conta especial selecionada!")

else:
    print("Sistema não reconheceu seu tipo de conta!")


if ternário

O if ternário permite escrever uma contição em uma unica linha.  Elw é composto por trÊs partes
a primeira parte é o retorno caso a expressão retorne verdadeiro, a segunda parte é a expressão
lógica e a terceira parte é o retorno caso a expressão não seja atendida.

Exemplo:

saldo = 2000
saque = 400

status = "Sucesso" if saldo <= saque else "Falha"

print(f'{status} ao realizar o saque!')
    


"""
MAIOR_IDADE =  18

idade = int(input("Informe sua idade: "))

if idade >= 18:
    print("Maior de idade, pode tirar CNH. ")

#if idade <= 18:
    #print("Ainda não pode tirar CNH. ")

else:
    print("Ainda não pode tirar CNH. ")        




