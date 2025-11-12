"""
Dicionários
Em algumas lingguagens de programação, os dicionários são conhecidos por mapas, arrays associativos, 
tabelas hash ou listas de associação.
Onde os dicionários são coleções do tipo chave/valor.
Listas ---> Índices, utilizamos []
Tuplas ---> Índices, utilizamos ()
--------- Sobre dicionários ---------
Dicionários ---> Chaves, utilizamos {}, onde as chaves e valores são separados por dois pontos {:}
Tanto chave quanto valor podem ser de qualquer tipo de dado.
Os dicionários são representados por chaves {}
Exemplo: {'chave': 'valor'}
Exemplo: {'nome': 'Geek', 'curso': 'Python'}
Exemplo: {'nome': 'Geek', 'idade': 3, 'altura':
podemos misturar tipos de dados

Obs: Não se faz necessário uso do IF ou do ELSE para verificar se uma chave já existe, caso tentemos adicionar uma
chave que já existe, o valor antigo será sobrescrito, ou seja, atualizado.
Exemplo:  dicionario = {'nome': 'Geek'}
          dicionario['nome'] = 'University' #Atualiza o valor da chave nome
            print(dicionario) # {'nome': 'University'}
----------------------------------------------------

"""
print(type({}))  # dict

#Mais comum
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)

#Menos comum
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)

#Acessando elementos
#Forma 1 - Acessando via chave, da mesma forma que listas e tuplas
print(paises['br'])
#OBS: Caso tentemos acessar uma chave que não existe, teremos o erro KeyError
#print(paises['ru']) #KeyError
#Forma 2 - Acessando via get - Recomendado
#print(paises.get('br'))
print(paises.get('ru')) #None
#Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada
print(paises.get('ru', 'Não encontrado')) #Não encontrado
#No get, caso a chave não exista, o valor None é retornado e não gera erro
#Já no acesso via colchetes, é gerado o erro KeyError

"""
O tipo None
O tipo de dado None em Python representa um tipo sem tipo, ou seja, um tipo especial que não é nem string,
nem inteiro, nem float. Nada!
É utilizado para representar um valor vazio ou nulo.
Em Python, sempre que uma função não retorna nenhum valor, o retorno é None.

Quando utilizamos? 
1 - Podemos utilizar None quando queremos criar uma variável e inicializá-la com um tipo sem tipo, antes de
definir seu valor real.
2 - Podemos utilizar None como valor default para variáveis ou parâmetros de funções.
3 - Podemos utilizar None para representar um valor nulo em estruturas de dados, como listas, tuplas ou dicionários.

   - Obs: Não precisamos utilizar None entre aspas. None é um tipo de dado próprio de Python, podemos definir
um valor padrão pra caso não encontremos o objeto com a chave informada

------------------------------------------------------------------------------------------------------------------
"""
"""Obs: Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive listas, tuplas ou até mesmo
dicionários como chaves de um dicionário.
Exemplos individuais para cada tipo de dado:"""

#Tupla
tupla = (1, 2, 3)
dicionario = {tupla: 'Valor'}
print(dicionario) # {(1, 2, 3): 'Valor'}
print(dicionario[tupla]) # Valor
print(dicionario[(1, 2, 3)]) # Valor
# print(dicionario[(1, 2)]) # KeyError
# print(dicionario[(1, 2, 3, 4)]) # KeyError
# print(dicionario[(4, 5, 6)]) # KeyError
# print(dicionario[(1, 2, 4)]) # KeyError
# print(dicionario[(1, 2, 3, 4, 5)]) # KeyError
# print(dicionario[(1, 2, 3, 4, 5, 6)]) # KeyError
# print(dicionario[(1, 2, 3, 4, 5, 6, 7)]) # KeyError
# print(dicionario[(1, 2, 3, 4, 5, 6, 7, 8)]) # KeyError
# print(dicionario[(1, 2, 3, 4, 5, 6, 7, 8, 9)]) # KeyError
# print(dicionario[(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)]) # KeyError

#LISTA
lista = [1, 2, 3]
"""
dicionario = {lista: 'Valor'} # TypeError: unhashable type: 'list'
print(dicionario)
print(dicionario[lista])
print(dicionario[[1, 2, 3]]) # TypeError: unhashable type: 'list'
print(dicionario[[1, 2]]) # TypeError: unhashable type: 'list'
print(dicionario[[1, 2, 3, 4]]) # TypeError
print(dicionario[[4, 5, 6]]) # TypeError
print(dicionario[[1, 2, 4]]) # TypeError
"""
#Adicionando elementos
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
#Forma 1 - Mais comum
receita['abr'] = 350
print(receita)
#Forma 2
receita.update({'mai': 500})
print(receita)


#Atualizando dados
#Forma 1
receita['mai'] = 550
print(receita)
#Forma 2
receita.update({'mai': 600})
print(receita)
"-------------------------------------------------------------------------"
#Atualizando dados - Adicionando novos dados
receita.update({'jun': 700})
print(receita)

#Remover dados
#Forma 1 - Mais comum
ret = receita.pop('jun') #Retorna o valor removido
print(ret)
print(receita)

