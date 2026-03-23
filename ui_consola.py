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
        print("\n" + "═" * 40)
        print("   🐾  TAMAGOTCHI — Simulador de mascotas")
        print("═" * 40)

    @staticmethod
    def pedir_tipo_mascota(opciones: dict) -> str:
        print("\n¿Qué mascota querés adoptar?")
        for key, (nombre, _) in opciones.items():
            print(f"  {key}. {nombre}")

        while True:
            eleccion = input("\nElegí (1/2/3): ").strip()
            if eleccion in opciones:
                return eleccion
            print("Opción inválida. Probá de nuevo.")

    @staticmethod
    def pedir_nombre() -> str:
        while True:
            nombre = input("¿Cómo se llama tu mascota? ").strip()
            if nombre:
                return nombre
            print("El nombre no puede estar vacío.")

    @staticmethod
    def pedir_accion(turno: int) -> str:
        print(f"\n── Turno {turno} ──────────────────────────")
        print(Consola.MENU_ACCIONES)
        return input("Opción: ").strip()

    @staticmethod
    def mostrar_resultado(mensaje: str):
        print(f"\n  → {mensaje}")

    @staticmethod
    def mostrar_mensaje(mensaje: str):
        print(mensaje)

    @staticmethod
    def mostrar_estado(estado: dict):
        nombre  = estado["nombre"]
        hambre  = estado["hambre"]
        energia = estado["energia"]
        humor   = estado["humor"]

        barra_h = Consola._barra(hambre,  invertida=True)   # más rojo = peor
        barra_e = Consola._barra(energia, invertida=False)
        barra_hu = Consola._barra(humor,  invertida=False)

        print(f"""
┌─────────────────────────────────────┐
│  Estado de {nombre:<26}│
├─────────────────────────────────────┤
│  Hambre   {barra_h} {hambre:>3}%  │
│  Energía  {barra_e} {energia:>3}%  │
│  Humor    {barra_hu} {humor:>3}%  │
└─────────────────────────────────────┘""")

    @staticmethod
    def mostrar_muerte(nombre: str, turno: int):
        print(f"""
╔══════════════════════════════════════╗
║  😢  {nombre} no pudo más...          
║  Sobrevivió {turno} turno(s).         
║  Mejor suerte la próxima vez.        
╚══════════════════════════════════════╝""")

    # ── Helpers ───────────────────────────────────────────────────────────────

    @staticmethod
    def _barra(valor: int, invertida: bool, largo: int = 10) -> str:
        """Genera una barra visual de progreso."""
        llenas = round(valor / 100 * largo)
        if invertida:
            simbolo = "█" if valor > 60 else ("▓" if valor > 30 else "░")
        else:
            simbolo = "░" if valor < 30 else ("▓" if valor < 60 else "█")
        return f"[{'█' * llenas}{'·' * (largo - llenas)}]"
