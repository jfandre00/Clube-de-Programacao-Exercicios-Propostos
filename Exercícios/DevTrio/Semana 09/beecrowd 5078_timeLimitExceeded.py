#beecrowd 5078 - time limit exceeded

def main():
    n = int(input())  # numero de lojas
    x = list(map(int, input().split()))  # precos das n lojas
    q = int(input())  # total de dias

    # Para cada dia, calcular o número de lojas e imprimir o resultado
    for _ in range(q):
        m = int(input())  # quanto que pode gastar no dia
        contador = 0
        for preco in x:
            if preco <= m:
                contador += 1
        print(contador)

if __name__ == '__main__':
    main()