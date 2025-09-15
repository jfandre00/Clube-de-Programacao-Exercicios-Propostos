# Se o valor V da compra for divisível pelo número P de parcelas, todas as parcelas serão iguais a V/P. 
# Caso contrário, precisa fazer um ajuste, pois os valores das parcelas devem ser inteiros e a soma das parcelas deve ser igual a V.
# Distribuir o resto da divisão (V % P) entre as primeiras parcelas. 
# Exemplo V=45 e P=7 -> 45/7 = 6 e resto 3 -> as 3 primeiras parcelas serão 7 e as outras 4 serão 6. 

V = int(input())
P = int(input())

if V % P == 0: # Caso ideal pois o valor é divisível
    parcela = V // P
    for _ in range(P):
        print(parcela)
else:
    parcela = V // P # Valor base da parcela
    resto = V % P # Resto que precisa ser distribuído
    for i in range(P):
        if i < resto: # Distribui o resto entre as primeiras parcelas
            print(parcela + 1)
        else:
            print(parcela)