#Forma 2o - Retorna o valor removido
del receita['mai']
print(receita)
#Forma 3 - Retorna o valor removido
ret = receita.popitem() #Remove o último item adicionado
print(ret)
print(receita)
#OBS: Caso tentemos remover uma chave que não existe, teremos o erro KeyError
#ret = receita.pop('jul') #KeyError
#del receita['jul'] #KeyError

#Exemplo de itens
produto1 = {'nome': 'Playstation 4', 'valor': 2300.00, 'qtde': 20}
produto2 = {'nome': 'Xbox S', 'valor': 4500.00, 'qtde': 10}
print(produto1)
print(produto2)


#métodos de dicionários
#Limpar dicionário (Zerar dados)
d = dict(a=1, b=2, c=3)
print(d)
d.clear()
print(d)

#Copiar dicionário
d = dict(a=1, b=2, c=3)
print(d)
novo = d.copy()
print(novo)
novo['d'] = 4
print(d)
print(novo)

#Forma 2 - Mais comum
novo = d.fromkeys('a', 'b')
print(novo)
novo = d.fromkeys(['nome', 'idade', 'altura'], 'desconhecido')
print(novo)

#Forma 2 - Shallow Copy
novo = d
novo['a'] = 4
print(d)
print(novo)


# Forma nao usual de criação de dicionários
outro = {}.fromkeys(['nome', 'idade', 'altura'], 'desconhecido')
print(outro)
print(type(outro))
# O método fromkeys cria as chaves com o valor definido, se não for definido, o valor padrão será None
#ELe vai gerar um dicionário com as chaves informadas, todas com o valor None. Ele irá atribui a esta chave o valor informado
novo = {}.fromkeys(['nome':"guilherme maia", 'idade', 'altura'])
print(novo)




"""
Conclusão 1: A forma mais comum de adicionar ou atualizar dados em um dicionário é utilizando a chave entre colchetes []
Conclusão 2: A forma mais comum de remover dados em um dicionário é utilizando a palavra reservada del
Conclusão 3: Em dicionários, não podemos ter chaves repetidas. Se tentarmos adicionar uma chave que já existe, o valor
será sobrescrito, ou seja, atualizado.
Conclusão 4: Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive listas, tuplas ou até mesmo
dicionários como chaves de um dicionário, desde que sejam imutáveis (tuplas).
Conclusão 5: Podemos misturar tipos de dados em um dicionário.
Conclusão 6: Podemos criar dicionários utilizando o construtor dict() ou utilizando chaves {}
Conclusão 7: Acessar elementos de um dicionário utilizando o get() é mais seguro do que utilizando colchetes []
Conclusão 8: Podemos utilizar o método keys() para obter as chaves de um dicionário, o método values() para obter os valores
e o método items() para obter os itens (chave/valor) de um dicionário.
Conclusão 9: Podemos utilizar a função len() para obter o tamanho (número de itens) de um dicionário.
Conclusão 10: Podemos utilizar a palavra reservada in para verificar se uma chave existe em um dicionário.
Conclusão 11: Podemos utilizar a palavra reservada not in para verificar se uma chave não existe em um dicionário.
Conclusão 12: Dicionários são mutáveis, ou seja, podemos adicionar, atualizar e remover itens.
Conclusão 13: Dicionários são desordenados, ou seja, não possuem uma ordem definida.
Conclusão 14: Dicionários são iteráveis, ou seja, podemos percorrer seus itens utilizando loops.
Conclusão 15: Dicionários são eficientes para buscas, pois utilizam uma estrutura de dados chamada tabela hash.
Conclusão 16: Dicionários são amplamente utilizados em Python, sendo uma das estruturas de dados mais importantes da linguagem.
Conclusão 17: Dicionários são muito utilizados em APIs, onde os dados são retornados no formato JSON, que é muito semelhante a um dicionário Python.
Conclusão 18: Dicionários são muito utilizados em bancos de dados NoSQL, onde os dados são armazenados em formato chave/valor.
Conclusão 19: Dicionários são muito utilizados em frameworks web, onde os dados são passados entre o servidor e o cliente no formato JSON.
Conclusão 20: Dicionários são muito utilizados em machine learning, onde os dados são armazenados em formato chave/valor para facilitar o acesso e a manipulação dos dados.
Conclusão 21: Dicionários são muito utilizados em data science, onde os dados são armazenados em formato chave/valor para facilitar o acesso e a manipulação dos dados.
Conclusão 22: Dicionários são muito utilizados em automação, onde os dados são armazenados em formato chave/valor para facilitar o acesso e a manipulação dos dados.
Conclusão 23: Dicionários são muito utilizados em scripts, onde os dados são armazenados em formato chave/valor para facilitar o acesso e a manipulação dos dados.
Conclusão 24: Dicionários são muito utilizados em jogos, onde os dados são armazenados em formato chave/valor para facilitar o acesso e a manipulação dos dados.
Conclusão 25: Dicionários são muito utilizados em sistemas, onde os dados são armazenados em formato chave/valor para facilitar o acesso e a manipulação dos dados.
Conclusão 26: Dicionários são muito utilizados em aplicações, onde os dados são armazenados em formato chave/valor para facilitar o acesso e a manipulação dos dados.
"""
