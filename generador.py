# -*- coding: utf-8 -*-
def generador(li=[1,2,3,4,5,6],indice=5):
    #5 864 443 200 nPr
    #8 145 060     nCr
    result=[] #lista para almazenar resultados
    count=0 #inicialización de variables
    terminar=0
    while True:
        if li[indice]==45:
            li[indice]=1
            li[indice-1]+=1
            #reloj basico, cuando la ultima posición llego a limite, 45; esta vuelve a valer 1, y suma uno a la anterior poscisión
        else:
            li[indice]+=1
        if li[indice-1] == 45:
            #condicional para no avanzar a mas de 45,y saber donde parar
            if li[indice-5]+li[indice-4]+li[indice-3]+li[indice-2]+li[indice-1]==45*5:
                pass
            else:
                li[indice-1]=1
                li[indice-2]+=1
        if li[indice-2]==45:
            if li[indice-5]+li[indice-4]+li[indice-3]+li[indice-2]==45*4:
                pass
            else:                
                li[indice-2]=1
                li[indice-3]+=1
        if li[indice-3]==45:
            if li[indice-5]+li[indice-4]+li[indice-3]==45*3:
                pass
            else:
                li[indice-3]=1
                li[indice-4]+=1
        if li[indice-4]==45:
            if li[indice-5]+li[indice-4]==45*2:
                pass
            else:
                li[indice-4]=1
                li[indice-5]+=1
        if li[indice-5]==45*1:
            pass
        if li==[45,44,43,42,41,40]:
            #donde terminar la creacion de valores
            break
        
        #Eliminacion de numeros repetidos
        #se dejan solo las combinaciones
        if li[5]>li[4]>li[3]>li[2]>li[1]>li[0]:
            result.append(li)
            ## teste0
            terminar+=1
            #debug
            print(terminar,li)
            #debug
        if terminar==1000:
            break
        #end tester
    return li
prueba=generador()
