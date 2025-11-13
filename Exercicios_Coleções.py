"""
1. Crie um programa que lê 6 valores inteiros, armazene em uma lista e em seguida mostre na tela os valores
lidos
2. Faça um programa que possua uma lista denominada A que armazene 6 números inteiros. O programa
deve executar os seguintes passos:
a) Atribua os seguintes valores a essa lista: 1, 0, 5, -2, -5, 7.
b) Armazene em uma variável inteira a soma entre os valores das posições A[0], A[1] e A[5] da lista e mostre
na tela esta soma.
c) Modifique a lista na posição 5, atribuindo a esta posição o valor 100.
d) Mostre na tela cada valor da lista A, um em cada linha.

3. Faça um programa que leia 10 valores, armazene-os em uma lista e apresente quantos valores pares ele
possui
"""

# Exercício 1
valores = []
while len(valores) < 6:
    try:
        num = int(input("Digite um valor inteiro: "))
        valores.append(num)
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
print("Valores lidos:", valores)

# Exercício 2
A = []

# Parte A - Atribuindo valores à lista A
A.append(1)
A.append(0)
A.append(5)
A.append(-2)
A.append(-5)
A.append(7)

#Parte B - Somando valores das posições A[0], A[1] e A[5]
soma_valores = A[0] + A[1] + A[5]
print("Soma dos valores nas posições A[0], A[1] e A[5]:", soma_valores)

# Parte C - Modificando a posição 5 para 100
print("Lista A antes da modificação:", A)
A[5]= 100
print("Lista A após modificação:", A)

# Parte D - Mostrando cada valor da lista A em uma linha
print("Valores na lista A:")
for valor in A:
    print(valor)

# Exercício 3
valores = []
if len(valores) < 10:
    try:
        num = int(input("Digite um valor inteiro: "))
        valores.append(num)
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
    confirma = input("Voce deseja inserir outro numero? (s/n)")
    while confirma.lower() == 'sim' or confirma.lower() == 's':
        try:
            num = int(input("Digite um valor inteiro: "))
            valores.append(num)
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
        if len(valores) < 10:
            confirma = input("Voce deseja inserir outro numero? (s/n)")
        else:
            break
pares = 0
for valor in valores:
    if valor % 2 == 0:
        pares += 1
print("Quantidade de valores pares:", pares)
print("Valores lidos:", valores)


#Gerando exercícios de tuplas
"""
1. Crie um programa que leia 5 valores inteiros e armazene-os em uma tupla. Em seguida, mostre na tela
qual foi o maior e o menor valor digitado, bem como as suas respectivas posições na tupla.
2. Desenvolva um programa que leia uma tupla com 20 números inteiros. Após a leitura, o programa deve
calcular e mostrar:
a) A soma de todos os números pares contidos na tupla.
b) A quantidade de números ímpares.
c) A média dos números contidos na tupla.
"""

#Resolução exercício 1