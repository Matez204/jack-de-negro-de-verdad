from juego import *
import os,time,sys 
juego = Juego()
juego.ini()
def espera():
    for i in range(3):
        print("\r."+"."*(i),end="")
        time.sleep(1)
    print("")
print("\nBienvenido a un juego de blacka jack, jugaras contra la casa.\
    \nYa esta repartiendo las cartas")
espera()
juego.mostrar_juego() 
if juego.jug.dar_val()==21:
    print("Te salio un Black Jack :D \nMiremos las cartas de la casa.")
    print("Las cartas de la casa son:")
    juego.casa.mostrar_cartas()
    if juego.jug.dar_val==juego.casa.dar_val():
        print("Empate :o")
        sys.exit()
    elif juego.jug.dar_val>juego.casa.dar_val():
        print("Ganaste ")
        sys.exit()
    else:
        print("Perdiste")
        sys.exit()
print("¿Te plantas o pides otra carta? 1.pedir 2.plantar")
el=int(input("")) 
while el!=2:
    juego.jug.agregar_carta(juego.mazo.dar_carta())
    print("Tus cartas son: ")
    juego.jug.mostrar_cartas(True)
    if juego.jug.dar_val()>21:
        print("Te pasaste de 21 :c \nLas cartas de la casa eran: ")
        juego.casa.mostrar_cartas(True)
        print("Perdiste >:c")
        sys.exit()
    print("¿Te plantas o pides otra carta? 1.pedir 2.plantar")
    el=int(input(""))
if juego.casa.dar_val()<18:
    print("La casa esta tomando cartas:")
    while juego.casa.dar_val()<18:
        juego.casa.agregar_carta(juego.mazo.dar_carta())
        print("Las cartas de la casa son ")
        juego.casa.mostrar_cartas(True)
        time.sleep(1)
        if juego.casa.dar_val()>21:
            print("La casa se paso de 21 :D \nGanaste ")
            sys.exit()
else:
    print("Las cartas de la casa son ")
    juego.casa.mostrar_cartas(True)
espera()
if juego.jug.dar_val()==juego.casa.dar_val():
        print("Empate :o")
        sys.exit()
elif juego.jug.dar_val()>juego.casa.dar_val():
    print("Ganaste ")
    sys.exit()
else:
    print("Perdiste")
    sys.exit()

    

# for i in range(10):
#     # Construye la cadena con el progreso y los puntos
#     progress_string = "\rProgreso: " + str(i) + "%" + " " + "." * (i % 4)
    
#     # Imprime la cadena sin un salto de línea
#     print(progress_string, end='')
    
#     # Espera 1 segundo
#     time.sleep(1)
# os.system("cls")