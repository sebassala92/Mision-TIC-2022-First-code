import math

def distancia(punto_1, punto_2):
    distancia = 2 * 6372.795477598 * math.asin(((math.sin((punto_2[0] - punto_1[0])/2)**2)+(math.cos(punto_1[0])*math.cos(punto_2[0])*(math.sin((punto_2[1] - punto_1[1])/2)**2))**0.5))
    return distancia

matriz_1 = [[5.4, -72.8],
            [5.125, -75.966],
            [5.135, -76.976]]


matriz_2 = [[6.124, -75.946, 1035],
            [6.125, -75.966, 109],
            [6.135, -75.976, 31],
            [6.144, -75.836, 151]]

matriz_3 = []

coordenadas_frecuentes = 1 #int(input('Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión: '))
if (coordenadas_frecuentes<1) & (coordenadas_frecuentes>3):
    print('Error ubicación')
elif (coordenadas_frecuentes >= 1) & (coordenadas_frecuentes <= 3):
    for i in range(4):
        distancia_2 = round(distancia(matriz_1[coordenadas_frecuentes - 1], matriz_2[i]))
        matriz_3.append([])
        matriz_3[i].append(matriz_2[i][2])
        matriz_3[i].append([matriz_2[i][0], matriz_2[i][1]])
        matriz_3[i].append(distancia_2)


    matriz_3.sort()
    matriz_3.pop()
    matriz_3.pop()

    for i in range(2):
        if matriz_1[coordenadas_frecuentes-1][0] < matriz_3[i][1][0]:
            if matriz_1[coordenadas_frecuentes-1][1] < matriz_3[i][1][1]:
                matriz_3[i].append(['Occidente', 'Norte'])
            elif matriz_1[coordenadas_frecuentes-1][1] > matriz_3[i][1][1]:
                matriz_3[i].append(['Oriente', 'Norte'])
        elif matriz_1[coordenadas_frecuentes-1][0] > matriz_3[i][1][0]:
            if matriz_1[coordenadas_frecuentes-1][1] < matriz_3[i][1][1]:
                matriz_3[i].append(['Occidente', 'Sur'])
            elif matriz_1[coordenadas_frecuentes-1][1] > matriz_3[i][1][1]:
                matriz_3[i].append(['Oriente', 'Sur'])


print(matriz_3)
