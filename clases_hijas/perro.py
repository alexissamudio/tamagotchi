"""
Módulo que define la clase Perro.
Es la mascota más energética: jugar le sube mucho el humor pero le cuesta energía.
"""

from clase_padre import Mascota


class Perro(Mascota):
    """Mascota de tipo perro. Jugar le da mucho humor pero gasta bastante energía."""

    # ── Efectos de jugar ──────────────────────────────────────────────────────
    # El perro juega con mucho entusiasmo: se cansa y da hambre, pero se pone muy feliz.
    JUGAR_HAMBRE  = -10  # jugar le da hambre
    JUGAR_ENERGIA = -15  # jugar lo cansa bastante
    JUGAR_HUMOR   = 25   # jugar lo pone muy contento

    def jugar(self):
        """Juega con entusiasmo: sube mucho el humor pero gasta energía y baja el hambre."""
        self._modificar_stats(
            hambre  = self.JUGAR_HAMBRE,
            energia = self.JUGAR_ENERGIA,
            humor   = self.JUGAR_HUMOR,
        )
        return f"{self.nombre} corre, salta y trae la pelota. ¡Cola en modo hélice!"

    def _mensaje_alimentar(self):
        """Mensaje al alimentar al perro."""
        return f"{self.nombre} devora el plato en segundos y menea la cola."

    def _mensaje_dormir(self):
        """Mensaje al hacer dormir al perro."""
        return f"{self.nombre} da tres vueltas y cae rendido con un suspiro."

    def sonido_caracteristico(self):
        """Sonido del perro, usado al presentarlo al inicio."""
        return "¡Guau guau!"
