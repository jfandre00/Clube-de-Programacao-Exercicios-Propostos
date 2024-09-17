#beecrowd 5054

def main():
    listaDePalavras = []
    numeroDePalavras = int(input())
    for i in range(numeroDePalavras):
        palavra = input()
        listaDePalavras.append(palavra)
    for palavra in listaDePalavras:
        if len(palavra) < 10:
            print(palavra)
        else:
            print(palavra[0] + str(len(palavra) - 2) + palavra[-1])

if __name__ == '__main__':
    main()
