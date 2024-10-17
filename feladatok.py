''' adott egy lista 
lista=[12, 21,56, 32, -5, -23, 35]
1.Hány pozitív szám van benne? 
2.Mennyi a negatív számok összege?
3.Mennyi az öttel osztható számok átlaga?
'''

def poz_szamok_szama(lista):
    print(lista)
    i:int=0
    db:int=0
    while(i<len(lista)):
        '''print(lista[i])'''
        if (lista[i]>0):
            db+=1
        i+=1
    
    return db

def negativ_szamok_osszege(lista):
    i:int=0
    db:int=0
    while(i<len(lista)):
        if(lista[i]<0):
            db+=1
        i+=1
    return db

def ottel_oszthatok_atlaga(lista):
    i:int=0
    db:int=0
    osszeg:int=0
    while(i<len(lista)):
        if(lista[i]%5==0):
            db+=1
            osszeg+=lista[i]
        i+=1
    atlag=osszeg/db
        
    return atlag
        