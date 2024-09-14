"""Objetivo geral
Conhecer métodos úteis para manipular objetos do tipo String, como
interpolar valores de variáveis e entender como funciona o fatiamento.

A Classe String do Ṕython é famosa por ser rica em métodos e por possuir
uma interface muito fácil de trabalhar.

Em algumas linguagens manipular sequências de caractéres não é um trabalho
trivial, porém, em python esse trabalho é muito simples.

curso = "pYthon"

print(curso.upper())

print(curso.lower())

print(curso.title())

curso = "   python"

print(curso.strip())

print(curso.lstrip())

print(curso.rstrip())

curso = "Python"

print(curso.center(10, "%"))

print(".".join(curso))

Fatiamentos

Em python temos 3 formas de interpolar variáveis em strings, a primeira é
usando o sinal de %, a segunda é usando o método format e a terceira é
utilizando f strings.

A primeira forma não é atualmente recomendads e seu uso Ṕython é raro, por
esse motivo iremos focar nas 2 últimas.

#primeira forma

nome = "leonardo"
idade = 35
profissão = "cientista de dados"
linguagem = "Python"
saldo = 45.444
dados = {"nome": "Leonardo", "idade": 35}

print("Nome: %s Idade %d" %(nome, idade))

print("Nome: {} Idade {}" .format(nome, idade))

print("Nome: {nome} Idade {idade}" .format(nome=nome, idade=idade))

print("Nome: {nome} Idade {idade}" .format(**dados))

print(f"nome: {nome} Idade {idade} saldo {saldo:.2f}")

Fatiamento

Fatiamento é uma técnica utilizada para retornar substrings (partes da string original),
informando início (start), fim(stop) e passo (step): [start:stop[, step]].

nome = "Leonardo da Silva Neves"

print(nome[0])

print(nome[:9])

print(nome[10:])

print(nome[10:16])

print(nome[10:16:2])

print(nome[:])

print(nome[::-1])

Strings multiplas linhas

Strings de múltiplas linhas são definidas informando 3 aspas simples ou duplas
durante a atribuição. Elas podem oculpar várias linhas do código, e todos os
espaços, em branco são incluídos na string final.



"""

nome = "Leonardo"

mensagem = f'''
  Olá meu nome é {nome},
Eu estou aprendendo Python.
    Essa mensagem tem diferentes recuos.
    '''
print(mensagem)


