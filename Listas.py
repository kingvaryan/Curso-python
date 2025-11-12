# LISTAS E SUAS APLICAÇÕES
"""Podemos usar listas para armazenar conjuntos de dados, como uma lista de nomes, números ou qualquer outro tipo de informação. 
As listas são mutáveis, o que significa que podemos adicionar, remover ou modificar elementos conforme necessário."""

"Não confundir listas com tuplas, que são imutáveis."

"""Não esquecer que a posição das listas começa em 0 e assim por diante.
Ou seja, o primeiro elemento está na posição 0, o segundo na posição 1, e assim por diante."""

#Como adicionar elementos a uma lista
nomes = ["Ana", "Bruno", "Carlos"]
nomes.append("Diana")  # Adiciona "Diana" ao final da lista
print(nomes)  # Saída: ['Ana', 'Bruno', 'Carlos', 'Diana']

#Adicionando um elemento em uma posição específica
nomes.insert(0, "Beatriz")  # Adiciona "Beatriz" na posição 1
print(nomes)  # Saída: ['Ana', 'Beatriz', 'Bruno', 'Carlos', 'Diana']

#Como remover elementos de uma lista
nomes.remove("Carlos")  # Remove "Carlos" da lista  
print(nomes)  # Saída: ['Ana', 'Beatriz', 'Bruno', 'Diana']

#Removendo o último elemento da lista
ultimo_nome = nomes.pop()  # Remove e retorna o último elemento da lista
print(nomes)  # Saída: ['Ana', 'Beatriz', 'Bruno']
print(ultimo_nome)  # Saída: 'Diana'

#Inserindo listas dentro de listas
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(listas[0])  # Saída: [1, 2, 3]
print(listas[1][1])  # Saída: 5  #Acessando o segundo elemento da segunda lista
print(listas[2][0])  # Saída: 7  #Acessando o primeiro elemento da terceira lista

#Adicionando elementos a uma lista dentro de outra lista
listas[1].append(10)  # Adiciona 10 à segunda lista
print(listas)  # Saída: [[1, 2, 3], [4, 5, 6, 10], [7, 8, 9]]
print(ultimo_nome)  # Saída: 'Diana'
print(nomes)  # Saída: ['Ana', 'Beatriz', 'Bruno']

#Obtendo o tamanho de uma lista
print(len(nomes))  # Saída: 3 (número de elementos na lista)

#Acessando elementos de uma lista
print(nomes[0])  # Saída: 'Ana' (primeiro elemento)
print(nomes[1])  # Saída: 'Beatriz' (segundo elemento)
print(nomes[-1])  # Saída: 'Bruno' (último elemento
print(nomes[-2])  # Saída: 'Beatriz' (penúltimo elemento)
print(nomes[0:2])  # Saída: ['Ana', 'Beatriz'] (elementos do índice 0 ao 1)
print(nomes[:2])  # Saída: ['Ana', 'Beatriz'] (
print(nomes[1:])  # Saída: ['Beatriz', 'Bruno'] (do índice 1 até o final)
print(nomes[:])  # Saída: ['Ana', 'Beatriz', 'Bruno'] (todos os elementos)

#Iterando sobre uma lista
for nome in nomes:
    print(nome) # Saída: Ana, Beatriz, Bruno (cada nome em uma linha)
#Verificando se um elemento está na lista
print("Ana" in nomes)  # Saída: True
print("Carlos" in nomes)  # Saída: False
print("Carlos" not in nomes)  # Saída: True
print("Ana" not in nomes)  # Saída: False

#Ordenando uma lista
numeros = [5, 2, 9, 1, 5, 6]
numeros.sort()  # Ordena a lista em ordem crescente
print(numeros)  # Saída: [1, 2, 5, 5, 6, 9]
numeros.sort(reverse=True)  # Ordena a lista em ordem decrescente
print(numeros)  # Saída: [9, 6, 5, 5, 2, 1]

