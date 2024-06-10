import os 
import time

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
     time.sleep(1)
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
        
     
     time.sleep(1)
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
        os.system("cls")
        time.sleep(0.5)
      
        for i in range(3):
            print(Mapa[i])

        P1(Mapa)
        if contador >= 2:
          win1(Mapa, coin)
        P2(Mapa)
        if contador >= 2:
          win2(Mapa, coin)
        contador+=1

        coin= win1(Mapa, coin)
        coin= win2(Mapa, coin)

def menu():
 
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
            Sing()
        case 3: 
            break
        case _:
            print("Ingrese una opcion valida")
            os.system("cls")
            time.sleep(0.5)
menu()