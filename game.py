"""
Módulo que contiene el motor principal del juego.
Coordina la selección de mascota, el loop de turnos y la detección del fin de partida.
"""

from clase_padre import Mascota
from clases_hijas import Perro, Gato, Robot
from ui_consola import Consola  # maneja todo lo que se muestra en pantalla y lo que el jugador escribe


class Game:
    """Motor del juego. Inicializa, coordina turnos y determina el fin."""

    # Relaciona la tecla del jugador con la mascota correspondiente.
    MASCOTAS_DISPONIBLES = {
        "1": ("Perro",  Perro),
        "2": ("Gato",   Gato),
        "3": ("Robot",  Robot),
    }

    # Relaciona la tecla del jugador con la dificultad y su decay por turno.
    DIFICULTADES = {
        "1": ("Fácil",   {"hambre": -5,  "energia": -4, "humor": -3}),
        "2": ("Normal",  {"hambre": -8,  "energia": -6, "humor": -4}),
        "3": ("Difícil", {"hambre": -12, "energia": -9, "humor": -6}),
    }

    # Relaciona la tecla del jugador con el nombre de la acción a ejecutar.
    ACCIONES = {
        "1": "alimentar",
        "2": "jugar",
        "3": "dormir",
        "4": "estado",
        "5": "salir",
    }

    def __init__(self):
        """Inicializa el juego sin mascota activa y con el contador de turnos en 0."""
        self.__mascota = None   # privado — solo Game puede tocarlo
        self.__turno   = 0     # privado — solo Game puede tocarlo
        self.__activo  = False # privado — solo Game puede tocarlo

    # ── Inicio ────────────────────────────────────────────────────────────────

    def iniciar(self):
        """Muestra la bienvenida, pide el tipo y nombre de mascota, y arranca el loop."""
        Consola.bienvenida()

        opcion_mascota     = Consola.pedir_tipo_mascota(self.MASCOTAS_DISPONIBLES)
        nombre             = Consola.pedir_nombre()
        opcion_dificultad  = Consola.pedir_dificultad(self.DIFICULTADES)

        nombre_especie, ClaseMascota = self.MASCOTAS_DISPONIBLES[opcion_mascota]
        self.__mascota = ClaseMascota(nombre)

        # Aplicar el decay de la dificultad elegida como atributos de instancia.
        # Esto sobreescribe los valores de clase de Mascota sin modificar la clase.
        nombre_dificultad, decay = self.DIFICULTADES[opcion_dificultad]
        self.__mascota.TURNO_HAMBRE  = decay["hambre"]
        self.__mascota.TURNO_ENERGIA = decay["energia"]
        self.__mascota.TURNO_HUMOR   = decay["humor"]

        Consola.mostrar_mensaje(
            f"\n¡{self.__mascota.nombre} ha llegado a tu vida! "
            f"{self.__mascota.sonido_caracteristico()}\n"
            f"Dificultad: {nombre_dificultad}\n"
        )

        self.__activo = True
        self.__loop_principal()

    # ── Loop principal ────────────────────────────────────────────────────────

    def __loop_principal(self):
        """
        Ciclo principal del juego. Se repite hasta que la partida termine.

        Cada vuelta representa un turno:
          1. El jugador elige una acción
          2. Se ejecuta esa acción
          3. Si la mascota sigue viva, el tiempo avanza (pasar_turno)
        """
        while self.__activo:
            self.__turno += 1
            opcion_jugador = Consola.pedir_accion(self.__turno)
            self.__procesar_accion(opcion_jugador)

            if not self.__determinar_fin():
                self.__mascota.pasar_turno()

    # ── Procesamiento de acciones ─────────────────────────────────────────────

    def __procesar_accion(self, opcion_jugador):
        """Ejecuta la acción elegida por el jugador y muestra el resultado en consola."""
        accion = self.ACCIONES.get(opcion_jugador)  # None si la tecla no es válida

        if accion in ("alimentar", "jugar", "dormir"):
            # getattr busca el método por nombre y lo llama: mascota.alimentar(), .jugar() o .dormir()
            metodo = getattr(self.__mascota, accion)
            resultado = metodo()
            Consola.mostrar_resultado(resultado)
            Consola.mostrar_estado(self.__mascota.get_estado())

        elif accion == "estado":
            Consola.mostrar_estado(self.__mascota.get_estado())

        elif accion == "salir":
            Consola.mostrar_mensaje("Hasta la próxima. Tu mascota te va a extrañar...")
            self.__activo = False

        else:
            Consola.mostrar_mensaje("Opción inválida. Intentá de nuevo.")
            self.__turno -= 1

    # ── Fin de partida ────────────────────────────────────────────────────────

    def __determinar_fin(self):
        """
        Revisa si la mascota murió y termina el juego en ese caso.
        Devuelve True si la partida terminó, False si continúa.
        """
        la_mascota_murio = not self.__mascota.esta_vivo()

        if la_mascota_murio:
            Consola.mostrar_muerte(self.__mascota.nombre, self.__turno)
            self.__activo = False
            return True

        return False
