import random

piedra = 'piedra'
papel = 'papel'
tijeras = 'tijera'
opciones = [piedra, papel, tijeras]
ganaJugador = [[papel, piedra], [tijeras, papel], [piedra, tijeras]]
ganaOrdenador = [[piedra, papel], [papel, tijeras], [tijeras, piedra]]


def opcionRandom():
    return random.choice(opciones)


def comprobarGanador(opcionJugador, opcionOrdenador):
    if [opcionJugador, opcionOrdenador] in ganaJugador:
        return 1
    elif [opcionJugador, opcionOrdenador] in ganaOrdenador:
        return -1
    return 0


jugador1 = 0
jugador2 = 0

print("Joc : Pedra, paper y tisora")

while True:
    intentos = int(input("Dime numero de intentos, tiene que ser impar y mayor de 3 menor de 99: "))
    if intentos % 2 != 0 and 3 <= intentos <= 99:
        break
    else:
        print("Numero no valido")
cont = 0
while cont < intentos:
    compruebaJuega = input("Vols jugar? (s/n): ")
    if 's' in compruebaJuega.lower():
        jugarConOtro = input("Quieres jugar con el ordenador (o) o con otro jugador (j)")
        if 'o' in jugarConOtro:
            elecionOrdenador = opcionRandom()
        while True:
            if 'j' in jugarConOtro:
                print("No mires jugador 2")
            elecionJugador = input("Selecciona un moviment ('p' per a pedra / 'a' per a paper / 't' per a tisores): ").lower()

            if 'j' in jugarConOtro:
                print("No mires jugador 1")
                elecionOrdenador = input("Selecciona un moviment ('p' per a pedra / 'a' per a paper / 't' per a tisores): ").lower()
                if 'p' in elecionOrdenador or 'a' in elecionOrdenador or 't' in elecionOrdenador:
                    if 'p' in elecionOrdenador:
                        elecionOrdenador = piedra
                    elif 'a' in elecionOrdenador:
                        elecionOrdenador = papel
                    elif 't' in elecionOrdenador:
                        elecionOrdenador = tijeras
                else:
                    print("Entrada incorrecta. Torna a intentar.")
                    break

            if 'p' in elecionJugador or 'a' in elecionJugador or 't' in elecionJugador:
                opcionJugador = ""
                if 'p' in elecionJugador:
                    opcionJugador = piedra
                elif 'a' in elecionJugador:
                    opcionJugador = papel
                elif 't' in elecionJugador:
                    opcionJugador = tijeras

                print(f"Eleccio del usuari: {opcionJugador}")
                print(f"Eleccio del ordinador/usuari2: {elecionOrdenador}")

                if comprobarGanador(opcionJugador, elecionOrdenador) == 1:
                    print("Gana l'usuari1 !!!")
                    jugador1 += 1
                elif comprobarGanador(opcionJugador, elecionOrdenador) == -1:
                    print("Gana l'ordinador/usuari2 !!!")
                    jugador2 += 1
                elif comprobarGanador(opcionJugador, elecionOrdenador) == 0:
                    print("Empate !!!")
                break
            else:
                print("Entrada incorrecta. Torna a intentar.")
    elif 'n' in compruebaJuega.lower():
        break
    else:
        print('Entrada incorrecta. Torna a intentar.')
    print()
    cont+= 1

if "s" in compruebaJuega:
    if jugador1 > jugador2:
        print("Ganador total l'usuari1 !!!")
    elif jugador2 > jugador1:
        print("Ganador total l'ordinador/usuari2 !!!")
    else:
        print("Al final fue Empate !!!")