
import numpy as np

class punto():

    def __init__(self, coordenada_x = 0, coordenada_y = 0):
        self.coordenadas_1 = []
        self.coordenadas_1.append(coordenada_x)
        self.coordenadas_1.append(coordenada_y)

    def imprimir_coordenada(self):
        print(self.coordenadas_1)

    def cuadrante(self):
        if self.coordenadas_1[0] > 0 and self.coordenadas_1[1] > 0:
            print('este punto se situa en la coordenada 1')

        elif self.coordenadas_1[0] < 0 and self.coordenadas_1[1] > 0:
            print('este punto se situa en la coordenada 2')

        elif self.coordenadas_1[0] < 0 and self.coordenadas_1[1] < 0:
            print('este punto se situa en la coordenada 3')

        elif self.coordenadas_1[0] > 0 and self.coordenadas_1[1] < 0:
            print('este punto se situa en la coordenada 4')

        if self.coordenadas_1[0] == 0 and self.coordenadas_1[1] == 0:
            print('este punto se situa en el origen')

        if self.coordenadas_1[0] == 0 and self.coordenadas_1[1] != 0:
            print('este punto se situa en el eje x')

        if self.coordenadas_1[0] != 0 and self.coordenadas_1[1] == 0:
            print('este punto se situa en el eje y')

    def vector_resultante(self, coordenadas_2 = [0, 0]):
        self.vector_resultante = list(np.array(self.coordenadas_1) - np.array(coordenadas_2))
        print(f'el vector resultante es {self.vector_resultante}')

    def distancia(self, coordenadas_3 = [0, 0]):
        self.distancia = (((self.coordenadas_1[0]-coordenadas_3[0])**2)+(((self.coordenadas_1[1]-coordenadas_3[1])**2)))**(1/2)
        print(f'la distancia es {self.distancia}')



class alumno():

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f'el nombre del alumno es {self.nombre} y su nota es {self.nota}')

    def pasa_curso(self):
        if self.nota > 3.0:
            print(f'el alumno {self.nombre} ha pasado el curso')
        else:
            print(f'el alumno {self.nombre} no ha pasado el curso')



