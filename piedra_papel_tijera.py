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


print("JUEGO : Piedra, papel y tijera")
while 1:
    compruebaJuega = input("Quieres jugar? (s/n): ")
    if 's' in compruebaJuega.lower():
        elecionOrdenador = opcionRandom()
        while True:
            elecionJugador = input("Selecciona un movimiento ('p' para piedra / 'a' para papel / 't' para tijeras): ").lower()
            print(f"Elección del ordenador: {elecionOrdenador}")
            if 'p' in elecionJugador or 'a' in elecionJugador or 't' in elecionJugador:
                opcionJugador = ""
                if 'p' in elecionJugador:
                    opcionJugador = piedra
                elif 'a' in elecionJugador:
                    opcionJugador = papel
                elif 't' in elecionJugador:
                    opcionJugador = tijeras

                print(f"Elección del usuario: {opcionJugador}")

                if comprobarGanador(opcionJugador, elecionOrdenador) == 1:
                    print("Gana el usuario !!!")
                elif comprobarGanador(opcionJugador, elecionOrdenador) == -1:
                    print("Gana el ordenador !!!")
                elif comprobarGanador(opcionJugador, elecionOrdenador) == 0:
                    print("Empate !!!")
                break
            else:
                print("Entrada incorrecta. Vuelve a intentar.")
    elif 'n' in compruebaJuega.lower():
        break
    else:
        print('Entrada incorrecta. Vuelve a intentar.')
    print()
