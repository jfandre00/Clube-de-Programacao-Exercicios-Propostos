def dobra_array(array, i=0):
    '''Dobra os valores do array a partir do índice i (padrão 0)'''
    # Se i for um índice válido	
    if i < len(array):
        # Dobra o valor do índice i
        array[i] *= 2
        # Usa a mesma função para dobrar os valores restantes (a partir de i+1)
        dobra_array(array, i+1)

array = [1, 2, 3, 4, 5]
dobra_array(array)
print(array)  # [2, 4, 6, 8, 10]
