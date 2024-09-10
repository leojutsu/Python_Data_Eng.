""" O que são operadores de associação( in / not in)?

São operadores utilizados para verificar se um objeto está presente em uma sequência.
"""
curso = "Curso de Python"

frutas = ["laranja", "uva", "tomate"]

saques = [1500, 100]

test1 = "Python" in curso

test2 = "maçã" not in frutas

test3 = 200 in saques

print(test1, test2, test3)

