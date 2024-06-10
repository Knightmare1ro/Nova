Grados= int(input("Bienvenido coloque la temperatura que quiere convertir: "))
Sistem= int(input("Elija en que sistema está actualmente (1)Celsius (2)Farenheit: "))

if Sistem == 1:
    while (Grados>101) or (Grados<-1): 
        print("Temperatura irreal")
        break
    print((Grados*9/5)+32)

if Sistem == 2:
    while (Grados>212) or (Grados<32): 
        print("Temperatura irreal")
        break
    print((Grados-32)*5/9)




