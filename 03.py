nomes=["","","","",""]
for i in range (len(nomes)):
    nomes[i]=input(f"escreva 5 nomes")
"""for y in range (len(nomes)):"""

comp=input("me fala um nome pra pesquisar")
for y in range (len(nomes)):
    if comp==nomes[y]:
        print("achei")

