#beecrowd 5060

def main():
    m, n = map(int, input().split())
    areaDomino = 2
    areaTotal = m * n
    print(areaTotal // areaDomino)
    



if __name__ == '__main__':
    main()

#q: qual o motivo de usarmos o if __name__ == '__main__' com o def main()?
#r: para que o código seja executado apenas quando o arquivo for executado diretamente, e não quando for importado por outro arquivo