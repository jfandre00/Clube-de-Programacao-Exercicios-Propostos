#beecrowd 5059

def main():
    n, k = map(int, input().split())
    scores = list(map(int, input().split()))
    
    # Pontuação mínima para avançar
    min_score = scores[k-1]
    
    contador = 0
    for score in scores:
        if score >= min_score and score > 0:
            contador += 1
    
    print(contador)

if __name__ == '__main__':
    main()