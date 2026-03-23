from dominio import Mascota, Perro, Gato, Robot
from ui_consola import Consola


class Game:
    """Motor del juego. Inicializa, coordina turnos y determina el fin."""

    MASCOTAS_DISPONIBLES = {
        "1": ("Perro",  Perro),
        "2": ("Gato",   Gato),
        "3": ("Robot",  Robot),
    }

    ACCIONES = {
        "1": "alimentar",
        "2": "jugar",
        "3": "dormir",
        "4": "estado",
        "5": "salir",
    }

    def __init__(self):
        self.__mascota: Mascota | None = None
        self.__turno = 0
        self.__activo = False

    # ── Inicio ────────────────────────────────────────────────────────────────

    def iniciar(self):
        Consola.bienvenida()

        tipo_key = Consola.pedir_tipo_mascota(self.MASCOTAS_DISPONIBLES)
        nombre   = Consola.pedir_nombre()

        _, ClaseMascota = self.MASCOTAS_DISPONIBLES[tipo_key]
        self.__mascota = ClaseMascota(nombre)

        Consola.mostrar_mensaje(
            f"\n¡{self.__mascota.nombre} ha llegado a tu vida! "
            f"{self.__mascota.sonido_caracteristico()}\n"
        )

        self.__activo = True
        self.__loop_principal()

    # ── Loop principal ────────────────────────────────────────────────────────

    def __loop_principal(self):
        while self.__activo:
            self.__turno += 1
            accion_key = Consola.pedir_accion(self.__turno)
            self.__procesar_accion(accion_key)

            if not self.__determinar_fin():
                self.__mascota.pasar_turno()

    # ── Procesamiento de acciones ─────────────────────────────────────────────

    def __procesar_accion(self, key: str):
        accion = self.ACCIONES.get(key)

        if accion == "alimentar":
            resultado = self.__mascota.alimentar()
            Consola.mostrar_resultado(resultado)

        elif accion == "jugar":
            resultado = self.__mascota.jugar()
            Consola.mostrar_resultado(resultado)

        elif accion == "dormir":
            resultado = self.__mascota.dormir()
            Consola.mostrar_resultado(resultado)

        elif accion == "estado":
            Consola.mostrar_estado(self.__mascota.get_estado())

        elif accion == "salir":
            Consola.mostrar_mensaje("Hasta la próxima. Tu mascota te va a extrañar...")
            self.__activo = False

        else:
            Consola.mostrar_mensaje("Opción inválida. Intentá de nuevo.")
            self.__turno -= 1  # no contar el turno fallido

    # ── Fin de partida ────────────────────────────────────────────────────────

    def __determinar_fin(self) -> bool:
        """Devuelve True si el juego terminó."""
        if not self.__mascota.esta_vivo():
            Consola.mostrar_muerte(self.__mascota.nombre, self.__turno)
            self.__activo = False
            return True
        return False
