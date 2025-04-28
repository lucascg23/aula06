notas=[0,0,0,0,0]
soma=0
contador=0
for i in range (len(notas)):
    notas[i]=float(input("escreva a nota"))
for y in range (len(notas)):
    soma+=notas[y]
media=soma/len(notas)
for x in range (len(notas)):
    if notas[x] >= media:
        contador+=1
print(media, contador)