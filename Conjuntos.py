"""
Conjuntos em qualquer linguagem de programação são estruturas de dados que armazenam elementos únicos, 
ou seja, não permitem duplicatas. 
Eles são úteis para operações matemáticas como união, interseção e diferença entre conjuntos.
Em python, os conjuntos são implementados usando a classe `set`.
Dito isto, da mesma forma que na matemática, conjuntos em Python também suportam operações como união, 
interseção e diferença.

- Sets(conjuntos) em Python são coleções não ordenadas de elementos únicos.
- Eles são definidos usando chaves `{}` ou a função `set()`.
- Operações comuns incluem:
  - União: `set1 | set2` ou `set1.union(set2)`
  - Interseção: `set1 & set2` ou `set1.intersection(set2)`
  - Diferença: `set1 - set2` ou `set1.difference(set2)`
- Elementos não são acessados por índice, pois conjuntos não são ordenados.

Conjuntos são bons para se utilizar quando precisamos garantir 
a unicidade dos elementos e realizar operações matemáticas de forma eficiente. 
Quando não nos importamos com a ordem dos elementos, conjuntos são uma ótima escolha.

Diferença entre conjuntos (Sets) e Mapas(Dictionaries) em Python:
- Conjuntos (Sets):
    - Armazenam apenas valores únicos.
    - Não possuem pares chave-valor.
    - São usados principalmente para operações matemáticas e verificação de unicidade.
- Mapas (Dictionaries):
    - Armazenam pares chave-valor.
    - Permitem acesso rápido aos valores através das chaves.
    - São usados para armazenar dados estruturados onde cada valor está associado a uma chave específica.
"""
s = set()
s.add(1) #usamos o .add pra adicionar elementos ao conjunto
s.add(2)
s.add(2)  # Tentativa de adicionar um elemento duplicado
print(s)  # Saída: {1, 2}

# Aplicações de de conjuntos
a = {1, 4, 3}
b = {3, 4, 5}
c = {5, 4, 3}
#União
uniao = a | b
print(uniao)  # Saída: {1, 2, 3, 4, 5}

#intersecção
intersecao = a & b
print(intersecao)  # Saída: {3} 
if a & b in c:
    print("Tem elementos em comum")
else:
    print("Não tem elementos em comum")
#diferença
diferenca = a - b
print(diferenca)  # Saída: {1, 2}

#importante lembrar que conjuntos não são ordenados
c = {5, 3, 1, 4, 2}
print(c)  # A ordem dos elementos pode variar a cada execução

lsita = [1, 2, 2, 3, 4, 4, 5]

conjunto = set(lsita)  # Remove duplicatas convertendo a lista em um conjunto

tupla = tuple(conjunto)  # Converte o conjunto de volta para uma tupla
print(tupla)  # Saída: (1, 2, 3, 4, 5) (a ordem pode variar)

dicionario = {'a': 1, 'b': 2, 'c': 3}
chaves_conjunto = set(dicionario.keys())  # Cria um conjunto com as chaves do dicionário
print(chaves_conjunto)  # Saída: {'a', 'b', 'c'} (a ordem pode variar)

#Assim como em todo outros conjunto Python, podemos colocar tipo de dados misturadoss em Sets
conjunto_misto = {1, "texto", 3.14, (1, 2), True}
print(conjunto_misto)  # Saída: {1, 'texto', 3.14, (1, 2), True} (a ordem pode variar)
"""
Dicionários em Python são estruturas de dados que armazenam pares chave-valor.
Cada chave é única e é usada para acessar o valor associado a ela.
Eles são definidos usando chaves `{}` e os pares chave-valor são separados por dois pontos `:`.
Dicionários são úteis para armazenar dados estruturados e permitem acesso rápido aos valores através das chaves. 
"""
