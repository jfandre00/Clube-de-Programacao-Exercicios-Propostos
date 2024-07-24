#beecrowd 2551

#Para terminarmos com EOF precisamos de um try com except (tratamento de erros)
#Para rodar o loop infinito vou usar o while True

while True:
    try:
        N = int(input())
        lista_velocidades = []
        recorde_dias = []

        maior_velocidade = 0

        for i in range(N):
            T, D = map(int, input().strip().split()) 
            #separando a entrada em duas variáveis
            velocidade_media = D / T
            lista_velocidades.append(velocidade_media)
            #no mesmo loop for já vou testando se a velocidade é a maior
            if velocidade_media > maior_velocidade:
                maior_velocidade = velocidade_media
                recorde_dias.append(i + 1) 
#Se velocidade média atual > maior_velocidade, atualiza maior_velocidade 
#e registra o dia (índice + 1) em recorde_dias
#garante que o primeiro treino resultado será imprimido pois a maior velocidade foi iniciada acima com 0, então toda primeira entrada é recorde. 

        for dia in recorde_dias:
            print(dia)
            #imprime os dias em que Flávio bateu seu recorde
    except EOFError:
        break

'''
Enunciado:
A grande Maratona de Rua de Curitiba irá ocorrer nos próximos dias! Vários atletas estão treinando há dias para o grande dia da corrida. Flávio é um dos atletas que está treinando diariamente para se sair bem na corrida. Ele tem corrido todas as manhãs nas pistas próximas de sua casa.

Os treinos do garoto são monitorados por um aplicativo em seu celular. Após cada treino, Flávio sabe tanto a duração do treino quanto a distância total percorrida. Com essas informações, ele consegue determinar a velocidade média obtida em cada treino.

Flávio está muito preocupado com a evolução de seu desempenho nos treinos, e em particular com seu recorde de velocidade média. Tal recorde é batido em um dado treino quando a velocidade média para este treino é maior que todas as velocidades médias obtidas nos treinos anteriores. Ajude Flávio a determinar em quais treinos ele conseguiu bater seu recorde.

Entrada
A entrada contém vários casos de teste. A primeira linha de cada caso contém um inteiro N (1 ≤ N ≤ 30), o número de treinos feitos. Considere que os treinos foram feitos nos dias 1, 2,...,N. As próximas N linhas descrevem os treinos. A linha i (1 ≤ i ≤ N) contém dois inteiros Ti e Di (1 ≤ Ti, Di ≤ 100), indicando, respectivamente, a duração do treino (em minutos) e a distância percorrida no treino (em quilômetros).

A entrada termina com fim-de-arquivo (EOF).

Saída
Para cada caso de teste, imprima uma lista de inteiros indicando os dias nos quais o recorde foi batido. Cada dia deve ser impresso em uma linha. Imprima os dias em ordem crescente. Note que o dia 1 sempre deve ser impresso.

Exemplo de Entrada	
3
1 1
2 1
2 3
2
2 16
4 20
Exemplo de Saída
1
3
1
'''