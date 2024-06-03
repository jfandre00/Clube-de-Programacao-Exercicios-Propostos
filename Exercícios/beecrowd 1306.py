result = []
case_number = 1

while True:
    line = input().strip()
    if line == "0 0":
        break
    
    R, N = map(int, line.split())
    
    if R <= N:
        result.append(f"Case {case_number}: 0")
    else:
        ruas_extras = R - N
        sufixos_necessarios = (ruas_extras + N - 1) // N
        
        if sufixos_necessarios > 26:
            result.append(f"Case {case_number}: impossible")
        else:
            result.append(f"Case {case_number}: {sufixos_necessarios}")
    
    case_number += 1

for res in result:
    print(res)

