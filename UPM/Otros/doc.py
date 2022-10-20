from ctypes import Union
from tkinter.messagebox import NO


precios = {
    'caca':30,
    'popo':10,
    'leche':5
}
cesta = {
    'leche':2,
    'caca':3,
    'popo':1
}
sumatorio = 0
for i,e in cesta.items():
    sumatorio += precios[i]*e
# print(round(sumatorio,2))

# nums= [1,23,8,12,6,5,16,7,21]
nums=[2,3,4]
resultado = {}
for i in nums:
    if i%2 == 0:
        resultado[i]=i**2
    else:
        resultado[i]=i**3
# print(resultado)
palabra = 'racecar'
palindromo = None 
if palabra == palabra[::-1]:
    palindromo = True
else:
    palindromo = False
# print(palindromo)

x = [2,4,3,6,1,7,8,3,4,8,6,1,9]
if x[0] == x[-1]:
    print('son iguales')
elif x[0]<x[-1]:
    print('primero menor que ultimo')
else:
    print('primero mayor que ultimo')
x = [1,2,3,4,5,6,7,8,9]
y = [1,3,5,7,9]
lista = []
for i in x:
    if i in y:
        lista.append(i)
print(len(lista))

div2= []
div3=[]
for i in x:
    if i%2 == 0:
        div2.append(i)
        if i%3 == 0:
            div3.append(i)
    elif i%3 == 0:
        div3.append(i)
print(div2)
print(div3)