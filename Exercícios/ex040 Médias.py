n1 = float(input('primeira nota:'))
n2 = float(input('Segunda nota:'))
media = (n1+n2) / 2
print(f'Tirando a média da nota {n1} e {n2} o aluno ficou com {media} no semestre.')
if media >= 7.0:
    print('Aluno APROVADO')
elif media >= 5.0 or 6.9:
    print('Aluno de recuparação')
elif media < 5.0:
    print('Aluno reprovado')
