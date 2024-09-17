#Listas encadeadas são as estruturas de dados dinâmicas mais simples e fundamentais.
#os itens da lista são conectados por ponteiros, formando uma cadeia de elementos (cadeia de nós).
#Cada nó contém um valor e um ponteiro para o próximo nó da lista.
#O último nó da lista aponta para None, indicando o fim da lista.
#A lista encadeada é uma estrutura de dados dinâmica, ou seja, ela pode crescer ou diminuir conforme necessário.

#nós da lista podem estar espalhados por toda a memória, e não precisam estar em posições contíguas.
#Isso permite que a lista cresça conforme necessário, sem a necessidade de realocar os elementos na memória.


#Uma lista que contem 4 itens a, b, c e d usa 8 células de memória, 4 para os valores e 4 para os ponteiros.

#Implementação de uma lista encadeada em Python

class No(object):
    # Implementação de um nó de lista encadeada
    
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo


class ListaEncadeada(object):
    # Implementa uma lista encadeada

    def __init__(self, inicio=None):
        self.__primeiro_no = inicio

    def __str__(self):
        no = self.__primeiro_no
        s = ""
        while no:
            s += f" -> {no.valor}" if s else str(no.valor)
            no = no.proximo
        return s

no_1 = No("once")
no_2 = No("upon")
no_3 = No("a")
no_4 = No("time")

no_1.proximo = no_2
no_2.proximo = no_3
no_3.proximo = no_4

lista = ListaEncadeada(no_1)
print(lista)