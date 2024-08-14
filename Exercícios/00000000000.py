#beecrowd 1771

#coluna letra B faixa 1 a 15, I 16 a 30, N 31 a 45, G 46 a 60, O 61 a 75

#OK se a cartela for válida
#Reciclavel se houver permutação possível
#Descartavel se não existir permutação

#1. verificar se está ok
#2. se não, como verificar se é possível transformar
#uma cartela que não é vá

#Eu verifiquei a quantidade de números que estão em cada letra, e vi se para cada letra tinha 5 numero - Patricia que acertou disse


#temos que ter 5 numeros B (1 a 15) I G O
#temos que ter 4 na faixa N 
#contamos quantos valores tem em cada faixa, e se tem exatamente essas quantidades de valores podemos transformar
# em reciclável
#inserir na posicao do indio algum valor entre 31 a 45,l pois podemos ai tratar essa coluna como outra qualquer


'''Explicação do código do professor
insert(12,31) coloca um numero que está no intervalo correto na posição do índio, resolvendo esse primeiro problema
no caso dos 3 loops um dentro do outro:
laço externo - indice inicial
laço interno - pula de 5 em 5, pega os valores B I N G O
if (cartela[i] -1) // 15 - se o intervalo é coluna B - essa conta tem que dar zero, no I é 1 e assim por diante - um numero entre 1 e 15 dividido por 15 - 1 vai ser zero, correto?'''