import os

def lista_subdiretorios(diretorio):
    # Verifica cada item dentro do diretório
    for item in os.scandir(diretorio):
        # Se o item atual é um subdiretório
        if item.is_dir() and not item.is_symlink():
            print(item.path)
            # Chama a função recursivamente para listar os subdiretórios do item atual
            lista_subdiretorios(item.path)


lista_subdiretorios("/Java") 