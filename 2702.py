# https://judge.beecrowd.com/pt/problems/view/2702

Ca,Ba,Pa = map(int, input().split())

Cr,Br,Pr = map(int, input().split())

contador = 0

if(Cr > Ca):
    contador += (Cr - Ca) 

if(Br > Ba):
    contador += (Br - Ba)

if (Pr > Pa):
    contador += (Pr - Pa)

print(contador)