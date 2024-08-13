n1, n2, n3, n4 = map(float, input().split())

media = (2*n1 + 3*n2 + 4*n3 + 1*n4) / 10

print(f'Media: {media:.1f}')

if media < 5:
    print(f'Aluno reprovado.')
elif media >= 7:
    print(f'Aluno aprovado.')
else: 
    print(f'Aluno em exame.')
    exame = float(input())
    print(f'Nota do exame: {exame:.1f}')
    media = (media + exame) /2
    if media >= 5:
        print(f'Aluno aprovado.')
    else:
        print(f'Aluno reprovado.')
    print(f'Media final: {media:.1f}')