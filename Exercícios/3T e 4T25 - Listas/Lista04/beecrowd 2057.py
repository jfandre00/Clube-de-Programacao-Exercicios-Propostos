s, t, f = map(int, input().split())
hora_no_destino = s + f
hora_chegada = hora_no_destino + t
if hora_chegada >= 24:
    hora_chegada -= 24
if hora_chegada < 0:
    hora_chegada += 24
print(hora_chegada)
