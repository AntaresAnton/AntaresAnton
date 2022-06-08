from os import system
system("cls")
lista_vehiculos = []

flag = True

while flag == True:

    print('======================================\n\033[1m' + 'Bienvenid@ a la serviteca Serviexpress' + '\033[0m\n======================================\n')
    print("¿Qué desea hacer?") 
    

    try:
        opcion=int(input("1.-Registrar Automovil\n2.-Registro Mantenimiento\n3.-Consultar Automovil\n4.-Salir \n"))

        if opcion == 1:
            
            flag_patente = False
            while flag_patente == False:
                try:
                    patente = input('\033[1m' + 'Ingrese la patente - ejemplo AA1111:' + '\033[0m\n\n')
                    
                    if (len(patente) != 6):
                        print("Longitud incorrecta para la patente")
                    if (patente[0:1].isalpha() and patente[2:5].isdigit()):
                        patente.upper()
                        flag_patente = True 
                    if (patente[0:3].isalpha() and patente[4:5].isdigit()):
                        patente.upper()
                        flag_patente = True             
                except:
                    print('\033[1m' + 'Patente ingresada no corresponde, reintenta.' + '\033[0m\n\n')

            flag_marca = False
            while flag_marca == False:
                marca = input('\033[1m' + 'Ingrese la marca del vehículo:' + '\033[0m\n\n').capitalize()
                if marca != "":
                    flag_marca = True
                else:
                    print('\033[1m' + 'Campo oblicatorio *Marca*' + '\033[0m\n')

                if flag_marca == False:
                    print('\033[1m' + 'Algo salió mal :( reintenta' + '\033[0m\n')

            flag_modelo = False
            while flag_modelo == False:
                modelo = input('\033[1m' + 'Ingrese el modelo del vehículo:' + '\033[0m\n\n').capitalize()
                if modelo != "":
                    flag_modelo = True
                else:
                    print('\033[1m' + 'Campo obligatorio *Modelo*' + '\033[0m\n\n')

                if flag_modelo == False:
                    print('\033[1m' + 'Reintente nuevamente' + '\033[0m\n\n')

            flag_año = False
            while flag_año == False:
                try:
                    año = int(input('\033[1m' + 'Ingrese el año de fabricación del vehículo:' + '\033[0m\n\n'))
                    
                    if año >= 1900 and año <= 2021:
                        flag_año = True
                    else:
                        print('\033[1m' + 'El año debe estar en el rango de 1900 y 2021' + '\033[0m\n\n')
                except:
                    print('\033[1m' + 'debe ingresar números' + '\033[0m\n')
            
            flag_ps = False
            while flag_ps == False:
                tipo_vehiculo = input("==============================================================\nMencione el tipo de Vehículo utilizando los siguientes términos \n B.-Bencinero \n D.-Diesel \n E.-Eléctrico \n H.-Híbrido \n\n (no distingue minúsculas de mayúsculas)\n==============================================================\n").upper()

                if tipo_vehiculo == 'B' or tipo_vehiculo == 'D' or tipo_vehiculo == 'E'or tipo_vehiculo == 'H':
                    flag_ps = True
                else:
                    print('\033[1m' + 'Debe ingresar los datos de acuerdo a lo indicado' + '\033[0m\n')

                registros = input('\033[1m' + 'Ingrese los registros del vehículo' + '\033[0m\n')
                print('\033[1m' + '========== Información ingresada de forma exitosa ==========' + '\033[0m\n\n')

            lista_vehiculos.append([patente, marca, modelo, año, tipo_vehiculo, registros, []])

        elif opcion == 2:
            try:
                consulta_patente = input('\033[1m' + 'Ingrese la patente del vehículo' + '\033[0m\n')

                for l in lista_vehiculos:
                    if l[0] == consulta_patente:
                        fecha = input('\033[1m' + 'Ingrese la fecha de atención (DD/MM/AAAA)' + '\033[0m\n')
                        observacion = input('\033[1m' + 'Ingrese las observaciones de la consulta' + '\033[0m\n')

                        l[6].append([fecha, observacion])
                        print('\033[1m' + 'la consulta fué ingresada correctamente' + '\033[0m\n')
                        break
                    
            except:
                print('\033[1m' + 'La patente debe ingresarla como AA1111 ó AAAA11' + '\033[0m\n')

        elif opcion == 3:
            try:
                consulta_patente = input('\033[1m' + 'Ingrese la patente del vehículo' + '\033[0m\n')

                for l in lista_vehiculos:
                    if l[0] == consulta_patente:
                        print('\033[1m' + '\n=======================  Datos del vehículo: =======================' + '\033[0m\n')
                        print('\033[1m' + 'Patente del vehículo:' + '\033[0m',l[0])
                        print('\033[1m' + 'Marca del vehículo:' + '\033[0m',l[1])
                        print('\033[1m' + 'Modelo del vehículo:' + '\033[0m',l[2])
                        print('\033[1m' + 'Año de fabricación del vehículo:' + '\033[0m',l[3])
                        print('\033[1m' + 'Tipo de vehículo:' + '\033[0m',l[4])
                        print('\033[1m' + 'Registros del vehículo:' + '\033[0m',l[5])

                        for x in l[6]:
                            print('\033[1m' + 'Fecha de atención:' + '\033[0m',x[0])
                            print('\033[1m' + 'Observaciones:' + '\033[0m',x[1])
                            print('\033[1m' + '\n===============  Datos entregados satisfactoriamente  ===============' + '\033[0m\n')

                        break
                    
            except:
                print('\033[1m' + '¡Successfull!' + '\033[0m\n')
        elif opcion == 4:
            print('\033[1m' + 'Gracias por utilizar nuestra aplicación' + '\033[0m\n')
            print('\033[1m' + 'Cerrando... ' + '\033[0m\n')
            flag = False
        else:
            print('\033[1m' + 'La opción seleccionada no es válida' + '\033[0m\n')

    except:
        print('\033[1m' + 'La opción ingresada no es válida - Reintenta' + '\033[0m\n')
