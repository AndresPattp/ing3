class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0
        self.partidos_jugados = 0
        self.goles_favor = 0
        self.goles_contra = 0

    def actualizar_estadisticas(self, goles_favor, goles_contra):
        self.partidos_jugados += 1
        self.goles_favor += goles_favor
        self.goles_contra += goles_contra
        
        if goles_favor > goles_contra:
            self.puntos += 3
        elif goles_favor == goles_contra:
            self.puntos += 1

class TablaPosiciones:
    def __init__(self):
        self.equipos = []

    def agregar_equipo(self, nombre):
        equipo = Equipo(nombre)
        self.equipos.append(equipo)

    def actualizar_resultado(self, equipo_local, equipo_visitante, goles_local, goles_visitante):
        for equipo in self.equipos:
            if equipo.nombre == equipo_local:
                equipo.actualizar_estadisticas(goles_local, goles_visitante)
            elif equipo.nombre == equipo_visitante:
                equipo.actualizar_estadisticas(goles_visitante, goles_local)

    def mostrar_tabla(self):
        print("\nTabla de Posiciones:")
        print("Equipo | PJ | PTS | GF | GC | DIF")
        print("-" * 35)
        equipos_ordenados = sorted(self.equipos, key=lambda x: x.puntos, reverse=True)
        for equipo in equipos_ordenados:
            dif_goles = equipo.goles_favor - equipo.goles_contra
            print(f"{equipo.nombre:<10} | {equipo.partidos_jugados:2} | {equipo.puntos:3} | {equipo.goles_favor:2} | {equipo.goles_contra:2} | {dif_goles:3}")


tabla = TablaPosiciones()


equipos = ["Brasil", "Argentina", "Colombia", "Chile"]
for equipo in equipos:
    tabla.agregar_equipo(equipo)


while True:
    print("\n1. Ingresar resultado")
    print("2. Mostrar tabla de posiciones")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        equipo_local = input("Equipo local: ")
        equipo_visitante = input("Equipo visitante: ")
        goles_local = int(input("Goles del equipo local: "))
        goles_visitante = int(input("Goles del equipo visitante: "))
        tabla.actualizar_resultado(equipo_local, equipo_visitante, goles_local, goles_visitante)
    elif opcion == "2":
        tabla.mostrar_tabla()
    elif opcion == "3":
        break
    else:
        print("Opción no válida. Intente de nuevo.")

print("Gracias por usar el programa.")