supermercado = []
while True:
    item = input("Digite um item para adicionar à lista de supermercado (ou 'sair' para terminar): ")
    if item.lower() == 'sair': # O Lower transforma tudo em minúsculo
        break
    supermercado.append(item)
print("Lista de supermercado:", supermercado)
while supermercado:
    item_comprado = input("Digite um item que você comprou (ou 'sair' para terminar): ")
    if item_comprado.lower() == 'sair':
        break
    if item_comprado in supermercado:
        supermercado.remove(item_comprado)
        print(f"{item_comprado} removido da lista.")
    else:
        print(f"{item_comprado} não está na lista.")
    print("Lista de supermercado atualizada:", supermercado)