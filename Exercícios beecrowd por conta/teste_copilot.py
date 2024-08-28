def obter_notas():
    pesos = [1, 2, 2, 3, 3]
    notas = []
    for i in range(5):
        while True:
            try:
                nota = float(input(f'Digite a {i+1}ª nota: '))
                if 0 <= nota <= 10:
                    notas.append((nota, pesos[i]))
                    break
                else:
                    print("Nota inválida. Digite uma nota entre 0 e 10.")
            except ValueError:
                print("Entrada inválida. Digite um número.")
    return notas

def calcular_media(notas):
    # Encontrar a menor nota e seu peso
    menor_nota, menor_peso = min(notas, key=lambda x: x[0])
    # Remover a menor nota e seu peso
    notas.remove((menor_nota, menor_peso))
    # Calcular a média ponderada com as notas restantes
    soma_ponderada = sum(nota * peso for nota, peso in notas)
    soma_pesos = sum(peso for _, peso in notas)
    return soma_ponderada / soma_pesos

def gerar_relatorio(notas, media):
    relatorio = "Relatório de Notas\n"
    relatorio += "-----------------\n"
    for i, (nota, peso) in enumerate(notas, 1):
        relatorio += f"Nota {i}: {nota} (Peso {peso})\n"
    relatorio += f"\nMédia: {media:.2f}\n"
    if media >= 7:
        relatorio += "Status: Aprovado\n"
    elif 5 <= media < 7:
        relatorio += "Status: Recuperação\n"
    else:
        relatorio += "Status: Reprovado\n"
    return relatorio

def main():
    notas = obter_notas()
    media = calcular_media(notas)
    relatorio = gerar_relatorio(notas, media)
    print(relatorio)

if __name__ == "__main__":
    main()

