from habilidades_conmejora import*
habilidades = [
        Divisas('bitcoin2euro', tasa=49929.38),
        Divisas('euro2bitcoin', tasa=1/49929.38),
        Contador('contarvocales', 'contador de vocales'),
        DetectorPalindromos('detectorpalindromo','Detecta si una palabra es palindroma'),
        ListaDeLaCompra('listadelacompra', 'Gestión de la lista de la compra'),
        Divisas('usd2euro', tasa=0.85, descripcion='Conversión de dólares a euros')
        ]
lista = ListaDeLaComp(habilidades)
lista.invocar("insertar", "Bananas")
lista.invocar("insertar", "Bananas")
lista.invocar("insertar", "Garbanzos", "0.68", "Alimentación", "cocido,hummus", "3")
lista.invocar("mostrar")