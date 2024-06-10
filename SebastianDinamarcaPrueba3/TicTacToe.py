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
     #Laterales
     if Mapa[0][0] == sprite and Mapa[0][1] == sprite and Mapa[0][2] == sprite:
        print(f"Ganador Jugador1 ")
        coin = False
     if Mapa[1][0] == sprite and Mapa[1][1] == sprite and Mapa[1][2] == sprite:
        print(f"Ganador Jugador1 ")
        coin = False
     if Mapa[2][0] == sprite and Mapa[2][1] == sprite and Mapa[2][2] == sprite:
        print(f"Ganador Jugador1 ")
        coin = False
     #Verticales
     if Mapa[0][0] == sprite and Mapa[1][0] == sprite and Mapa[2][0] == sprite:
        print(f"Ganador Jugador1 ")
        coin = False
     if Mapa[0][1] == sprite and Mapa[1][1] == sprite and Mapa[2][1] == sprite:
        print(f"Ganador Jugador1 ")
        coin = False
     if Mapa[0][2] == sprite and Mapa[1][2] == sprite and Mapa[2][2] == sprite:
        print(f"Ganador Jugador1 ")
        coin = False
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
     #Laterales
     if Mapa[0][0] == sprite and Mapa[0][1] == sprite and Mapa[0][2] == sprite :
        print(f"Ganador Jugador2 ")
        coin = False
       
     if Mapa[1][0] == sprite and Mapa[1][1] == sprite and Mapa[1][2] == sprite:
        print(f"Ganador Jugador2 ")
        coin = False
       
     if Mapa[2][0] == sprite and Mapa[2][1] == sprite and Mapa[2][2] == sprite:
        print(f"Ganador Jugador2 ")
        coin = False
        
     #Verticales
     if Mapa[0][0] == sprite and Mapa[1][0] == sprite and Mapa[2][0] == sprite:
        print(f"Ganador Jugador2 ")
        coin = False
       
     if Mapa[0][1] == sprite and Mapa[1][1] == sprite and Mapa[2][1] == sprite:
        print(f"Ganador Jugador2 ")
        coin = False
       
     if Mapa[0][2] == sprite and Mapa[1][2] == sprite and Mapa[2][2] == sprite:
        print(f"Ganador Jugador2 ")
        coin = False
        
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
        res=float(input("Player2 Ingrese una posicion usando . (max 3 min 1: )"))

        match res:
            case 1.1:
                if Mapa[0][0]== Sprite or Mapa[0][0]== Sprite2:
                    print("Esta Ocupado")
                else:
                    Mapa[0][0]= Sprite
                    break
            case 1.2:
                if Mapa[0][1]== Sprite or Mapa[0][1]== Sprite2:
                    print("Esta Ocupado")
                else:
                    Mapa[0][1]= Sprite
                    break
            case 1.3:
                if Mapa[0][2]== Sprite or Mapa[0][2]== Sprite2:
                    print("Esta Ocupado")
                else:
                    Mapa[0][2]= Sprite
                    break
            case 2.1:
                if Mapa[1][0]== Sprite or Mapa[1][0]== Sprite2:
                    print("Esta Ocupado")
                else:
                    Mapa[1][0]= Sprite
                    break
            case 2.2:
                if Mapa[1][1]== Sprite or Mapa[1][1]== Sprite2:
                    print("Esta Ocupado")
                else:
                    Mapa[1][1]= Sprite
                    break
            case 2.3:
                if Mapa[1][2]== Sprite or Mapa[1][2]== Sprite2:
                    print("Esta Ocupado")
                else:
                    Mapa[1][2]= Sprite
                    break
            case 3.1:
                if Mapa[2][0]== Sprite or Mapa[2][0]== Sprite2:
                    print("Esta Ocupado")
                else:
                    Mapa[2][0]= Sprite
                    break
            case 3.2:
                if Mapa[2][1]== Sprite or Mapa[2][1]== Sprite2:
                    print("Esta Ocupado")
                else:
                    Mapa[2][1]= Sprite
                    break
            case 3.3:
                if Mapa[2][2]== Sprite or Mapa[2][2]== Sprite2:
                    print("Esta Ocupado")
                else:
                    Mapa[2][2]= Sprite
                    break
            case _:
                print("No es una cordenada")

    return Mapa   
      
