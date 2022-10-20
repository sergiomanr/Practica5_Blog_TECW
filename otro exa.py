actual = [(1,15),(2,16),(3,19),(4,17),(5,11),(6,19,),(7,22)]
historico = [(1,11),(2,14),(3,29),(4,14),(5,9),(6,10,),(7,12)]
def calcular(actuals,historicos):
    if len(actuals) != len(historicos):
        print("1")
    for i in range(len(actuals)):
        if actuals[i][0] != historicos[i][0]:
            print("2")
    dias = []
    for i in range(len(actuals)):
        if actuals[i][1] > historicos[i][1]:
            dias.append(actuals[i][1])
        else:
            print("han habido",len(dias),"seguidos de calor")
            dias = []
        if len(dias) > 3:
            print("hay ola de calor")
    
calcular(actual,historico)  