# Mój wspaniały program
A = abs(int(input("Podaj pierwszą liczbę\n")))
B = abs(int(input("Podaj drugą liczbę (rózną od 0)\n")))

W = int(A/B)
R = A - W*B

#print ("w jest", W, "r jest", R)

newA = B
newB = R
#print (newA, newB)

if R == 0:
    print ("Liczby są podzelne. Wynik dzielenia to:", W)

elif R >0:
    while R>0:

        W = int(newA/newB)
        R = newA - W*newB
        #print ("po pętli A jest", newA, "Wynik jest", W, "a reszta jest", R)
        newA = newB
        NWD = newB
        newB = R
    print ("NWD liczb", A, "i", B, "to:", NWD)

else:
    print ("Coś zmaściłeś")
