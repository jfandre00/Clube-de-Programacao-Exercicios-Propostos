#A premissa da hash table é que a chave determina a localização do valor

dicionario = {}

dicionario["bad"] = "evil"
dicionario["cab"] = "taxi"
dicionario["ace"] = "star"

#Abaixo um exemplo de codificação que determinamos

# a=1, b=2, c=3, d=4, e=5 -> a chave bad está na posição 2 * 1 * 4 = 8
# a=1, c=3, b=2 -> a chave cab está na posição 3 * 1 * 2 = 6
# a=1, c=3, e=5 -> a chave ace está na posição 3 * 1 * 5 = 15

# A busca é feita em O(1) pois a chave é calculada e a posição é encontrada diretamente, somente 2 passos são necessários






