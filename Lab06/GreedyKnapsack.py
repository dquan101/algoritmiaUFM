def greedy_knapsack(valor, peso, capacidad):
    index = list(range(len(valor)))
    ratio = [v/w for v, w in zip(valor, peso)]
    index.sort(key=lambda i: ratio[i], reverse=True)
 
    maximo_valor = 0
    fracciones = [0]*len(valor)
    for i in index:
        if peso[i] <= capacidad:
            fracciones[i] = 1
            maximo_valor += valor[i]
            capacidad -= peso[i]
        else:
            fracciones[i] = capacidad/peso[i]
            maximo_valor += valor[i]*capacidad/peso[i]
            break
 
    return maximo_valor, fracciones
 
 
n = 3
valor = [60,100,120]
peso = [10,20,30]
capacidad = 50
 
maximo_valor, fracciones = greedy_knapsack(valor, peso, capacidad)
print("Elementos: Cobre, Plata, Oro")
print("Peso Maximo: 50")
print('El valor maximo es:', maximo_valor)
print('Las fracciones que se deben de tomar son:', fracciones)