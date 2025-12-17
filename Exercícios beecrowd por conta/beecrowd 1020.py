entrada = int(input())
ano, mes, dia = 0, 0, 0

while entrada > 0:
    if entrada >= 365:
        ano += 1
        entrada -= 365
    elif entrada >= 30:
        mes += 1
        entrada -= 30
    else:
        dia += 1
        entrada -= 1

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dia} dia(s)')
