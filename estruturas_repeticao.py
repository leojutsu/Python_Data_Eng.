""" O que são estruturas de repetição?

São estruturas utilizadas para repetir um trecho um determinado número de vezes.
Esse número pode ser conhecido previamente ou determinado atravez de uma expressão
lógica.

# Receba um número do teclado e exiba  os 2 números seguintes

a = int(input("Digite um número inteiro: "))
print(a)

repita 2 vezes:
    a += 1
    print(a)

Comando for e a função built-in range

# Comando for

O comando  for é usado para percorrer um objeto iterável. Faz sentido usar for quando sabemos
o número exato de vezes que nosso bloco de código deve ser executado, ou quando queremos percorrer
um objeto interável.

Exemplo:

texto = input("Informe um texto")
VOGAIS = "AEIOU"

for letras in texto:
    if letras.upper() in VOGAIS:
        print(letra, end="")

print()  # adicionar uma quebra de linha.

# Função range

Range é uma função built-in do python, ela é usada para produzir uma sequência de números
inteiros a partir de um ínicio (inclusivo) para um fim (exclusivo). Se usarmos range (i, j)
será produzido:

i, i+1, i+2, i+3, ..., j- 1.

Ela recebe 3 argumentos: stop (obrigatório), start (opcional) e step opcional.

#Comando while

    O comando while é usado para repetir um bloco de código várias vezes. Faz sentido usar while
    quando não sabemos o número exato de vezes que nosso bloco de código deve ser executado.

    opcao = -1
    
    white opcao != 0:
        opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

        if opcao ==1:
            print("sacando...")
        else opcao == 2:
            print("Exibindo o extrato...")


# while / else

    white opcao != 0:
        opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

        if opcao ==1:
            print("sacando...")
        else opcao == 2:
            print("Exibindo o extrato...")

    else:
        print("Obrigado por usar nosso sistema bancário, até logo!")
            
                
    """

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break
    
    if numero % 2 == 0:
        continue
    

    print(numero)