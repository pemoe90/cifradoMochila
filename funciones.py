# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Created on Sun Jan  4 18:05:40 2015

@author: pemoe90
"""
import random

    
def generarMochila():
    #funcion para generar la mochila
    primos = [467, 547,751,677,619,379,503,727,167,227]    
    print "Introduzca tamaño de la mochila"    
    tamano = input()
    aleatorio = random.randrange(1,20)
    mochila = [aleatorio]
    suma = aleatorio
    i=1
    for i in range(tamano-1):
        suma = suma+mochila[i]
        numero = suma+random.randrange(1,60)
        mochila.append(numero)
        
    m = mochila[tamano-1]*2 + random.randrange(1,99)
    w = primos[random.randrange(0,9)]
    i = 0
    b=[]
    for i in range (tamano):
        numero = (w*mochila[i])%m
        b.append(numero)
    
    claves = [mochila, m, w, b]
    f = open("clave.txt", "w")
    f.write("Mochila:")
    f.write(str(claves[0]))
    f.write('\n')
    f.write("m:")
    f.write(str(claves[1]))
    f.write('\n')
    f.write("w:")
    f.write(str(claves[2]))
    f.write('\n')
    f.write("clave pública:")
    f.write(str(claves[3]))
    f.write('\n')
    f.close()
    return mochila, m, w, b

def cifradoMochila():
    #funcion para cifrar un documento
    texto = numeroBinario()     
    print 'Tamaño de la clave'
    tamano = input()
    clave = []
    print 'Introduzca clave publica'
    i=0
    while i < tamano:
        print ("Introduzca elemento")
        el = input()
        clave.append(el)
        i=i+1
    print 'Introduzca m'
    m = input()
    if (len(texto)% tamano) !=0:
        i=0
        while i<=(len(texto)%tamano):
            texto = texto +'0'
            i = i+1
    print 'Introduzca nombre del fichero donde se guardara el texto'
    nombre = raw_input()
    fcifrado = open(nombre,"a")
    i=0
    j=0
    suma = 0
    textocifrado=''
    aux = []
    while i<len(texto):
        if j==tamano:
            j=0
            suma = 0
        if texto[i]=='1':
            suma=suma+clave[j]
        if j==tamano-1:
            suma = suma%m
            aux.append(suma)
        i=i+1
        j=j+1
    i=0
    while i < len(aux):
        aux[i]=str(aux[i])
        textocifrado += aux[i]
        textocifrado += ','
        i=i+1
    fcifrado.write(textocifrado)
    fcifrado.close()
    
def descifraMochila():
    #funcion para descifrar un documento
    texto = leerFichero()
    print 'Tamaño de la mochila'
    tamano = input()
    clave = []
    numeros = []
    print 'Introduzca mochila'
    i=0
    while i < tamano:
        print ("Introduzca elemento")
        el = input()
        clave.append(el)
        i=i+1
    print 'Introduzca w'
    w= input ()
    print 'Introduzca m'
    m = input()
    inv = inversoModulo(w,m)
    i=0
    texto = cadenaEntero(texto)
    while i < len(texto):
        texto[i]=(texto[i]*inv)%m
        i=i+1

    numeros = descifraNumero(texto,clave)
    numeros = binarioNumero(numeros)
    descifrado = numeroLetra(numeros)
    descifrado = str(descifrado)
    f = open("descifradomochila.txt", "w")
    f.write(descifrado)
    f.close()

def letranumero (texto):
    #funcion para pasar una cadena a numero
    alfabeto = 'abcdefghijklmnopqrstuvwxyz '
    texto = texto.lower()
    i=0
    j=0
    numeros=[]
    
    while i<len(texto):
        while j < len(alfabeto):
            if texto[i]==alfabeto[j]:
                numeros.append(j)
            j=j+1
        j=0
        i=i+1
        
    return numeros

def numeroBinario():
    #funcion para pasar de un numero a bit de 5 elementos
    nbinarios = ['00000','00001','00010','00011','00100','00101','00110','00111','01000','01001','01010','01011','01100','01101','01110','01111','10000','10001','10010','10011','10100','10101','10110','10111','11000','11001','11010']
      
    texto = leerFichero()  
    
    numeros = letranumero(texto)
    textob = ''
    i=0
    
    while i < len(numeros):
        textob += str(nbinarios[numeros[i]])
        i=i+1

    return textob
    
def leerFichero ():
    #funcion para leer ficheros
    print "Introduzca el nombre del fichero"
    nombre = raw_input()
    f = open (nombre, "r")
    texto = f.read()
    f.close()
    return texto


def numeroLetra(num):
    #funcion para pasar un numero a su letra correspondiente
    alfabeto = 'abcdefghijklmnopqrstuvwxyz '
    i=0
    texto=''
    while i < len(num):
        aux = num[i]
        texto = texto + alfabeto[aux]
        i=i+1
    return texto
    
    
def binarioNumero(texto):
    #funcion para pasar una cadena de 1 y 0 a decimal
    numeros = []
    i=5
    aux = texto[0:5]
    while i<len(texto):
        if i%5==0:
            numeros.append(aux)
            aux=""
            aux = aux + texto[i]
        else:
            aux = aux + texto[i]
        
        i=i+1
    i=0
    decimal = []
    while i<len(numeros):
        decimal.append(int(numeros[i],2))
        i=i+1
    return decimal
    
def descifraNumero (texto, mochila):
    #funcion para conseguir la cadena de binarios al descifrar
    i = 0
    numero=''
    while i < len(texto):
        j=len(mochila)-1
        aux=''
        res = texto[i]
        while j >=0:
            if mochila[j] <= res:
                res = res-mochila[j]
                aux = '1'+aux
            else:
                aux = '0'+aux
            j=j-1
        numero = numero+aux 
        i=i+1
    
    return numero
        
def cadenaEntero(texto):
    #funcion para conseguir los numeros de una cadena
    texto = texto.split(',')
    i=0
    num = []
    while i < len(texto)-1: #-1 porque el ultimo elemento esta vacio
        num.append(int(texto[i]))
        i=i+1
    return num
    
def inversoModulo(w,m):
    #funcion para buscar el inverso de w modulo m
    inv = 1
    while (inv*w)%m!=1:
        inv = inv+1
    return inv

if __name__ == "__main__":
	print inversoModulo(2,11)
