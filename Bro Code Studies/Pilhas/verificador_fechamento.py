from pilhas import Pilha

def verifica_sintaxe(codigo):
    DELIM = {"(": ")", "[": "]", "{": "}"}
    p = Pilha()
    # Inicia um laço que itera pelos caracteres no código
    for c in codigo:
        # Se o caractere é um delimitador de abertura:
        if c in "([{":
            # Empilhamos o caractere:
            p.empilha(c)
        # Se o caractere é um delimitador de fechamento:
        elif c in ")]}":
            if p.vazia():
                # Se a pilha está vazia, falta um delimitador de abertura
                return f"Erro #2: {c} não foi aberto"
            # Desempilha último delimitador de abertura
            del_abertura = p.desempilha()
            if c != DELIM[del_abertura]:
                # Se os delimitadores são de tipos diferentes, há um erro
                return f"Erro #3: {del_abertura} fechado com {c}"
    # Se chegamos ao final do código e a pilha não está vazia, falta um delimitador de fechamento
    if not p.vazia():
        return f"Erro #1: {p.topo()} não foi fechado"
    # Se não houve erros, a sintaxe está correta
    return "Nenhum erro encontrado"

print(verifica_sintaxe("( var x = { y: [1, 2, 3] } )"))
print(verifica_sintaxe(" var x = { y: [1, 2, 3]  } )"))
print(verifica_sintaxe("(var x = 2;"))
print(verifica_sintaxe("var x = [1, 2, 3)];"))