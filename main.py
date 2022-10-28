from ejercicios.starWars import *
from ejercicios.regladesarrus import *
from ejercicios.hanoi import *
import unittest
def iniciar():
    while True:
        print(' Ejercicio 1')
        print(' Ejercicio 2')
        print(' Ejercicio 3')
        print(' Ejercicio 4')
        print(' Ejercicio 5')
        print('Salir')
        eleccion = int(input('Seleccione una opcion:'))
        if eleccion == 1:
            print('Ejercicio 1')
            jugarHanoi()
        elif eleccion == 2:
            print('Ejercicio 2')
            filas(0,matriz,0)
            print(matriz)
            print(determinante(matriz))
            unittest.main()
        elif eleccion == 3:
            while True:
                print('1.listado ordenado por nombre de las naves de manera ascendente')
                print('2.listado ordenado por largo de las naves de manera descendente')
                print('3.mostrar toda la información del “Halcón Milenario” y la “Estrella de la Muerte”')
                print('4.determinar cuáles son las cinco naves con mayor cantidad de pasajeros')
                print('5.indicar cuál es la nave que requiere mayor cantidad de tripulación')
                print('6.mostrar todas las naves que comienzan con AT')
                print('7.listar todas las naves que pueden llevar seis o más pasajeros')
                print('8.mostrar toda la información de la nave más pequeña')
                print('9.mostrar toda la información de la nave más grande')           
                apartado = int(input('Elige un apartado: '))

                if apartado == 1:
                    print('ap1',ordenarNombre([v1, v2, v3, v4, v5, v6]))
                elif apartado == 2:
                    print('ap2',ordenarLargo([v1, v2, v3, v4, v5, v6]))
                elif apartado == 3:
                    print('ap3',obtenerDatos([v1, v2, v3, v4, v5, v6]))
                elif apartado == 4:
                    print('ap4',obtenerTripulantes([v1, v2, v3, v4, v5, v6]))
                elif apartado == 5:
                    print('ap5',obtenerNave([v1, v2, v3, v4, v5, v6]))
                elif apartado == 6:
                    print('ap6',obtenerNaveAT([v1, v2, v3, v4, v5, v6]))
                elif apartado == 7:
                    print('ap7',obtenerNaveTripulantes([v1, v2, v3, v4, v5, v6]))
                elif apartado == 8:
                    print('ap8',obtenerNavePequeña([v1, v2, v3, v4, v5, v6]))
                elif apartado == 9:
                    print('ap9',obtenerNaveGrande([v1, v2, v3, v4, v5, v6]))
                else:
                    print('Opcion no valida')
                unittest.main()
        elif eleccion == 4:
            print('Ejercicio 4')

        elif eleccion == 5:
            print('Ejercicio 5')
        elif eleccion == 6:
            print('Salir')
            break
        else:
            print('Opcion no valida')
                 