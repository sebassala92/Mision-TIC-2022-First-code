from os import system

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

def adivinanza1():
    opcion7 = int(input('Primera adivinanza: “Para confirmar por favor\n'
                        'responda: Si me giras pierdo tres unidades por\n'
                        'eso debes colocarme siempre de pie, la respuesta es”: '))  # solicitar la respuesta a la adivinanza: respuesta 9
    return opcion7

def adivinanza2():
    opcion8 = int(input('Segunda adivinanza: “Para confirmar por favor\n'
                        'responda: Me separaron de mi hermano siamés,\n'
                        'antes era un ocho y ahora soy un... la respuesta es”: '))  # solicitar la respuesta a la adivinanza: respuesta 3
    return opcion8


print('Bienvenido al sistema de ubicación para zonas públicas WIFI')  # mensaje de beinvenida

nombre_usuario = '51617'  # asignacion nombre de usuario
contraseña = '71615'  # asignacion contraseña

nombre_usuario_2 = input('ingrese el nombre de usurario: ')  # ingreso de la contraseña por parte del usuario

if nombre_usuario_2 == nombre_usuario:  # verificamos que el usuario exista

    contraseña_usuario = input('ingrese la contraseña: ')  # solicitamos la contraseña

    if contraseña_usuario == contraseña:  # verificamos que la contraseña sea correcta

        # calculo del captcha para codigo 51617

        num1 = 617  # primer numero
        num2 = int((7 * 7) / 49)  # segundo numero
        captcha = num1 + num2  # suma final
        print(f'captcha {num1} + {num2}')
        captcha_usuario = int(
            input('ingrese el valor de la suma mostrada en el captcha: '))  # se solicita la suma del captcha

        if captcha_usuario == captcha:  # verificamos el la coinicdencia del captcha
            print('Sesión iniciada')  # concedemos acceso



            x1 = menu1() #llamar a la funcion menu
            contador1 = 0
            salir = False

            while not salir:  #ciclo while para ejecutar las opciones del menu

                if x1 > 7 or x1 <= 0:
                    if contador1 < 3:
                        contador1 += 1
                        print('Error\nElija una opcion')
                        x1 = menu1()  # mostrar nuevamente el menu
                        continue

                    elif contador1 == 3:
                        print('Error')
                        break

                elif x1 == 1:
                    print(f'Usted ha elegido la opción {x1}')
                    break

                elif x1 == 2:
                    print(f'Usted ha elegido la opción {x1}')
                    break

                elif x1 == 3:
                    print(f'Usted ha elegido la opción {x1}')
                    break

                elif x1 == 4:
                    print(f'Usted ha elegido la opción {x1}')
                    break

                elif x1 == 5:
                    print(f'Usted ha elegido la opción {x1}')
                    break

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
                    salir = False
                    print('Hasta pronto')
                    break

        else:
            print('Error')  # anunciamos error

    else:
        print('Error')  # anunciamos error
else:
    print('Error')  # anunciamos error