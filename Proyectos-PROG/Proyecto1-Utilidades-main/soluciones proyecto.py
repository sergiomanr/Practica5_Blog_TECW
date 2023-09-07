# def euros_a_bitcoins(euros):
#     '''Convierte una cantidad de euros a bitcoins. 1 bitcoin = 44570.17 €'''
#     bitcoin = 44570.17
#     conversión = euros/bitcoin 
#     print("Eso equivale a",round(conversión,2),"bitcoin")
# euros_a_bitcoins(4457.017)

# def bitcoin_a_euros(bitcoin):
#     precio_btc = 44570.17
#     conversion = bitcoin*precio_btc
#     print("Esos bitcoins equivalen a",round(conversion,2),"€")
# bitcoin_a_euros(0.22)

# def contar_vocales(texto):
#     vocales = 0
#     for x in texto[:]:
#         if x == 'a' or x== 'e' or x== 'i' or x== 'o' or x== 'u':
#             vocales += 1
#     print(vocales)
# contar_vocales('texto de ejemplo')

def max_temperaturas(temperaturas, umbral):
    w = []
    for i in temperaturas:
        if i >= umbral:
            w.append(i)
    print(w)
max_temperaturas([23.2, 25.3, 45.0, 18.0, 59.3], 60.0)