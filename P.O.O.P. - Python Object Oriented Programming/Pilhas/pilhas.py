class Pilha(object):
    #Implementa o tipo abstrato de dados Pilha
    def __init__(self):
        self.__dados = []

    def __str__(self):
        return str(self.__dados)

    def empilha(self, elemento):
    #Adiciona item no topo da pilha
        self.__dados.append(elemento)

    def desempilha(self):
    #Remove e retorna o item no topo da pilha
        if not self.vazia():
            return self.__dados.pop()
    
    def topo(self):
    #Retorna o elemento no topo da pilha
        if not self.vazia():
            return self.__dados[-1]
        
    def vazia(self):
    #Verifica se a pilha está vazia
        return len(self.__dados) == 0


'''pilha = Pilha()
pilha.empilha(1)
pilha.empilha(2)
pilha.empilha(3)
pilha.empilha(4)
pilha.empilha(5)
pilha.empilha(6)
pilha.empilha(7)
print(f'a pilha está vazia? {pilha.vazia()}')
print(f'o elemento no topo da pilha é {pilha.topo()}')
#como mostrar a pilha inteira?
print(pilha)'''

#Qual o Big-O da função empilha?
#O(1) - constante
#Qual o Big-O da função desempilha?
#O(1) - constante

#Exemplo de aplicação de Pilhas?
#1. Desfazer e refazer ações
#2. Navegação de páginas na web
#3. Processamento de expressões matemáticas
#4. Verificação de parênteses
#5. Resolução de labirintos



