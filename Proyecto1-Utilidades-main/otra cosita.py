EURO_BITCOIN_RATE = 44471.78

def sumar_numeros(num1, num2):
    '''Suma los dos numeros proporcionados.'''
    suma = num1 + num2
    return suma

#######################################################################################

def euros_a_bitcoins(euros):
  '''Convierte una cantidad de euros a bitcoins. 1 bitcoin = 44570.17 €'''
  bitcoin = 44570.17
  conversión = euros/44570.17 
  # print("\nEso equivale a",conversión,"bitcoin\n")
  return float(conversión)
  # raise NotImplementedError

def bitcoins_a_euros(numero_btc: float):
  '''Convierte una cantidad de bitcoins a euros. 1 bitcoin = 44570.17 €'''
  precio_btc = 44570.17
  conversion = numero_btc*precio_btc
  # print("Esos bitcoins equivalen a",conversion,"€")
  return float(conversion)
  # raise NotImplementedError

#######################################################################################

def contar_vocales(texto):

  '''Devuelve el número de vocales que tiene el texto dado.'''
  vocales = 0
  for x in texto:
    if x == 'a' or x== 'e' or x== 'i' or x== 'o' or x== 'u':
      vocales += 1
  return vocales
  # raise NotImplementedError

#######################################################################################

def es_palindromo(texto):

  '''Detecta si un texto es palíndromo o no'''
  a = list(texto)
  while ' ' in a:
    a.remove(' ')
  if a == a[::-1]:
    return True
  else:
    return False
  # raise NotImplementedError

#######################################################################################

def max_temperaturas(temperaturas, umbral):
  w = []
  for i in temperaturas:
    if int(i) >= umbral:
      w.append(i)
  return w
  # raise NotImplementedError



#######################################################################################

prod = []
def insertar(producto: str):
    '''Añade un producto a la lista'''
    prod.append(producto)

def borrar(numero):
    '''Devuelve el producto en el índice dado de lista de productos.'''
    prod.remove(prod[numero])
    # raise NotImplementedError

def lista_productos():
  '''Devuelve los producto en formato lista.'''  
  return prod
  # raise NotImplementedError

def productos():
  '''Muestra la lista de productos con sus índices.'''
  if len(prod) == 0:
    print('No hay productos')
  else:
    contador = 0
    for i in prod:
        print(contador, i)
        contador += 1
  # raise NotImplementedError

def cantidad():
  '''Devuelve el número de productos.'''
  return len(prod)
  # raise NotImplementedError
  
#######################################################################################

def cifrar(texto: str, desplazamiento: int)-> str:
    dic = {}
    contador = 1
    letras_unir = [] 
    for i in 'ABCDEFGHIJKLMÑOPQRSTUVWXYZÁÉÍÓÚ':
        dic[i] = contador
        contador += 1
    for e in texto.upper():
        if e in dic.keys():
          s = dic[e] + desplazamiento
          if s > 31:
            s = s-31
          for x,y in dic.items():
            if y == s:
              letras_unir.append(x)  
        else:
          letras_unir.append(e)
    return ''.join(letras_unir)
# print(cifrar('hola mundo', 0))
def descifrar(cifrado: str, desplazamiento: int)-> str:
    dic = {}
    contador = 1
    for i in 'ABCDEFGHIJKLMÑOPQRSTUVWXYZÁÉÍÓÚ':
        dic[i] = contador
        contador += 1
    letras_unir = []    
    for e in cifrado.upper():
        if e in dic.keys():
            s = dic[e] - desplazamiento
            if s <= 0:
                s = s+31
            for x,y in dic.items():
                if y == s:
                    letras_unir.append(x)  
        else:
            letras_unir.append(e)
    return ''.join(letras_unir)
# print(descifrar('UXÍSH, BJNXD',20))
#######################################################################################

x = str(input("""
Menú interactivo

Escribe tu acción
---->
"""))
print(x)