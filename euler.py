#Analisis de algoritmos
#Jose Alexander Artavia Quesada
#2015098028

def e_cuadratica(n):
    """
    Funcion que calcula una aproximacion de euler con un algoritmo
    que resuelve el problema en complejidad temporal cuadrática

    Entrada: un numero >= 0
    Salida: aproximacion de euler
    Restricciones: entrada tipo int
    """

    i = 0
    resultado = 0

    while (i <= n):
        resultado += (1/factorial(i))
        i += 1
            
    return resultado


def e_lineal(n):
    """
    Funcion que calcula una aproximacion de euler con un algoritmo
    que resuelve el problema en complejidad temporal lineal

    Entrada: un numero >= 0
    Salida: aproximacion de euler
    Restricciones: entrada tipo int
    """

    i = 0
    fact = 1
    resultado = 0
    
    while(i <= n):
        resultado += (1/fact)
        i += 1
        fact = fact * i
        
    return resultado


def factorial(numero):
    """
    Funcion que calcula el factorial de un numero

    Entrada: un numero >= 0
    Salida: factorial de numero
    Restricciones: entrada tipo int
    """
    
    resultado = 1
    
    if numero >= 1:
        for i in range (1,numero+1):
            resultado = resultado * i
            
    return resultado

#-------------------------------------------------------------#

"""
print("1 =",e_cuadratica(0))
print("2 =",e_cuadratica(1))
print("2.5 =",e_cuadratica(2))
print("2.666 =",e_cuadratica(3))
print("2.708",e_cuadratica(4),"\n")

print("1 =",e_lineal(0))
print("2 =",e_lineal(1))
print("2.5 =",e_lineal(2))
print("2.666 =",e_lineal(3))
print("2.708",e_lineal(4))
"""
