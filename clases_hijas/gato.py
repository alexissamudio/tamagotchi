"""
Módulo que define la clase Gato.
Es la mascota más equilibrada: jugar tiene costos moderados en todos los stats.
"""

from clase_padre import Mascota


class Gato(Mascota):
    """Mascota de tipo gato. Stats moderados, ideal para partidas largas."""

    # ── Efectos de jugar ──────────────────────────────────────────────────────
    # El gato juega con calma: se cansa y da hambre poco, y sube el humor de forma moderada.
    JUGAR_HAMBRE  = -8   # jugar le da poca hambre
    JUGAR_ENERGIA = -15  # jugar lo cansa moderadamente
    JUGAR_HUMOR   = 20   # jugar lo pone contento, pero no tanto como al perro

    def jugar(self):
        """Juega de forma tranquila: sube el humor con bajo costo de energía y hambre."""
        self._modificar_stats(
            hambre  = self.JUGAR_HAMBRE,
            energia = self.JUGAR_ENERGIA,
            humor   = self.JUGAR_HUMOR,
        )
        return f"{self.nombre} manotea el juguete, lo ignora y finalmente lo empuja al piso."

    def _mensaje_alimentar(self):
        """Mensaje al alimentar al gato."""
        return f"{self.nombre} olfatea el plato, lo mira con desdén... y come igual."

    def _mensaje_dormir(self):
        """Mensaje al hacer dormir al gato."""
        return f"{self.nombre} encuentra el lugar más incómodo posible y duerme ahí."

    def sonido_caracteristico(self):
        """Sonido del gato, usado al presentarlo al inicio."""
        return "Mrrrow..."
