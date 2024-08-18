lanche = ('Hambúrguer', 'Suco', 'Pizza','Pudim')
print(lanche [0:3])
print(lanche [-2])
print(lanche [2:]) #do 2 até o final
print(lanche [1:3]) #do início até o 3

for cont in range(0, len(lanche)):
    print(f'Vou comer {lanche[cont]} na posicão {cont}.')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

for comida in lanche:
    print(f'Eu vou comer {comida}.')

print(sorted(lanche)) #mostra a tupla de forma ordenada.

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.count(5)) #quantas vezes está aparecendo o número 5
print(c.index(8)) #em que posição está o 8