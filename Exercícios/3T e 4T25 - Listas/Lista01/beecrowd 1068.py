while True:
    try:
        s = input() #lendo a entrada
    except EOFError:
        break

    balance = 0 # balanco entre ( e )
    ok = True # se não tem um ) vindo sem ter um ( antes
    for ch in s:
        if ch == '(':
            balance += 1
        elif ch == ')':
            if balance == 0: #aqui achou um ) sem ter um ( antes
                ok = False
                break
            balance -= 1

    if ok and balance == 0:
        print("correct")
    else:
        print("incorrect")