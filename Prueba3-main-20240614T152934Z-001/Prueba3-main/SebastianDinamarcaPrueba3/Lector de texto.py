archivo= open( "aaa.txt", "r")
texto=archivo.read()
contador=0
for letra in texto:
    if letra == " ":
        contador +=1
length=len(texto)

ArchivoN= open("Nex.txt", "x")
ArchivoN.write(f"Tiene {contador} espacios y {length-contador} letras")
ArchivoN.close()