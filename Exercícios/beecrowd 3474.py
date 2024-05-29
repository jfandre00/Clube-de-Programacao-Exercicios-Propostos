'''
Charlinho e seus amigos colecionavam figurinhas. Algumas tinham valores altos de venda, pois eram raras. Sempre que encontravam uma figurinha rara, vendiam e dividiam o valor entre o grupo, para que pudessem comprar mais pacotes de figurinhas, na esperança de encontrarem novas figurinhas raras.

Entrada
A entrada consiste em vários casos de teste. Cada caso contém um valor real V e um valor inteiro N, representando o valor que uma figurinha rara foi vendida, e a quantidade de integrantes do grupo de Charlinho, incluindo ele. Todos os valores serão possíveis de fazer uma divisão por igual entre os membros do grupo.

Saída
Imprima o valor que cada integrante irá receber.

Exemplos de Entrada	Exemplos de Saída
10.00     4           2.50

10.50     3           3.50
'''


v, n = list(map(float, input().split()))

print(f'{v / n:.2f}')
