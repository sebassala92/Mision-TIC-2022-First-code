from os import system   #importar la libreria system
import sys  #importar la libreria sys
import math #importar la libreria math
import json #importar la libreria csv

def menu1(): #funcion menu 1
    opcion = int(input('\n' '1. Cambiar contraseña\n'   #solicitar la opcion a elegir
                            '2. Ingresar coordenadas actuales\n'
                            '3. Ubicar zona wifi más cercana\n'
                            '4. Guardar archivo con ubicación cercana\n'
                            '5. Actualizar registros de zonas wifi desde archivo\n'
                            '6. Elegir opción de menú favorita\n'
                            '7. Cerrar sesión\n\n'   
                            'Elija una opcion: '))
    return opcion   #retornar la variable opcion

def menu2(): #funcion menu 2
    opcion2 = int(input('\n''1. Ingresar coordenadas actuales\n'    #solicitar la opcion a elegir
                            '2. Cambiar contraseña\n'   
                            '3. Ubicar zona wifi más cercana\n'
                            '4. Guardar archivo con ubicación cercana\n'
                            '5. Actualizar registros de zonas wifi desde archivo\n'
                            '6. Elegir opción de menú favorita\n'
                            '7. Cerrar sesión\n\n'   
                            'Elija una opcion: '))
    return opcion2   #retornar la variable opcion

def menu3(): #funcion menu 3
    opcion3 = int(input('\n''1. Ubicar zona wifi más cercana\n' #solicitar la opcion a elegir
                            '2. Cambiar contraseña\n'   
                            '3. Ingresar coordenadas actuales\n'                            
                            '4. Guardar archivo con ubicación cercana\n'
                            '5. Actualizar registros de zonas wifi desde archivo\n'
                            '6. Elegir opción de menú favorita\n'
                            '7. Cerrar sesión\n\n'   
                            'Elija una opcion: '))
    return opcion3   #retornar la variable opcion

def menu4(): #funcion menu 4
    opcion4 = int(input('\n''1. Guardar archivo con ubicación cercana\n' #solicitar la opcion a elegir
                            '2. Cambiar contraseña\n'   
                            '3. Ingresar coordenadas actuales\n'
                            '4. Ubicar zona wifi más cercana\n'                            
                            '5. Actualizar registros de zonas wifi desde archivo\n'
                            '6. Elegir opción de menú favorita\n'
                            '7. Cerrar sesión\n\n'   
                            'Elija una opcion: '))
    return opcion4   #retornar la variable opcion

def menu5(): #funcion menu 5
    opcion5 = int(input('\n''1. Actualizar registros de zonas wifi desde archivo\n' #solicitar la opcion a elegir
                            '2. Cambiar contraseña\n'   
                            '3. Ingresar coordenadas actuales\n'
                            '4. Ubicar zona wifi más cercana\n'
                            '5. Guardar archivo con ubicación cercana\n'                            
                            '6. Elegir opción de menú favorita\n'
                            '7. Cerrar sesión\n\n'   
                            'Elija una opcion: '))
    return opcion5   #retornar la variable opcion


def selec_opc():    #funcion seleccionar opcion
    opcion6 = int(input('Seleccione opcion favorita: '))    #solicitar la opcion a elegir
    return opcion6  #retornar la variable opcion 2

def adivinanza1():  #funcion adivinanza
    opcion7 = int(input('Primera adivinanza: “Para confirmar por favor\n'
                        'responda: Si me giras pierdo tres unidades por\n'
                        'eso debes colocarme siempre de pie, la respuesta es”: '))  # solicitar la respuesta a la adivinanza: respuesta 9
    return opcion7  #retornar opcion numerica adivinanza 1

def adivinanza2():
    opcion8 = int(input('Segunda adivinanza: “Para confirmar por favor\n'
                        'responda: Me separaron de mi hermano siamés,\n'
                        'antes era un ocho y ahora soy un... la respuesta es”: '))  # solicitar la respuesta a la adivinanza: respuesta 3
    return opcion8 #retornar opcion numerica adivinanza 1

