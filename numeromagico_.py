nm = 7
n1 = 0
I = 1
risultato = 0

while I <= 10:
    I = I+1
    n1 = int(input("scegli numero magico: "))
    if(n1 == nm):
        I = 11
        risultato = ("Complimenti hai indovinato!")
    else:
        risultato = ("game over!")
print(risultato)