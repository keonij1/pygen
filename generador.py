def generador(li=[1,2,3,4,5,6],indice=5,ranA=1,ranB=45):
    #5 864 443 200
    #8 145 060
    result=[]
    #gen=range(ranA,ranB+1)
    count=0
    terminar=0
    while True:
        if li[indice]==45:
            li[indice]=1
            li[indice-1]+=1
        else:
            li[indice]+=1
        if li[indice-1] == 45:
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
            break
        #Eliminacion de numeros repetidos

        if li[5]>li[4]>li[3]>li[2]>li[1]>li[0]:
            result.append(li)
                ## tester
            terminar+=1
            #debug
            print(terminar,li)
        #debug
        if terminar==1000:
            break
        #end tester
    return li
prueba=generador()
