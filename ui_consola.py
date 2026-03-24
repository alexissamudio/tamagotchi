"""
Módulo de interfaz de usuario por consola.
Contiene toda la lógica de impresión y lectura de input. No modifica ningún estado del juego.
"""


class Consola:
    """Responsable de toda la interacción con el usuario. Solo imprime y lee."""

    MENU_ACCIONES = """
┌─────────────────────────────┐
│  ¿Qué hacemos?              │
│  1. Alimentar               │
│  2. Jugar                   │
│  3. Dormir                  │
│  4. Ver estado              │
│  5. Salir                   │
└─────────────────────────────┘"""

    @staticmethod
    def bienvenida():
        """Muestra la pantalla de título del juego."""
        print("\n" + "═" * 40)
        print("   🐾  TAMAGOTCHI — Simulador de mascotas")
        print("═" * 40)

    @staticmethod
    def pedir_tipo_mascota(opciones):
        """Muestra las mascotas disponibles y devuelve la clave elegida por el jugador."""
        print("\n¿Qué mascota querés adoptar?")
        for key, (nombre, _) in opciones.items():
            print(f"  {key}. {nombre}")

        # Seguimos preguntando hasta que el jugador elija una opción válida
        while True:
            eleccion = input("\nElegí (1/2/3): ").strip()
            opcion_valida = eleccion in opciones
            if opcion_valida:
                return eleccion
            print("Opción inválida. Probá de nuevo.")

    @staticmethod
    def pedir_nombre():
        """Pide el nombre de la mascota. Repite hasta recibir un nombre no vacío."""
        # Seguimos preguntando hasta que el jugador escriba algo
        while True:
            nombre = input("¿Cómo se llama tu mascota? ").strip()
            nombre_valido = len(nombre) > 0
            if nombre_valido:
                return nombre
            print("El nombre no puede estar vacío.")

    @staticmethod
    def pedir_accion(turno):
        """Muestra el número de turno, el menú de acciones y devuelve la opción ingresada."""
        print(f"\n── Turno {turno} ──────────────────────────")
        print(Consola.MENU_ACCIONES)
        return input("Opción: ").strip()

    @staticmethod
    def mostrar_resultado(mensaje):
        """Imprime el resultado de una acción con formato de flecha."""
        print(f"\n  → {mensaje}")

    @staticmethod
    def mostrar_mensaje(mensaje):
        """Imprime un mensaje genérico en consola."""
        print(mensaje)

    @staticmethod
    def mostrar_estado(estado):
        """Muestra los stats actuales de la mascota con barras de progreso visuales."""
        nombre  = estado["nombre"]
        hambre  = estado["hambre"]
        energia = estado["energia"]
        humor   = estado["humor"]

        barra_hambre  = Consola._barra(hambre)
        barra_energia = Consola._barra(energia)
        barra_humor   = Consola._barra(humor)

        print(f"""
┌─────────────────────────────────────┐
│  Estado de {nombre:<26}│
├─────────────────────────────────────┤
│  Hambre   {barra_hambre} {hambre:>3}%  │
│  Energía  {barra_energia} {energia:>3}%  │
│  Humor    {barra_humor} {humor:>3}%  │
└─────────────────────────────────────┘""")

    @staticmethod
    def mostrar_muerte(nombre, turno):
        """Muestra la pantalla de game over con el nombre de la mascota y los turnos sobrevividos."""
        print(f"""
╔══════════════════════════════════════╗
║  😢  {nombre} no pudo más...
║  Sobrevivió {turno} turno(s).
║  Mejor suerte la próxima vez.
╚══════════════════════════════════════╝""")

    # ── Helpers ───────────────────────────────────────────────────────────────

    @staticmethod
    def _barra(valor, largo=10):
        """Genera una barra visual de progreso. █ bueno, ▓ regular, ░ malo."""
        bloques_llenos = round(valor / 100 * largo)
        bloques_vacios = largo - bloques_llenos
        simbolo = "░" if valor < 30 else ("▓" if valor < 60 else "█")
        return f"[{simbolo * bloques_llenos}{'·' * bloques_vacios}]"
