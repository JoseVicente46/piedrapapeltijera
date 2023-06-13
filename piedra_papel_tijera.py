import random

piedra = 'piedra'
papel = 'papel'
tijeras = 'tijera'
spok = "spok"
opciones = [piedra, papel, tijeras, spok]
ganaJugador = [[papel, piedra], [tijeras, papel], [piedra, tijeras], [spok, papel], [tijeras, spok], [piedra, spok]]
ganaOrdenador = [[piedra, papel], [papel, tijeras], [tijeras, piedra], [papel, spok], [spok, tijeras], [spok, piedra]]


def opcionRandom():
    return random.choice(opciones)


def comprobarGanador(opcionJugador, opcionOrdenador):
    if [opcionJugador, opcionOrdenador] in ganaJugador:
        return 1
    elif [opcionJugador, opcionOrdenador] in ganaOrdenador:
        return -1
    return 0


vectorSi = ["Si", "s", "S", "SI", "Y", "sí", "SÍ", "si"]
print("Joc : Pedra, paper y tisora")
while 1:
    compruebaJuega = input("Vols jugar? (si/n): ")
    if compruebaJuega in vectorSi:
        elecionOrdenador = opcionRandom()
        while True:
            elecionJugador = input(
                "Selecciona un moviment ('p' per a pedra / 'a' per a paper / 't' per a tisores / 's' per a spok): ").lower()
            print(f"Eleccio del ordinador: {elecionOrdenador}")
            if 'p' in elecionJugador or 'a' in elecionJugador or 't' in elecionJugador or 's' in elecionJugador:
                opcionJugador = ""
                if 'p' in elecionJugador:
                    opcionJugador = piedra
                elif 'a' in elecionJugador:
                    opcionJugador = papel
                elif 't' in elecionJugador:
                    opcionJugador = tijeras
                elif 's' in elecionJugador:
                    opcionJugador = spok

                print(f"Eleccio del usuari: {opcionJugador}")

                if comprobarGanador(opcionJugador, elecionOrdenador) == 1:
                    print("Gana l'usuari !!!")
                elif comprobarGanador(opcionJugador, elecionOrdenador) == -1:
                    print("Gana l'ordinador !!!")
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
