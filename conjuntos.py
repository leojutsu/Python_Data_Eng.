carros = ["Ferrari", "Ford", "Lamborguini", "Dodge", "Mazda", "Honda", "Corola"]



#for indice, carro in enumerate(carros):
    #print(f'{indice}: {carro}')

#list comprehention
numeros = [23, 32, 98, 45, 33, 22, 87, 34]

pares = [numero for numero in numeros if numero % 2 == 0]

#print(pares)

#lista = []

#lista.append(RG)
#lista.append(CPF)

#print(lista)

#lista.clear()

#tupla
numeros = (23, 32, 98, 45, 33, 22, 87, 34,)

#for indice, numero in enumerate(numeros):
    #print(f'{indice}: {numero}')

#set
numeros = {23, 32, 98, 45, 33, 22, 87, 34}

#for indice, numero in enumerate(numeros):
    #print(f'{indice}: {numero}')    



conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

interseccao = conjunto_a.intersection(conjunto_b)

uniao = conjunto_a.union(conjunto_b)

diferenca = conjunto_a.difference(conjunto_b)

dif_sim = conjunto_a.symmetric_difference(conjunto_b)



#print(dif_sim)

""" Métodos do conjuto ser


-.union
-.intersection

#Criação e acesso aos dados em um dicionário.

# ex:

pessoa = {"nome": "Leonardo", "idade": 35}

pessoa2 = dict(nome="guilherme", idade=28)

pessoa2["telefone"] = "222-3333"

pessoa2["nome"] = "Luiz"
pessoa2["idade"] = 23



#print(pessoa2["idade"])
#print(pessoa2["nome"])

#métodos da classe dict

#pessoa.clear()

copia = pessoa.copy()

copia["cor"] = "amarelo"

#print(pessoa2)

print(copia.fromkeys(["telefone", "email", "estado"], "vazio"))

print(pessoa2.get("cidade"))

print(pessoa2.items())



#print(pessoa2.pop("idade"))

print(pessoa2.setdefault("pais", "USA"))

print(pessoa2.keys())


"""

contato = {"leojutsu@gmail.com": {"nome": "Leonardo", "telefone": "222-333"}}

contato.update({"leojutsu@gmail.com" : {"nome: Leo"}})

print(contato)

print(contato.values())


