## Programa credenciales reto 1 mision tic 2022

print('Bienvenido al sistema de ubicación para zonas públicas WIFI')    #mensaje de beinvenida

nombre_usuario = '51617'    #asignacion nombre de usuario
contraseña = '71615'    #asignacion contraseña

nombre_usuario_2 = input('ingrese el nombre de usurario: ')   #ingreso de la contraseña por parte del usuario

if nombre_usuario_2 == nombre_usuario:  #verificamos que el usuario exista
    
    contraseña_usuario = input('ingrese la contraseña: ') #solicitamos la contraseña

    if contraseña_usuario == contraseña:    #verificamos que la contraseña sea correcta

        #calculo del captcha para codigo 51617

        num1 = 617  #primer numero
        num2 = int((7*7)/49) #segundo numero
        captcha = num1 + num2   #suma final
        print(f'captcha {num1} + {num2}')
        captcha_usuario = int(input('ingrese el valor de la suma mostrada en el captcha: '))   #se solicita la suma del captcha

        if captcha_usuario == captcha:  #verificamos el la coinicdencia del captcha
            print('Sesión iniciada')    #concedemos acceso
        else:
            print('Error')  #anunciamos error
        
    else:
        print('Error')  #anunciamos error
else:
    print('Error')  #anunciamos error