#Usando a função sorted() para ordenar sem modificar a lista original
numeros = [5, 2, 9, 1, 5, 6]
numeros_ordenados = sorted(numeros)  # Retorna uma nova lista orden
print(numeros_ordenados)  # Saída: [1, 2, 5, 5, 6, 9]
print(numeros)  # Saída: [5, 2, 9, 1, 5, 6] (lista original permanece inalterada)
numeros_ordenados_decrescente = sorted(numeros, reverse=True)  # Retorna uma nova lista ordenada em ordem decrescente
print(numeros_ordenados_decrescente)  # Saída: [9, 6, 5, 5, 2, 1]

#Uma alternativa pro uso do extend
mais_nomes = ["Eduardo", "Fernanda"]
nomes += mais_nomes  # Adiciona os elementos de mais_nomes à lista nomes
print(nomes)  # Saída: ['Ana', 'Beatriz', 'Bruno', 'Eduardo', 'Fernanda']

#Utilizando o reverse em listas
nomes.reverse()  # Inverte a ordem dos elementos na lista
print(nomes)  # Saída: ['Fernanda', 'Eduardo', 'Bruno', 'Beatriz', 'Ana']

#Utilizando o count em listas
print(nomes.count("Ana"))  # Saída: 1 (conta quantas vezes "Ana" aparece na lista)
print(nomes.count("Carlos"))  # Saída: 0 (conta quantas vezes "Carlos" aparece na lista)

#Utilizando o slicing em listas
print(nomes[1:4])  # Saída: ['Eduardo', 'Bruno', 'Beatriz'] (elementos do índice 1 ao 3)
print(nomes[:3])  # Saída: ['Fernanda', 'Eduardo', 'Bruno'] (primeiros três elementos)
print(nomes[2:])  # Saída: ['Bruno', 'Beatriz', 'Ana'] (do índice 2 até o final)
print(nomes[-3:])  # Saída: ['Bruno', 'Beatriz', 'Ana'] (últimos três elementos)
print(nomes[:-2])  # Saída: ['Fernanda', 'Eduardo', 'Bruno'] (todos os elementos exceto os dois últimos)
print(nomes[:])  # Saída: ['Fernanda', 'Eduardo', 'Bruno', 'Beatriz', 'Ana'] (todos os elementos)
print(nomes[::-1])  # Saída: ['Ana', 'Beatriz', 'Bruno', 'Eduardo', 'Fernanda'] (lista invertida)

#Copiando listas
copia_nomes = nomes.copy()  # Cria uma cópia da lista nomes
print(copia_nomes)  # Saída: ['Fernanda', 'Eduardo', 'Bruno', 'Beatriz', 'Ana']
copia_nomes.append("Gabriel")  # Adiciona "Gabriel" à cópia
print(copia_nomes)  # Saída: ['Fernanda', 'Eduardo', 'Bruno', 'Beatriz', 'Ana', 'Gabriel']
print(nomes)  # Saída: ['Fernanda', 'Eduardo', 'Bruno', 'Beatriz', 'Ana'] (lista original permanece inalterada)

#Outra forma de copiar listas
outra_copia_nomes = nomes[:]  # Cria uma cópia da lista nomes
print(outra_copia_nomes)  # Saída: ['Fernanda', 'Eduardo', 'Bruno', 'Beatriz', 'Ana']
outra_copia_nomes.remove("Ana")  # Remove "Ana" da outra cópia
print(outra_copia_nomes)  # Saída: ['Fernanda', 'Eduardo', 'Bruno', 'Beatriz']
print(nomes)  # Saída: ['Fernanda', 'Eduardo', 'Bruno', 'Beatriz', 'Ana'] (lista original permanece inalterada)

#Limpando uma lista
nomes.clear()  # Remove todos os elementos da lista nomes
print(nomes)  # Saída: [] (lista vazia)

