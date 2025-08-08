# -*- coding: utf-8 -*-

LEITURAS = 10
PROCEDIMENTO2 = 2
PROCEDIMENTO3 = 6
PROCEDIMENTO4 = 8
lista = []

for _ in range(LEITURAS):
    nome = input()
    lista.append(nome)
    
print(lista[PROCEDIMENTO2])
print(lista[PROCEDIMENTO3])
print(lista[PROCEDIMENTO4])