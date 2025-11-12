"""
Mapas são conhecidos como dicionários em Python. Eles armazenam pares de chave-valor, onde cada chave é única.
Relembrando: Dicionários são mutáveis, ou seja, podem ser alterados após sua criação. E são representados
por chaves {}.
"""

receita = {'jan': 100,'fev': 120,'mar': 300}
print(receita)
#iterar sobre dicionários
for chave in receita:
    print(f'Em {chave} recebi {receita[chave]}')

#Acessando elementos
print(receita['fev'])
#Adicionando elementos
receita['abr'] = 350
print(receita)
#Removendo elementos
ret = receita.pop('mar')
print(ret)
print(receita)
#Dicionário de chaves (Acessando as chaves)
print(receita.keys())
#Dicionário de valores (acessando os valores)
print(receita.values()) 
#Dicionário de itens(chave-valor)
print(receita.items())

for valor in receita.values(): #Acessando os valores dentro de cada chave
    print(f'Valor recebido: {valor}')

#Desempacotamento de dicionários
for chave, valor in receita.items():
    print(f'Chave: {chave} recebeu o valor: {valor}')


#Soma, valor máximo, valor mínimo e tamanho
print(sum(receita.values())) #Soma dos valores
print(max(receita.values())) #Valor máximo
print(min(receita.values())) #Valor mínimo
print(len(receita)) #Quantidade de itens no dicionário
#Verificando se determinada chave está no dicionário
print('mar' in receita)
print('abr' in receita)
#Convertendo listas para dicionários
lista = [('jan', 100), ('fev', 200), ('mar', 300)]
print(dict(lista))
tupla = (('jan', 100), ('fev', 200), ('mar', 300))
print(dict(tupla))
conjunto = {('jan', 100), ('fev', 200), ('mar', 300)}
print(dict(conjunto))
#Criando dicionário com o método fromkeys
outro = {}.fromkeys('a','b') #Cria chaves com valor padrão
print(outro)