#Excluindo listas
del nomes  # Exclui a variável nomes
# print(nomes)  # Isso geraria um erro, pois nomes não existe mais
# Criando uma lista vazia
minha_lista = []
# Adicionando elementos com append()
minha_lista.append(10)
minha_lista.append(20)
minha_lista.append(30)
print("Lista após append:", minha_lista)
# Adicionando múltiplos elementos com extend()
minha_lista.extend([40, 50])
print("Lista após extend:", minha_lista)
# Inserindo elemento em posição específica com insert()
minha_lista.insert(2, 25)  # Insere 25 na posição 2
print("Lista após insert:", minha_lista)
# Adicionando múltiplos elementos novamente usando extend()
minha_lista.extend([60, 70, 80])

#Converter uma string para uma lista
print("Lista após novo extend:", minha_lista)
frase = "Guilherme Maia!"
lista_frase = list(frase)  # Converte a string em uma lista de caracteres
print(lista_frase)  # Saída: ['O', 'l', 'á', ' ', ',', ' ', 'm', 'u', 'n', 'd', 'o', '!']
palavras = frase.split()  # Divide a string em uma lista de palavras
print(palavras)  # Saída: ['Olá,', 'mundo!']

#Converter uma lista para uma string
lista_palavras = ['Olá,', 'mundo!']
frase_concatenada = ' '.join(lista_palavras)  # Concatena as palavras em uma string
print(frase_concatenada)  # Saída: 'Olá, mundo!'
frase_sem_virgula = ''.join(lista_palavras)  # Concatena as palavras sem espaços
print(frase_sem_virgula)  # Saída: 'Olá,mundo!'

#Utilizando o join com outros separadores
frase_com_hifen = '-'.join(lista_palavras)  # Concatena as palavras com hífen
print(frase_com_hifen)  # Saída: 'Olá,-mundo!'
frase_com_asterisco = '*'.join(lista_palavras)  # Concatena as palavras com asterisco
print(frase_com_asterisco)  # Saída: 'Olá,*mundo!'

#criando lista através do range
lista_numeros = list(range(1, 11))  # Cria uma lista com números de 1 a 10
print(lista_numeros)  # Saída: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Exemplo de lista de supermercado adicionando itens de acordo com a entrada do usuário e removendo itens comprados
supermercado = []
while True:
    item = input("Digite um item para adicionar à lista de supermercado (ou 'sair' para terminar): ")
    if item.lower() == 'sair': # O Lower transforma tudo em minúsculo
        break
    supermercado.append(item)
print("Lista de supermercado:", supermercado)
while supermercado: #Enquanto a lista não estiver vazia
    item_comprado = input("Digite um item que você comprou (ou 'sair' para terminar): ") #usuário digita o item comprado
    if item_comprado.lower() == 'sair':
        break
    if item_comprado in supermercado: #verifica se o item está na lista
        supermercado.remove(item_comprado) #remove o item da lista
        print(f"{item_comprado} removido da lista.") #confirmação de remoção
    else:
        print(f"{item_comprado} não está na lista.") #Afirma que o item não está na lista
    print("Lista de supermercado atualizada:", supermercado) #mostra a lista atualizada
#Exemplo de lista de tarefas
tarefas = []
while True:
    tarefa = input("Digite uma tarefa para adicionar à lista de tarefas (ou 'sair' para terminar): ")
    if tarefa.lower() == 'sair':
        break
    tarefas.append(tarefa)
print("Lista de tarefas:", tarefas)
while tarefas:
    tarefa_concluida = input("Digite uma tarefa que você concluiu (ou 'sair' para terminar): ")
    if tarefa_concluida.lower() == 'sair':
        break
    if tarefa_concluida in tarefas:
        tarefas.remove(tarefa_concluida)
        print(f"{tarefa_concluida} removida da lista.")
    else:
        print(f"{tarefa_concluida} não está na lista.")
    print("Lista de tarefas atualizada:", tarefas)

#Gerando indice em um for utilizando enumerate
for indice, nome in enumerate(outra_copia_nomes):
    print(f"Índice: {indice}, Nome: {nome}")
# Saída:
# Índice: 0, Nome: Fernanda
# Índice: 1, Nome: Eduardo
# Índice: 2, Nome: Bruno
#Índices são úteis para rastrear a posição dos elementos na lista durante a iteração.

