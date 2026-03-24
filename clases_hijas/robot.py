"""
Módulo que define la clase Robot.
En vez de comer, se carga. Jugar no le da hambre pero drena más energía.
"""

from clase_padre import Mascota


class Robot(Mascota):
    """Mascota de tipo robot. Sobreescribe alimentar() para simular carga eléctrica en vez de comida."""

    # ── Efectos de jugar ──────────────────────────────────────────────────────
    # El robot no necesita comida para jugar, pero consume mucha batería.
    JUGAR_HAMBRE  = 0    # jugar no afecta su nivel de batería
    JUGAR_ENERGIA = -18  # jugar drena bastante batería
    JUGAR_HUMOR   = 20   # jugar lo pone contento

    # ── Efectos de cargar (alimentar para el robot) ───────────────────────────
    # Cargar al robot es más efectivo que alimentar a una mascota normal.
    CARGAR_HAMBRE  = 40  # la carga llena mucho la batería
    CARGAR_ENERGIA = 20  # la carga también recupera energía
    CARGAR_HUMOR   = 15  # enchufarse lo pone de buen humor

    def jugar(self):
        """Ejecuta protocolo de diversión: sube humor pero drena energía sin afectar el hambre."""
        self._modificar_stats(
            hambre  = self.JUGAR_HAMBRE,
            energia = self.JUGAR_ENERGIA,
            humor   = self.JUGAR_HUMOR,
        )
        return f"{self.nombre} ejecuta protocolo_diversión_v2.exe. Procesando... ¡DIVERTIDO!"

    def alimentar(self):
        """Los robots no comen, se cargan. Sube más el hambre que una mascota normal."""
        self._modificar_stats(
            hambre  = self.CARGAR_HAMBRE,
            energia = self.CARGAR_ENERGIA,
            humor   = self.CARGAR_HUMOR,
        )
        return self._mensaje_alimentar()

    def _mensaje_alimentar(self):
        """Mensaje al cargar al robot. Muestra el porcentaje de batería resultante."""
        return f"{self.nombre} conecta el cable de carga. Batería al {self.hambre}%."

    def _mensaje_dormir(self):
        """Mensaje al poner en suspensión al robot."""
        return f"{self.nombre} entra en modo suspensión. Zzzz... (sonido de ventilador)"

    def sonido_caracteristico(self):
        """Sonido del robot, usado al presentarlo al inicio."""
        return "BZZZT... 01001000 01101001"
