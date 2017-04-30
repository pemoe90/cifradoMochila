# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
Created on Sun Jan  4 11:19:42 2015

@author: pemoe90
"""
import sys
import funciones 

def menu():
    opcion = 4
    while opcion !=0:
        print "-------------------------------"
        print ("Introduzca opción")
        print ("1.Generar clave pública")
        print ("2.Cifrar texto")
        print ("3.Descifrar documento")
        print ("0.Salir")
        opcion = input()
        if opcion == 0: 
            sys.exit(1)
                
        elif opcion == 1: 
           funciones.generarMochila()
           
                
        elif opcion == 2:
            funciones.cifradoMochila()
            
                
        elif opcion == 3:
            funciones.descifraMochila()
            
            
        else:
            print ("La opción escogida no es válida")

if __name__ == "__main__":
   menu()