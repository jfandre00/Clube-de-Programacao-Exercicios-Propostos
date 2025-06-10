import requests
from bs4 import BeautifulSoup

def decode_secret_message(doc_url):
    # Passo 1: Baixar o conteúdo da URL
    response = requests.get(doc_url)
    if response.status_code != 200:
        print(f"Erro ao acessar o documento. Código: {response.status_code}")
        return

    # Passo 2: Analisar o HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    if not table:
        print("Tabela não encontrada no documento.")
        return

    # Passo 3: Extrair dados da tabela
    rows = table.find_all('tr')[1:]  # pular o cabeçalho
    grid_data = []
    max_x = max_y = 0
    for row in rows:
        cols = row.find_all(['td', 'th'])
        if len(cols) < 3:
            continue
        try:
            x = int(cols[0].text.strip())
            char = cols[1].text.strip()
            y = int(cols[2].text.strip())
            grid_data.append((x, y, char))
            max_x = max(max_x, x)
            max_y = max(max_y, y)
        except ValueError:
            continue

    # Passo 4: Criar a grade (inicialmente preenchida com espaços)
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, char in grid_data:
        grid[y][x] = char  # preencher a grade nas posições corretas

    # Passo 5: Imprimir a grade invertendo as linhas (para que y=0 fique no topo)
    for row in reversed(grid):
        print(''.join(row))

# Exemplo de uso
doc_url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
decode_secret_message(doc_url)
