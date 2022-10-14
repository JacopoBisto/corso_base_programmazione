n1=int(input("inserire primo valore"))
n2=int(input("inserire secondo valore"))
n3=int(input("inserire terzo valore"))
if (n1+n2+n3>10):
    print(n1+n2+n3)
else:
    #se n1 è il maggiore stampa n1
    if (n1 > n2 and n1 > n3):
        print(n1)
    else:
        #se n2 è il maggiore stampa n2
         if(n2 > n1 and n2 > n3):
            print(n2)
         else:
             #se n3 è il maggiore stampa n3
             if(n3 > n1 and n3 > n2):
                print(n3)
