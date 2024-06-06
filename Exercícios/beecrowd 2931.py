#beecrowd exercicio 2931

def processar_casos():
    import sys
    input = sys.stdin.read
    dados = input().strip().split('\n')

    index = 0
    while index < len(dados):
        # Lê número de combinações e número de crianças
        linha = dados[index].strip()
        index += 1

        if linha == "":
            continue

        C, K = map(int, linha.split())

        # Dicionário para armazenar combinações suspeitas
        combinacoes_suspeitas = {}

        # Lê combinações suspeitas
        for _ in range(C):
            presente_desejado = dados[index].strip()
            index += 1
            S = int(dados[index].strip())
            index += 1
            presentes_suspeitos = set()
            for _ in range(S):
                presente_suspeito = dados[index].strip()
                presentes_suspeitos.add(presente_suspeito)
                index += 1
            combinacoes_suspeitas[presente_desejado] = presentes_suspeitos

        # Verifica cada criança
        for _ in range(K):
            presente_desejado, presente_recebido = dados[index].strip().split(';')
            index += 1
            if presente_recebido in combinacoes_suspeitas.get(presente_desejado, set()):
                print('Y')
            else:
                print('N')

# Para executar a função, chame processar_casos() usando redirecionamento de entrada padrão
if __name__ == "__main__":
    processar_casos()

'''Após ler e armazenar todas as combinações de presentes suspeitos e os dados das crianças, fazemos o seguinte:

Para cada criança, lemos o presente desejado e o presente recebido. Consultamos o dicionário de combinações suspeitas: Pegamos o conjunto de presentes suspeitos associados ao presente desejado da criança. Verificamos se o presente recebido está no conjunto de presentes suspeitos: Se o presente recebido está no conjunto de presentes suspeitos, imprimimos Y (Mamãe Noel deve investigar). Se o presente recebido não está no conjunto de presentes suspeitos, imprimimos N (Mamãe Noel não precisa investigar). Exemplo de Verificação Dados das Combinações Suspeitas:

Para o presente desejado "Carro", os presentes suspeitos são {"Caminhão", "Ônibus"}. Para o presente desejado "Boneca", o presente suspeito é {"Barbie"}. Dados das Crianças:

Criança 1: Deseja "Carro" e recebeu "Caminhão". Criança 2: Deseja "Boneca" e recebeu "Barbie". Criança 3: Deseja "Carro" e recebeu "Bicicleta". Verificação:

Criança 1: "Caminhão" está no conjunto de presentes suspeitos para "Carro" -> Imprime Y. Criança 2: "Barbie" está no conjunto de presentes suspeitos para "Boneca" -> Imprime Y. Criança 3: "Bicicleta" não está no conjunto de presentes suspeitos para "Carro" -> Imprime N.'''