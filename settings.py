def es_palindromo(texto):

  '''Detecta si un texto es palíndromo o no'''
  a = list(texto)
  while ' ' in a:
    a.remove(' ')
  print(a)
  if a == a[::-1]:
    print(True)
  else:
    print(False)
es_palindromo("ella te da detalle")
# print(list('ella te da detalle'))
# print(list("ella te da detalle")[::-1])