numa=[0,0,0,0,0,0,0,0,0,0]
m=[0,0,0,0,0,0,0,0,0,0]
for a in range (len(numa)):
    numa[a]=float (input("escreva os numeros"))

novon=float(input("digita outro"))

for b in range (len(numa)):
    m[b]=novon*numa[b]

print(m)