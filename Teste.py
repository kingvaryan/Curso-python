def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def main():
    nums = [read_int(f"Digite o {i+1}º número: ") for i in range(3)]
    pares = []
    impares = []
    for i, n in enumerate(nums, 1):
        tipo = "par" if n % 2 == 0 else "ímpar"
        print(f"Número {i} ({n}) é {tipo}.")
        (pares if n % 2 == 0 else impares).append(n)

    print()
    print("Pares:", pares if pares else "Nenhum")
    print("Ímpares:", impares if impares else "Nenhum")

if __name__ == "__main__":
    main()

# Teste.py
# Este arquivo contém o código principal para ler três números inteiros do usuário,
# determinar se são pares ou ímpares, e exibir os resultados.