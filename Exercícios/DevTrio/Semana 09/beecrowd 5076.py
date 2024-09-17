#beecrowd 5076

def main():
    n = int(input())
    s = map(int, input().split())
    totalPessoas = sum(s)
    capacidadeTaxi = 4
    totalTaxi = 0
    if totalPessoas % capacidadeTaxi == 0:
        totalTaxi = totalPessoas // capacidadeTaxi
    else:
        totalTaxi = (totalPessoas // capacidadeTaxi) + 1
    print(totalTaxi)


if __name__ == '__main__':
    main()