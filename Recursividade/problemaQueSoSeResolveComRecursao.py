#Exemplo: varredura em um sistema de arquivos.

#Digamos que você precisa escrever um programa que faz algo com todo o conteúdo de um diretório e de todos os seus subdiretórios (temos uma quantidade indefinida de níveis de subdiretórios).

import os


def lista_subdiretorios(diretorio):
    # Verifica cada item dentro do diretório
    for item in os.scandir(diretorio):
        # Se o item atual é um subdiretório
        if item.is_dir() and not item.is_symlink():
            # Imprime o caminho
            print(item.path) 

lista_subdiretorios("/") # subdiretórios do diretório raiz

lista_subdiretorios("/Windows") # subdiretórios do diretório Windows