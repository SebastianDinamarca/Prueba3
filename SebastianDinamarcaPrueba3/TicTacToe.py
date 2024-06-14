import os 
import time
import random

def empate(Mapa, coin):

    sprite="[X]"
    sprite2="[O]"
    c=0
    for i in range(3):
        for a in range(3):
            if Mapa[i][a] == sprite or Mapa[i][a] == sprite2:
                c+=1
            if c == 9 :
                print("Empate")       
                coin=False
                return coin         

def win1(Mapa,coin):

    sprite="[X]"

     #laterales
    for i in range(0,3):
        if Mapa[i][0] == sprite and Mapa[i][1] == sprite and Mapa[i][2] == sprite:
            print(f"Ganador Jugador1 ")
            coin = False 

     #Verticales
    for i in range(0,3):
        if Mapa[0][i] == sprite and Mapa[1][i] == sprite and Mapa[2][i] == sprite:
            print(f"Ganador Jugador1 ")
            coin= False

     #Diagonales
    if Mapa[0][0] == sprite and Mapa[1][1] == sprite and Mapa[2][2] == sprite:
        print(f"Ganador Jugador1 ")
        coin = False
        
    if Mapa[0][2] == sprite and Mapa[1][1] == sprite and Mapa[2][0] == sprite:
        print(f"Ganador Jugador1 ")
        coin = False
        
    time.sleep(0.5)
    return coin

def win2(Mapa,coin): 
    #Jugador 2
    sprite="[O]"

     #laterales
    for i in range(0,3):
        if Mapa[i][0] == sprite and Mapa[i][1] == sprite and Mapa[i][2] == sprite:
            print(f"Ganador Jugador2 ")
            coin = False 

     #Verticales
    for i in range(0,3):
        if Mapa[0][i] == sprite and Mapa[1][i] == sprite and Mapa[2][i] == sprite:
            print(f"Ganador Jugador2 ")
            coin= False

     #Diagonales
    if Mapa[0][0] == sprite and Mapa[1][1] == sprite and Mapa[2][2] == sprite:
        print(f"Ganador Jugador2 ")
        coin = False
        
    if Mapa[0][2] == sprite and Mapa[1][1] == sprite and Mapa[2][0] == sprite:
        print(f"Ganador Jugador2 ")
        coin = False

    time.sleep(0.5)
    return coin

def P2(Mapa):
    Sprite="[O]"
    Sprite2="[X]"
    time.sleep(0.5)
    os.system("cls")
    for i in range(3):
             print(Mapa[i])
    while True:
        res=input("Player2 Ingrese una posicion usando . (max 3 min 1: )")

        for i in range(0, 3):
            for a in range(0, 3):
             x=f"{i+1}.{a+1}"
             if res == x:
                if Mapa[i][a]== Sprite or Mapa[i][a]== Sprite2:
                    print("Esta Ocupado")
                elif Mapa[i][a]!= Sprite or Mapa[i][a]!= Sprite2:
                    Mapa[i][a]= Sprite
                    return Mapa
                else:
                    print("no es una cordenada")
            else:
                a=False
        if a == False:
            print("Ingrese una opcion valida")
             
def P1(Mapa):
    Sprite="[X]"
    Sprite2= "[O]"
    time.sleep(0.5)
    os.system("cls")
    for i in range(3):
            print(Mapa[i])
    while True:
        res=input("Player1 Ingrese una posicion usando . (max 3 min 1: )")
        for i in range(0, 3):
            for a in range(0, 3):
             x=f"{i+1}.{a+1}"
             if res == x:
                if Mapa[i][a]== Sprite or Mapa[i][a]== Sprite2:
                    print("Esta Ocupado")
                elif Mapa[i][a]!= Sprite or Mapa[i][a]!= Sprite2:
                    Mapa[i][a]= Sprite
                    return Mapa
                else:
                    print("no es una cordenada")
             else:
                a=False
        if a == False:
            print("Ingrese una opcion valida")
           
def P1P2():
    Mapa=[["[ ]","[ ]","[ ]"],
          ["[ ]","[ ]","[ ]"],
          ["[ ]","[ ]","[ ]"]]
    coin= True
    contador=0

    while coin:
        time.sleep(0.5)
        os.system("cls")
        
        for i in range(3):
            print(Mapa[i])

        if coin == True:
            P1(Mapa)
            contador+=1
            if contador >= 2:
                coin =  win1(Mapa, coin)
            if coin == False:
                break

        if contador == 9:
            print("GG empate")
            break

        if coin == True:
            P2(Mapa)
            contador+=1
            if contador >= 2:
                coin =  win2(Mapa, coin)
            if coin == False:
                break
        
def Com(Mapa):

    Sprite="[O]"
    Sprite2="[X]"
    time.sleep(0.5)
    os.system("cls")
    for i in range(3):
            print(Mapa[i])
    while True:
        r1 = random.randint(1, 3)
        r2 = random.randint(1, 3)
        res=f"{r1}.{r2}"


        for i in range(0, 3):
            for a in range(0, 3):
             x=f"{i+1}.{a+1}"
             if res == x:
                if Mapa[i][a]== Sprite or Mapa[i][a]== Sprite2:
                    continue
                elif Mapa[i][a]!= Sprite or Mapa[i][a]!= Sprite2:
                    Mapa[i][a]= Sprite
                    return Mapa
        
def P1Com():
    Mapa=[["[ ]","[ ]","[ ]"],
          ["[ ]","[ ]","[ ]"],
          ["[ ]","[ ]","[ ]"]]
    coin= True
    contador=0

    while coin:
        time.sleep(0.5)
        os.system("cls")
      
        for i in range(3):
            print(Mapa[i])

        if coin == True:
            P1(Mapa)
            contador+=1
            if contador >= 2:
                coin =  win1(Mapa, coin)
            if coin == False:
                break

        if contador == 9:
            print("GG empate")
            break

        if coin == True:
            Com(Mapa)
            contador+=1
            if contador >= 2:
                coin =  win2(Mapa, coin)
            if coin == False:
                break
        
        contador+=1

def menu():
    os.system("cls")
    while True:
        res= int(input("""
        1.Player vs Player
        2.Player vs COM
        3.Salir  

        Ingrese una opcion:         
        """))
        match res:
            case 1:
                P1P2()
            case 2:
                P1Com()
            case 3: 
                break
            case _:
                print("Ingrese una opcion valida")

        time.sleep(0.5)
        os.system("cls")
        
menu()