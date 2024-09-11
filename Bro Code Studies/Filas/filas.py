#filas são FIFO (First In First Out)
#em inglês, fila é chamada de queue
#fila é uma estrutura de dados que permite a inserção de elementos em uma extremidade e a remoção em outra

class Fila(object):
    #Implementa o tipo abstrato de dados fila

    def __init__(self):
        self.__dados = []

    def __str__(self):
        return str(self.__dados)
    
    def enfileira(self, item):
        #Adiciona um item no final da fila
        self.__dados.append(item)
    
    def desenfileira(self):
        #Remove o primeiro item da fila e o retorna
        if len(self.__dados) > 0:
            return self.__dados.pop(0)
    
    def primeiro(self):
        #Retorna o primeiro item da fila sem removê-lo
        if not self.vazia():
            return self.__dados[0]
    
    def vazia(self):
        #Verifica se a fila está vazia
        return len(self.__dados) == 0
    
    def tamanho(self):
        #Retorna o número de itens na fila
        return len(self.__dados)
    
    def limpa(self):
        #Remove todos os itens da fila
        self.__dados = []

#Testando a classe Fila
fila = Fila()
print(fila)
fila.enfileira("Ana")
fila.enfileira("Carlos")
fila.enfileira("Maria")
fila.enfileira("João")
fila.enfileira("Pedro")
print(fila)
print(fila.desenfileira())
#Removeu o primeiro elemento, que é Ana
print(fila)

fila.desenfileira()
#Removeu o segundo elemento, que é Carlos
print(fila)

print(fila.primeiro())
print(fila.tamanho())
print(fila.vazia())





print(fila.primeiro())