def P1(Mapa):
    Sprite="[X]"
    Sprite2= "[O]"
    time.sleep(0.5)
    os.system("cls")

    for i in range(3):
            print(Mapa[i])
    while True:
        res=float(input("Player1 Ingrese una posicion usando . (max 3 min 1: )"))

        match res:
            case 1.1:      #Agregar or Mapa[0][0]== Sprite2
                if Mapa[0][0]== Sprite or Mapa[0][0]== Sprite2:
                    print("Esta Ocupado")
                else:
                    Mapa[0][0]= Sprite
                    break
            case 1.2:
                if Mapa[0][1]== Sprite or Mapa[0][1]== Sprite2:
                    print("Esta Ocupado")
                else:
                    Mapa[0][1]= Sprite
                    break
            case 1.3:
                if Mapa[0][2]== Sprite or Mapa[0][2]== Sprite2:
                    print("Esta Ocupado")
                else:
                    Mapa[0][2]= Sprite
                    break
            case 2.1:
                if Mapa[1][0]== Sprite or Mapa[1][0]== Sprite2:
                    print("Esta Ocupado")
                else:
                    Mapa[1][0]= Sprite
                    break
            case 2.2:
                if Mapa[1][1]== Sprite or Mapa[1][1]== Sprite2:
                    print("Esta Ocupado")
                else:
                    Mapa[1][1]= Sprite
                    break
            case 2.3:
                if Mapa[1][2]== Sprite or Mapa[1][2]== Sprite2:
                    print("Esta Ocupado")
                else:
                    Mapa[1][2]= Sprite
                    break
            case 3.1:
                if Mapa[2][0]== Sprite or Mapa[2][0]== Sprite2:
                    print("Esta Ocupado")
                else:
                    Mapa[2][0]= Sprite
                    break
            case 3.2:
                if Mapa[2][1]== Sprite or Mapa[2][1]== Sprite2:
                    print("Esta Ocupado")
                else:
                    Mapa[2][1]= Sprite
                    break
            case 3.3:
                if Mapa[2][2]== Sprite or Mapa[2][2]== Sprite2:
                    print("Esta Ocupado")
                else:
                    Mapa[2][2]= Sprite
                    break
            case _:
                print("No es una cordenada")
    return Mapa   

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
                win1(Mapa, coin)
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
                win2(Mapa, coin)
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
        res=float(f"{r1}.{r2}")

        match res:
            case 1.1:
                if Mapa[0][0]== Sprite or Mapa[0][0]== Sprite2:
                    continue
                else:
                    Mapa[0][0]= Sprite
                    break
            case 1.2:
                if Mapa[0][1]== Sprite or Mapa[0][1]== Sprite2:
                    continue
                else:
                    Mapa[0][1]= Sprite
                    break
            case 1.3:
                if Mapa[0][2]== Sprite or Mapa[0][2]== Sprite2:
                    continue
                else:
                    Mapa[0][2]= Sprite
                    break
            case 2.1:
                if Mapa[1][0]== Sprite or Mapa[1][0]== Sprite2:
                    continue
                else:
                    Mapa[1][0]= Sprite
                    break
            case 2.2:
                if Mapa[1][1]== Sprite or Mapa[1][1]== Sprite2:
                   continue
                else:
                    Mapa[1][1]= Sprite
                    break
            case 2.3:
                if Mapa[1][2]== Sprite or Mapa[1][2]== Sprite2:
                    continue
                else:
                    Mapa[1][2]= Sprite
                    break
            case 3.1:
                if Mapa[2][0]== Sprite or Mapa[2][0]== Sprite2:
                    continue
                else:
                    Mapa[2][0]= Sprite
                    break
            case 3.2:
                if Mapa[2][1]== Sprite or Mapa[2][1]== Sprite2:
                    continue
                else:
                    Mapa[2][1]= Sprite
                    break
            case 3.3:
                if Mapa[2][2]== Sprite or Mapa[2][2]== Sprite2:
                   continue
                else:
                    Mapa[2][2]= Sprite
                    break
            case _:
              continue

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
            if contador >= 2:
                win1(Mapa, coin)
                coin =  win1(Mapa, coin)
            if coin == False:
                break

        if coin == True:
            Com(Mapa)
            if contador >= 2:
                win2(Mapa, coin)
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