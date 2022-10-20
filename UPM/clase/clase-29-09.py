lista = [1,2,1]
def lista_palindromo(lista: list):
    if  lista == lista[::-1]:
        return True
    else:
        return False
print(lista_palindromo(lista))