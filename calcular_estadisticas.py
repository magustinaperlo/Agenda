import math

print ("\n"*1)
print ("BIENVENIDO A LA CALCULADORA DE ESTADISTICAS\n con esta calculadora podras:\n sumar\n calcular promedio\n saber el numero mayor y el menor\n calcular desviación estándar" )
print ("\n")

numeros = input("ingrese numeros separados por espacios: ").split ()

#convertir en una lista de numeros 
numeros = [float(num)for num in numeros]

#diccionario con las operaciones
resultados = {
        "suma" : sum (numeros),
        "promedio" : sum (numeros) / len (numeros),
        "maximo" : max (numeros),
        "minimo" : min (numeros),
        "desviacion estandar" : math.sqrt (sum((x - sum(numeros)/len(numeros))**2 for x in numeros) / len(numeros))
}

for operacion, resultado in resultados.items ():
    print (f"{operacion}: {resultado}")        
           