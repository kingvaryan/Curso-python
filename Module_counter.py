from collections import Counter

"""
O módulo contador fornece funcionalidades para contar elementos em diferentes estruturas de dados.
Dentre essas funcionalidades, destacam-se:
- Contagem de elementos em listas, tuplas e dicionários.
- Contagem de ocorrências de um elemento específico.
- Funções para resetar e exibir contagens.
"""
# Armazena a última contagem realizada pelo módulo
_last_counts = Counter()

def contar_elementos(sequencia):
    """
    Conta elementos em listas, tuplas, strings ou qualquer iterável.
    Retorna um dicionário {elemento: quantidade} e atualiza o contador interno.
    Exemplo de uso:
      contar_elementos(['a', 'b', 'a']) -> {'a': 2, 'b': 1}
    """
    global _last_counts
    counts = Counter(sequencia)
    _last_counts = counts.copy()
    return dict(counts)

def contar_valores_dict(dicionario):
    """
    Conta as ocorrências dos valores presentes em um dicionário.
    Útil quando as chaves são diferentes mas os valores podem se repetir.
    Exemplo:
      contar_valores_dict({'x': 1, 'y': 2, 'z': 1}) -> {1: 2, 2: 1}
    """
    global _last_counts
    counts = Counter(dicionario.values())
    _last_counts = counts.copy()
    return dict(counts)

def contar_ocorrencia(sequencia, item):
    """
    Conta quantas vezes um item específico aparece na sequência.
    Exemplo:
      contar_ocorrencia([1,2,1,3], 1) -> 2
    """
    global _last_counts
    counts = Counter(sequencia)
    vezes = counts.get(item, 0)
    _last_counts = Counter({item: vezes})
    return vezes

def exibir_contagens():
    """
    Retorna a última contagem armazenada pelo módulo (como dicionário).
    Se nenhuma contagem foi feita, retorna {}.
    """
    return dict(_last_counts)

def resetar_contador():
    """
    Reseta a contagem interna para um estado vazio.
    """
    global _last_counts
    _last_counts = Counter()

# Exemplos práticos (são executados apenas quando este arquivo for rodado diretamente)
if __name__ == "__main__":
    # 1) Contar elementos numa lista
    lista = ['maçã', 'banana', 'maçã', 'laranja']
    print("Contagem da lista:", contar_elementos(lista))
    # 2) Contar quantas vezes um item aparece
    print("Ocorrências de 'maçã':", contar_ocorrencia(lista, 'maçã'))
    # 3) Contar valores dentro de um dicionário
    d = {'a': 1, 'b': 2, 'c': 1}
    print("Contagem dos valores do dicionário:", contar_valores_dict(d))
    # 4) Ver a última contagem armazenada
    print("Última contagem guardada:", exibir_contagens())
    # 5) Resetar e verificar
    resetar_contador()
    print("Após reset:", exibir_contagens())

###############################################################################################

    #Conteúdo do youtube#
"""
O funcionamento do módulo Counter da biblioteca collections em Python é bastante simples e eficiente
para contar elementos em iteráveis.
É como se a gente tivesse uma lista, o contador vai percorrer essa lista e contar quantas vezes
cada elemento aparece, armazenando essa informação em uma estrutura de dados chamada dicionário,
onde a chave é o elemento e o valor é a contagem de ocorrências desse elemento.
No exemplo abaixo, criamos uma lista x com alguns elementos repetidos.
Quando passamos essa lista para o Counter, ele retorna um dicionário com a contagem de cada elemento.
"""
from collections import Counter

x = ['a', 'b', 'c', 'a', 'b', 'b']
contador = Counter(x)
print(contador)

#Mais comum
mais_comum = contador.most_common(1)
print(mais_comum)

#Atualizar contador
contador.update(['a', 'b', 'a'])
print(contador)

#Subtrair contador
contador.subtract(['b', 'c'])
print(contador)

letters = contador.elements()
print(letters)
for letter in letters:
    print(letter, contador[letter])

y = Counter(x)
z = dict(y)
print(z)

