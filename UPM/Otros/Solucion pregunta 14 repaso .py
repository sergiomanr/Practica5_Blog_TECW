import math
a=int(input("Introduzca el coeficiente 'a':"))
b=int(input("\nIntroduzca el coeficiente 'b':"))
c=int(input("\nIntroduzca el coeficiente 'c':"))

if a == 0:
    x = -c/b
    print("Como a es 0, la única solución es x=",round(x,1))
else:
    radicando = b**2 - (4*a*c)
    if radicando < 0:
            print("\nLas raices no son reales")
    else:	
        sol1 = round(( -b + math.sqrt(radicando)) / (2*a), 2)
        sol2 = round(( -b - math.sqrt(radicando)) / (2*a), 2)
        print ("\nLas soluciones son:", sol1, sol2)
