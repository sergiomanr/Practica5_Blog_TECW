provee_por_cliente = [[1,1,0],[1,2,0],[1,1,1],[0,0,0],[1,0,0]]

frecuencia_solo_1_proveedor = 0

for i in provee_por_cliente: 
    if i == [1,1,1]:
        frecuencia_solo_1_proveedor +=1
    elif i[0] in [0,1] and i[1] in [0,1] and i[2] in [0,1] and i != [0,0,0]:
        frecuencia_solo_1_proveedor +=1
print(frecuencia_solo_1_proveedor/len(provee_por_cliente))
print('Provee',provee_por_cliente)
print('Frecuencia', frecuencia_solo_1_proveedor)