#Encontrando em qual índice da lista está o elemento
indice_bruno = outra_copia_nomes.index("Bruno")  # Retorna o índice de "Bruno"
print(f"O índice de Bruno é: {indice_bruno}")  # Saída: O índice de Bruno é: 2
#Se o elemento não estiver na lista, o index() gerará um erro.

#Contando quantas vezes um elemento aparece na lista
outra_copia_nomes.append("Bruno")  # Adiciona outro "Bruno" à lista
contagem_bruno = outra_copia_nomes.count("Bruno")  # Conta quantas vezes "Bruno" aparece
print(f"Bruno aparece {contagem_bruno} vezes na lista.")  # Saída: Bruno aparece 2 vezes na lista.

#Podemos fazer busca dentro de um range. inicio/fim
indice_bruno_range = outra_copia_nomes.index("Bruno", 1, 4)  # Procura "Bruno" entre os índices 1 e 3
print(f"O índice de Bruno no range é: {indice_bruno_range}")  # Saída: O índice de Bruno no range é: 2
#Se o elemento não estiver no range especificado, o index() gerará um erro.

""" Revisão de Slicing
Slicing é uma técnica poderosa em Python que permite extrair partes de listas, strings e outras sequências.
A sintaxe básica para slicing é: sequência[início:fim:passo]
- início: índice onde o slice começa (inclusivo)
- fim: índice onde o slice termina (exclusivo)
- passo: intervalo entre os índices (opcional, padrão é 1)
"""

#Soma, valor máximo, valor mínimo e tamanho de listas
valores = [10, 20, 30, 40, 50]
soma_valores = sum(valores)  # Soma todos os elementos da lista
print(f"Soma dos valores: {soma_valores}")  # Saída: Soma dos valores: 150
valor_maximo = max(valores)  # Encontra o valor máximo na lista
print(f"Valor máximo: {valor_maximo}")  # Saída: Valor máximo: 50
valor_minimo = min(valores)  # Encontra o valor mínimo na lista
print(f"Valor mínimo: {valor_minimo}")  # Saída: Valor mínimo: 10
tamanho_lista = len(valores)  # Obtém o número de elementos na lista
print(f"Tamanho da lista: {tamanho_lista}")  # Saída: Tamanho da lista: 5
#Essas funções são úteis para análises rápidas de dados armazenados em listas.

#Desempacotamento de listas
cores = ["vermelho", "verde", "azul"]
cor1, cor2, cor3 = cores  # Desempacota os elementos da lista em variáveis
print(cor1)  # Saída: vermelho
print(cor2)  # Saída: verde
print(cor3)  # Saída: azul
#Se o número de variáveis não corresponder ao número de elementos na lista, ocorrerá um erro.


#Podemos usar o * para desempacotar o restante dos elementos em uma lista
cores = ["vermelho", "verde", "azul", "amarelo", "roxo"]
cor1, *outras_cores = cores  # Desempacota o primeiro elemento em cor1 e o restante em outras_cores
print(cor1)  # Saída: vermelho

#Shallow copy vs Deep copy
import copy
lista_original = [[1, 2, 3], [4, 5, 6]]
shallow_copia = copy.copy(lista_original)  # Cria uma cópia rasa (shallow copy)
deep_copia = copy.deepcopy(lista_original)  # Cria uma cópia profunda (deep copy)
lista_original[0][0] = 99  # Modifica um elemento na lista original
print("Lista Original:", lista_original)  # Saída: [[99, 2, 3], [4, 5, 6]]
print("Shallow Copy:", shallow_copia)  # Saída: [[99, 2, 3], [4, 5, 6]] (afeta a shallow copy)
print("Deep Copy:", deep_copia)  # Saída: [[1, 2, 3], [4, 5, 6]] (permanece inalterada)
#Shallow copy cria uma nova lista, mas os elementos internos ainda referenciam os mesmos objetos. Deep copy cria uma nova lista e novos objetos internos.