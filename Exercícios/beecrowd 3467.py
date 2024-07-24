#beecrowd 3467

while True:
    try: 
        sofa = input().strip()
        if sofa[2] == 'L':
            print('Esse eh o meu lugar')
        else:
            print('Oi, Leonard')
    except EOFError:
        break

'''
Enunciado:
Sheldon Cooper é um cara excêntrico. Uma de suas excentricidades é ter um local favorito no sofá: o lado esquerdo (de quem se senta). Mas não é um gosto aleatório, ele tem suas razões para isso: no inverno, esse lugar é perto o bastante do aquecedor para continuar quente, e não tão perto para causar transpiração. No verão, está no caminho de uma brisa, criada por duas janelas. Daí ele vê a televisão num ângulo que não é nem direto, que desencoraje a conversa, e não é longe o bastante para criar distorções na lente. Faça um programa que considere onde Leonard Hofstadter (o colega de apartamento de Sheldon) está sentado e mostre o que Sheldon irá falar.

Entrada
A entrada possui múltiplos casos de teste e termina com fim de arquivo. Cada caso de teste possui uma string com três caracteres que representam os lugares do sofá, onde 'x' é um lugar vago e 'L' é o local onde Leonard está sentado.

Saída
Seu programa deverá mostrar a fala do Sheldon ao ver Leonard. Se Leonard estiver no lugar favorito do Sheldon: "Esse eh o meu lugar", caso contrário: "Oi, Leonard".

Exemplo de Entrada	
xxL
Lxx
Exemplo de Saída
Esse eh o meu lugar
Oi, Leonard

Exemplo de Entrada
xLx
Exemplo de Saída
Oi, Leonard
'''