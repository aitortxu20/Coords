import math

def comprobacion(corda):
    listacord = list(corda)
    valorx = 0
    valory = 0
    indicecoma = 0
    for i in range(len(listacord)):
        if listacord[i] == ',':
            indicecoma = i

    if indicecoma < 1:
        return (False)
    else:
        valorx = listacord[0:indicecoma]
        valory = listacord[indicecoma+1:]

        try:
            valorx = float(''.join(valorx))
            valory = float(''.join(valory))
            return (valorx,valory)
        except:
            return (False)



while True:
    try:
        cordA = input('Introduzca las coordenadas del punto A separando los valores por una coma >>> ')
        cordB = input('Introduzca las coordenadas del punto B separando los valores por una coma >>> ')
        cordxA = comprobacion(cordA)[0]
        cordyA = comprobacion(cordA)[1]
        cordxB = comprobacion(cordB)[0]
        cordyB = comprobacion(cordB)[1]
        distancia = math.sqrt((cordxA-cordxB)**2 + (cordxB - cordyB)**2)
        print('La distancia entre los dos puntos es {} '.format(distancia))
        break

    except:
        pass


