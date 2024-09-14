"""Estudo aprofundado sobre funções

O que é uma função?

Função é um bloco de código identificado por um nome e pode receber uma lista
de parâmetros, esses parâmetros podem ou não ter valores padrão. Usar funções
torna o código mais legível e possibilita o reaproveitamento de código.
Programar em funções, é o mesmo que dizer que estamos programando de maneira
estruturada.

def exibir_mensagem_1():
    print("Olá mundo!")

def exibir_mensagem_2(nome):
    print(f'Seja bem vindo {nome}!')

def exibir_mensagem_3(nome="Leonardo"):
    print(f'Seja bem vindo {nome}!')

exibir_mensagem_1()

exibir_mensagem_2("Leonardo")

exibir_mensagem_3()

exibir_mensagem_3("Thiago")

Retornando valores

Para retornar um valor, utilizamos a palavra reservada return.
Toda a função python retorna None por padrão. Diferente de
outras lingragem de programação, em python uma função pode
retornar mais de um valor.

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecesor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(calcular_total([10, 11, 12, 43]))

print(retorna_antecesor_e_sucessor(10))

Argumentos Nomeados

Funções também podem ser chamadas usando argumentos nomeados da forma chave=valor.

def salvar_carro(marca, modelo, ano, placa):
    #salva carro no banco de dados...
    print(f'Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}')

#salvar_carro("Dodge", "Charge", 2024, "ABC-456")
#salvar_carro(marca="fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca": "fiat", "modelo":"stylo", "ano":2003, "placa":"ABC-1234"})    

Args Kwargs

Podemos combinar parâmetros obrigatórios com args e kwargs. Quando esses são definidos
(*args e ""kwargs), o método recebe os valores como tupla e dicionário respectivamente.

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem =  f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)

# outro exemplo:

def order_pizza(size, *toppings, **details):
    print(f'Ordered a {size} pizza with the following toppings: ')
    for topping  in toppings:
        print(f'- topping')
    print('\nDetails of the order are:')
    for key, value in details.items():
        print(f'- {key}: {value}')

order_pizza('large', 'peperroni', 'olives', delivery=True, tip=5)

Parâmetros Especiais

Por padrão, argumentos podem ser passados para uma função Python tanto por posição quanto
explicitamente pelo nome. Para uma melhor legibilidade e desempenho, faz sentido restringir
a meneira pelo qual argumentos possam ser passados, assim um desenvolvedor precisa olhar
apenas para a  definição da função para determinar se os itens são passados por posição,
por posição e nome, ou por nome.

Ex:

def f(pos1, pos2, /, por_or_kwd, *, kwd1, kwd2):
      ----------     ----------     ----------
      posicinal      pos or key     - kwd olnly   

#   Positional only

#def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
#    print(modelo, ano, placa, marca, motor, combustivel)

#criar_carro("F-40", 1999, "FER-123", marca="Ferrari", motor="5.00", combustivel="Gas")    
#criar_carro("F-40", 1999, "FER-123", "Ferrari", "5.00", "Gas")           

# Keyword only

#def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
#    print(modelo, ano, placa, marca, motor, combustivel)

#criar_carro(modelo="Aventador", ano=2017, placa="lab-234", marca="Lamborgini",
#            motor="10.0", combustivel="Gas")    #válido

#criar_carro("Aventador", 2017, "lab-234", marca="Lamborgini",
#             motor="10.0", combustivel="Gas") # inválido


#Keyword and positional only

def criar_carro( modelo, ano, placa,/,*, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Aventador", 2017, "lab-234", marca="Lamborgini",
            motor="10.0", combustivel="Gas")   # válido

criar_carro(modelo="Aventador", ano=2017, placa="lab-234", marca="Lamborgini",
            motor="10.0", combustivel="Gas") # inválido

Objetos de primeira classe

Em python tudo é objeto, dessa forma funções também são objetos o que as
torna objetos de primeira classe. Com isso  podemos atribuir funções a 
variáveis, passá-las como parâmetros para funções, usá-las como valores em
estrururas de dados (listas, tuplas, dicionários, etc) e usar como valor de
retorno para uma função (closures).

def somar(a, b):
    return a+b

def subtrair(a, b):
    return a-b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)
print(op(1,100))

op = somar

Escopo local e Escopo global

Python trabalha com escopo local e global, dentro do bloco da  função o escopo é local.
Portanto alterações ali feitas em objetos imutáveis serão perdidas quando o método terminar
de ser  executado. Para usar objetos globais utilizamos a palavra chave global, que informa
ao interpretador que a váriavel que está sendo manipulada no escopo local é global. 
Essa não é uma boa prática e deve ser evitada.



"""
salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

novo_salario = salario_bonus(500)

print(novo_salario)