def distancia(punto_1, punto_2):    #funcion distancia entre latitudes y longitudes
    distancia = 2 * 6372.795477598 * math.asin(((math.sin((punto_2[0] - punto_1[0])/2)**2)+(math.cos(punto_1[0])*math.cos(punto_2[0])*(math.sin((punto_2[1] - punto_1[1])/2)**2))**0.5))
    return distancia

print('Bienvenido al sistema de ubicación para zonas públicas WIFI')  #mensaje de beinvenida

nombre_usuario = '51617'  #asignacion nombre de usuario
contraseña = '71615'  #asignacion contraseña

nombre_usuario_2 = input('ingrese el nombre de usurario: ')  # ngreso de la contraseña por parte del usuario

if nombre_usuario_2 == nombre_usuario:  #verificamos que el usuario exista

    contraseña_usuario = input('ingrese la contraseña: ')  #solicitamos la contraseña

    if contraseña_usuario == contraseña:  #verificamos que la contraseña sea correcta

        # calculo del captcha para codigo 51617

        num1 = 617  # primer numero
        num2 = int((7 * 7) / 49)  #segundo numero
        captcha = num1 + num2  #suma final
        print(f'captcha {num1} + {num2}')
        captcha_usuario = int(input('ingrese el valor de la suma mostrada en el captcha: '))  #se solicita la suma del captcha

        if captcha_usuario == captcha:  #verificamos el la coinicdencia del captcha
            print('Sesión iniciada')  #concedemos acceso


            #variables codigo menu
            x1 = menu1() #llamar a la funcion menu
            contador1 = 0
            contador2 = 0
            salir = False
            opcion_coordenada = 0
            matriz_2 = [[6.124, -75.946, 1035],
                        [6.125, -75.966, 109],
                        [6.135, -75.976, 31],
                        [6.144, -75.836, 151]]
            matriz_3 = []

            while not salir:  #ciclo while para ejecutar las opciones del menu

                if x1 > 7 or x1 <= 0:   #condicinal if para garantizar la eleccion correcta del menu
                    if contador1 < 3:   #maximo numero de intentos 3
                        contador1 += 1
                        print('Error\nElija una opcion')
                        x1 = menu1()  # mostrar nuevamente el menu
                        continue

                    elif contador1 == 3:    #condicional para terminar el programa luego de 3 intentos
                        print('Error')
                        break

                elif x1 == 1:   #condicional para la opcion 1 del menu
                    intento_1 = input('ingrese su contraseña actual: ') #solicitar la contraseña
                    if intento_1 == contraseña: #verificar que la contraseña es correcta
                        contraseña_2 = input('ingrse su nueva contraseña: ')    #solicitar nueva contraseña
                        if contraseña != contraseña_2:  #virificar que la contraseña es diferente a la anterior
                            contraseña = contraseña_2   #actualizar contraseña
                            x1 = menu1()    #regresar al menu principal
                            continue
                        else:
                            print('no puede ingresar la misma contraseña')  #negar actualizacion de contraseña
                            x1 = menu1()    #regresar al menu Principal
                            continue
                    else:
                        print('Error')
                        break

                elif x1 == 2:   #condicional para la opcion 2 del menu
                    if contador2 == 0:  #verificar que es la primera vez ingresando a la opcion 2
                        contador2 += 1  #sumar 1 al contador2
                        matriz_1 = []   #crear matriz vacia
                        limites_latitud = [6.077, 6.284]    #establecer los limites de latitud
                        limites_longitud = [-76.049, -75.841]   #establecer los limites de longitud
                        for fila in range(3):   #ciclo for para introducir la locaclizacion del usuario en la matriz_1
                            matriz_1.append([]) #agregar una lista vacia a la matriz_1
                            latitud = float(input('ingrese la latitud: '))  #solicitar la latitud  del uruario
                            if (latitud == False):  #verificar si la latitud es un flotante o entero
                                print('Error coordenada')
                                sys.exit()  #salir del programa
                            if (limites_latitud[0] < latitud) and (limites_latitud[1] > latitud):   #verificar que la latitud se encuentra dentro de los limites
                                matriz_1[fila].append(latitud)  #agregar la latitud a las filas de la matriz_1
                                longitud = float(input('ingrese la longitud: '))    #solicitar la longitud del uruario
                                if (longitud == False): #verificar si la longitud es un flotante o entero
                                    print('Error coordenada')
                                    sys.exit()  #salir del programa
                                if (limites_longitud[0] < longitud) and (limites_longitud[1] > longitud):   #verificar que la longitud se encuentra dentro de los limites
                                    matriz_1[fila].append(longitud) #agregar la longituda las filas de la matriz_1
                                else:
                                    print('Error coordenada')   #error fuera de los limites
                                    sys.exit()  #salir del programa
                            else:
                                print('Error coordenada')   #error fuera de los limites
                                sys.exit()  #salir del programa
                        x1 = menu1()    #regresar al menu principal
                        continue

                    elif contador2 > 0:
                        opcion_coordenada = int(input(f'coordenada [latitud,longitud] 1: {matriz_1[0]}\n'
                                                      f'coordenada [latitud,longitud] 2: {matriz_1[1]}\n'
                                                      f'coordenada [latitud,longitud] 3: {matriz_1[2]}\n'
                                                      'La coordenada 1 es la que esta mas al norte\n'
                                                      'La coordenada 2 es la que esta mas al sur\n'
                                                      'Presione 1, 2 o 3 para actualizar la respectiva coordenada\n'
                                                      'Presiones 0 para regresar al menu: '))
                        if opcion_coordenada == 1:
                            latitud = float(input('ingrese la latitud: '))
                            if (latitud == False):
                                print('Error coordenada')
                                sys.exit()
                            elif (limites_latitud[0] < latitud) and (limites_latitud[1] > latitud):
                                matriz_1[0].append(latitud)
                                matriz_1[0].pop(0)
                                longitud = float(input('ingrese la longitud: '))
                                if (longitud == False):
                                    print('Error coordenada')
                                    sys.exit()
                                elif (limites_longitud[0] < longitud) and (limites_longitud[1] > longitud):
                                    matriz_1[0].append(longitud)
                                    matriz_1[0].pop(0)
                                    x1 = menu1()
                                    continue
                                else:
                                    print('Error actualización')
                                    sys.exit()
                            else:
                                print('Error actualización')
                                sys.exit()

                        elif opcion_coordenada == 2:
                            latitud = float(input('ingrese la latitud: '))
                            if (latitud == False):
                                print('Error coordenada')
                                sys.exit()
                            elif (limites_latitud[0] < latitud) and (limites_latitud[1] > latitud):
                                matriz_1[1].append(latitud)
                                matriz_1[1].pop(0)
                                longitud = float(input('ingrese la longitud: '))
                                if (longitud == False):
                                    print('Error coordenada')
                                    sys.exit()
                                elif (limites_longitud[0] < longitud) and (limites_longitud[1] > longitud):
                                    matriz_1[1].append(longitud)
                                    matriz_1[1].pop(0)
                                    x1 = menu1()
                                    continue
                                else:
                                    print('Error actualización')
                                    sys.exit()

                            else:
                                print('Error actualización')
                                sys.exit()

                        elif opcion_coordenada == 3:
                            latitud = float(input('ingrese la latitud: '))
                            if (latitud == False):
                                print('Error coordenada')
                                sys.exit()
                            elif (limites_latitud[0] < latitud) and (limites_latitud[1] > latitud):
                                matriz_1[2].append(latitud)
                                matriz_1[2].pop(0)
                                longitud = float(input('ingrese la longitud: '))
                                if (longitud == False):
                                    print('Error coordenada')
                                    sys.exit()
                                elif (limites_longitud[0] < longitud) and (limites_longitud[1] > longitud):
                                    matriz_1[2].append(longitud)
                                    matriz_1[2].pop(0)
                                    x1 = menu1()
                                    continue
                                else:
                                    print('Error actualización')
                                    sys.exit()
                            else:
                                print('Error actualización')
                                sys.exit()
                        elif opcion_coordenada == 0:
                            x1 = menu1()
                            continue

                        else:
                            print('Error actualización')
                            sys.exit()

                elif x1 == 3:
                    if contador2 > 0:   #verificar que ya se ingresaron las coordenadas del usuario
                        print(f'coordenada [latitud, longitud] 1: {matriz_1[0]}\n'  #imprimir las 3 ubicaciones del usuario
                              f'coordenada [latitud, longitud] 2: {matriz_1[1]}\n'
                              f'coordenada [latitud, longitud] 3: {matriz_1[2]}\n')
                        coordenadas_frecuentes = int(input('Por favor elija su ubicación actual (1, 2 ó 3) para calcular la distancia a los puntos de conexión: ')) #soliciar la ubicacion del usuario
                        if (coordenadas_frecuentes<1) | (coordenadas_frecuentes>3): #verificar que la opcion elegida no es diferente de 1 y 3
                            print('Error ubicación')
                            break   #terminar el programa
                        elif (coordenadas_frecuentes >= 1) & (coordenadas_frecuentes <= 3): #verificar que la opcion elegida esta entre 1 y 3
                            for i in range(4):  #ciclo for para ingresar informacion a la matriz_3
                                distancia_2 = round(distancia(matriz_1[coordenadas_frecuentes - 1], matriz_2[i]))   #calcular la distancia
                                matriz_3.append([]) #agregar listas vacias a la matriz_3
                                matriz_3[i].append(matriz_2[i][2])  #agregar la cantidad de ususarios promedio a cada fila de matriz_3
                                matriz_3[i].append([matriz_2[i][0], matriz_2[i][1]])    #agregar la latitud y la longitud a cada fila de matriz_3
                                matriz_3[i].append(distancia_2)   #agregar la distancia a cada fila de la matriz_3

                            matriz_3.sort() #ordenar la matriz_3
                            matriz_3.pop()  #elimnar el ultimo elemento de la matriz 3
                            matriz_3.pop()  #elimnar el ultimo elemento de la matriz 3

                            for i in range(2):  #ciclo for para agregar las etiquetas de direccion a la matriz_3
                                if matriz_1[coordenadas_frecuentes - 1][0] < matriz_3[i][1][0]: #verificar la posicion del ususario con respecto a la zona wifi
                                    if matriz_1[coordenadas_frecuentes - 1][1] < matriz_3[i][1][1]: #verificar la posicion del ususario con respecto a la zona wifi
                                        matriz_3[i].append(['Occidente', 'Norte'])  #agregar la etiqueta de direccion a la matriz_3
                                    elif matriz_1[coordenadas_frecuentes - 1][1] > matriz_3[i][1][1]:   #verificar la posicion del ususario con respecto a la zona wifi
                                        matriz_3[i].append(['Oriente', 'Norte'])    #agregar la etiqueta de direccion a la matriz_3
                                elif matriz_1[coordenadas_frecuentes - 1][0] > matriz_3[i][1][0]:   #verificar la posicion del ususario con respecto a la zona wifi
                                    if matriz_1[coordenadas_frecuentes - 1][1] < matriz_3[i][1][1]: #verificar la posicion del ususario con respecto a la zona wifi
                                        matriz_3[i].append(['Occidente', 'Sur'])    #agregar la etiqueta de direccion a la matriz_3
                                    elif matriz_1[coordenadas_frecuentes - 1][1] > matriz_3[i][1][1]:   #verificar la posicion del ususario con respecto a la zona wifi
                                        matriz_3[i].append(['Oriente', 'Sur'])  #agregar la etiqueta de direccion a la matriz_3

                            print(f'La zona WiFi {coordenadas_frecuentes}: ubicada en {matriz_3[0][1]} a {matriz_3[0][2]} metros, tiene en promedio {matriz_3[0][0]} usuarios\n'    #imprimir informacion varia 
                                  f'La zona WiFi {coordenadas_frecuentes}: ubicada en {matriz_3[1][1]} a {matriz_3[1][2]} metros, tiene en promedio {matriz_3[1][0]} usuarios') #imprimir informacion varia
                            indicaciones = int(input('Elija 1 o 2 para recibir indicaciones de llegada: ')) #solicitar una de las 2 ubicaciones

                            if (indicaciones == 1): #verificar si se escogio la opcion 1
                                print(f'Para llegar a la zona 1 wifi dirigirse primero al {matriz_3[0][3][0]} y luego hacia el {matriz_3[0][3][1]}')   #imprimir indicaciones de llegada
                                print('El tiempo promedio en bus es:', (matriz_3[0][2]/16.67), '\n'  #imprimir indicaciones tiempo
                                      'El tiempo promedio a pie es:', (matriz_3[0][2]/0.483))    #imprimir indicaciones de tiempo
                            elif (indicaciones == 2):
                                print(f'Para llegar a la zona 2 wifi dirigirse primero al {matriz_3[1][3][0]} y luego hacia el {matriz_3[1][3][1]}')   #imprimir indicaciones de llegada
                                print('El tiempo promedio en bus es:', (round(matriz_3[1][2] / 16.67)), '\n'    #imprimir indicaciones de tiempo
                                      'El tiempo promedio a pie es:', (round(matriz_3[1][2]) / 0.483)) #imprimir indicaciones de tiempo
                            else:
                                print('Error zona wifi')    #imprimir error de eleccion indicaciones
                                break
                            salir = True
                            while salir: #ciclo while para salir al m,enu principal
                                salir = input('presione 0 para salir: ')
                                if salir == '0':
                                    x1 = menu1()
                                    salir = False

                    else:
                        print('Error sin registro de coordenadas')
                        break

                elif x1 == 4:
                    if (contador2 > 0) & (len(matriz_3) > 0):
                        informacion = {
                                       'actual': [matriz_1[coordenadas_frecuentes - 1][0], matriz_1[coordenadas_frecuentes - 1][1]],
                                       'zonawifi1' : [matriz_3[indicaciones - 1][1][0], matriz_3[indicaciones - 1][1][1], matriz_3[indicaciones - 1][0]],
                                       'recorrido' : [matriz_3[indicaciones - 1][2], 'Bus', (round(matriz_3[1][2] / 16.67))]
                                       }
                        print(informacion)
                        seleccionar = input('¿Esta de acuerdo con la informacion a exportar? Presione 1 para confirmar, 0 para regresar al menú principal?')
                        if seleccionar == '1':
                            print('Exportando archivo')
                            data_json = json.dumps(informacion)
                            archivo_json = open("informacion.json", "w")
                            archivo_json.write(data_json)
                            archivo_json.close()
                            break

                        elif seleccionar == '0':
                            x1 = menu1()
                    else:
                        print('Error de alistamiento')
                        break

                elif x1 == 5:

                    f = open(r"C:\Users\zebas\OneDrive\Escritorio\Mision TIC 2022\informacion.json", "r")
                    content = f.read()
                    jsondecoded = json.loads(content)

                    seleccionar = input('Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal: ')
                    if seleccionar == '0':
                        x1 = menu1()

                elif x1 == 6:

                    x6 = selec_opc()

                    if x6 > 5 or x6 <= 0:
                        print('Error')
                        break

                    if x6 <= 5:

                        x7 = adivinanza1()

                        if x7 == 1:

                            x8 = adivinanza2()

                            if x8 == 7:

                                if x6 == 1:
                                    system("cls")
                                    x1 = menu1()
                                    print(f'Usted ha elegido la opción {x1}')
                                    break

                                elif x6 == 2:
                                    system("cls")
                                    x1 = menu2()
                                    print(f'Usted ha elegido la opción {x1}')
                                    break

                                elif x6 == 3:
                                    system("cls")
                                    x1 = menu3()
                                    print(f'Usted ha elegido la opción {x1}')
                                    break

                                elif x6 == 4:
                                    system("cls")
                                    x1 = menu4()
                                    print(f'Usted ha elegido la opción {x1}')
                                    break

                                elif x6 == 5:
                                    system("cls")
                                    x1 = menu5()
                                    print(f'Usted ha elegido la opción {x1}')
                                    break

                            else:
                                print('Error')
                                continue

                        else:
                            print('Error')
                            continue

                elif x1 == 7:
                    salir = True
                    print('Hasta pronto')

        else:
            print('Error')  # anunciamos error

    else:
        print('Error')  # anunciamos error
else:
    print('Error')  # anunciamos error