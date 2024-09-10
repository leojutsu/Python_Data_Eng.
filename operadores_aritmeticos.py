produto1 = 20

produto2 = 10

soma = (produto1 + produto2) # soma
print(f'{produto1} + {produto2} = {soma}')

subt = (produto1 - produto2) # subtração
print(f'{produto1} - {produto2} = {subt}')

mult = (produto1 * produto2) # multiplocação
print(f'{produto1} * {produto2} = {mult}')

div = (produto1 / produto2) # divisão convencional com ponto flutuante (resto da divisão)
print(f'{produto1} / {produto2} = {div}')

div_int = (produto1 // produto2) # divisão inteira
print(f'{produto1} // {produto2} = {div_int}')

mod_div = (produto2 % produto1) # módulo da divisão
print(f'{produto1} % {produto2} = {mod_div}')

pot = (produto2 **2) # operação de potênciação
print(f'{produto2}² = {pot}')

# Expressões numéricas
# O python respeita a orden das operações
#1. parênteses
#2. potênciação e radiciação
#3. multiplicação e divisão
#4. soma e subtração

x = (10 + 5) * 4 # O python respeita a orden das operações
print(x)

y = (10 / 2) + (25 * 2) - (2 ** 2)
print(y)