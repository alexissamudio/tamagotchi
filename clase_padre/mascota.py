"""
Módulo que define la clase base abstracta Mascota.
Toda mascota del juego hereda de esta clase.
"""

from abc import ABC, abstractmethod


class Mascota(ABC):
    """Clase base abstracta. Define el contrato de toda mascota."""

    # ── Stats iniciales ───────────────────────────────────────────────────────
    HAMBRE_INICIAL  = 50   # arranca con la panza a la mitad
    ENERGIA_INICIAL = 80   # arranca descansada
    HUMOR_INICIAL   = 60   # arranca contenta pero no eufórica

    # ── Efectos de alimentar ──────────────────────────────────────────────────
    # Comer llena la panza, da un poco de energía y mejora el humor.
    ALIMENTAR_HAMBRE  = 30
    ALIMENTAR_ENERGIA = 10
    ALIMENTAR_HUMOR   = 10

    # ── Efectos de dormir ─────────────────────────────────────────────────────
    # Dormir recupera mucha energía, pero la mascota gasta algo de panza estando quieta.
    DORMIR_HAMBRE  = -10
    DORMIR_ENERGIA = 40
    DORMIR_HUMOR   = 5

    # ── Efectos de pasar un turno (el tiempo avanza solo) ─────────────────────
    # Cada turno la mascota tiene más hambre, menos energía y se pone un poco más triste.
    TURNO_HAMBRE  = -10
    TURNO_ENERGIA = -8
    TURNO_HUMOR   = -5

    def __init__(self, nombre: str) -> None:
        """Inicializa la mascota con stats por defecto."""
        self._nombre  = nombre
        self._hambre  = self.HAMBRE_INICIAL   # 100 = lleno, 0 = muerto de hambre
        self._energia = self.ENERGIA_INICIAL  # 100 = lleno de energía, 0 = agotado
        self._humor   = self.HUMOR_INICIAL    # 100 = feliz, 0 = miserable

    # ── Getters ──────────────────────────────────────────────────────────────

    @property
    def nombre(self) -> str:
        """Devuelve el nombre de la mascota."""
        return self._nombre

    @property
    def hambre(self) -> int:
        """Devuelve el nivel de hambre (100 = lleno, 0 = muerta de hambre)."""
        return self._hambre

    @property
    def energia(self) -> int:
        """Devuelve el nivel de energía (100 = llena de energía, 0 = agotada)."""
        return self._energia

    @property
    def humor(self) -> int:
        """Devuelve el nivel de humor (100 = feliz, 0 = miserable)."""
        return self._humor

    # ── Lógica interna ───────────────────────────────────────────────────────

    def _modificar_stats(self, hambre=0, energia=0, humor=0) -> None:
        """Modifica los stats sumando o restando los valores recibidos, sin salir del rango 0-100."""
        self._hambre  = max(0, min(100, self._hambre  + hambre))
        self._energia = max(0, min(100, self._energia + energia))
        self._humor   = max(0, min(100, self._humor   + humor))

    def esta_vivo(self) -> bool:
        """Devuelve True si la mascota sigue viva. Muere si se le acaba el hambre o la energía."""
        sin_hambre  = self._hambre  <= 0
        sin_energia = self._energia <= 0
        return not sin_hambre and not sin_energia

    # ── Acciones comunes (con comportamiento por defecto) ────────────────────

    def alimentar(self) -> str:
        """Sube el hambre, energía y humor. Devuelve el mensaje de la especie."""
        self._modificar_stats(
            hambre  = self.ALIMENTAR_HAMBRE,
            energia = self.ALIMENTAR_ENERGIA,
            humor   = self.ALIMENTAR_HUMOR,
        )
        return self._mensaje_alimentar()

    def dormir(self) -> str:
        """Recupera mucha energía a costa de algo de hambre. Devuelve el mensaje de la especie."""
        self._modificar_stats(
            hambre  = self.DORMIR_HAMBRE,
            energia = self.DORMIR_ENERGIA,
            humor   = self.DORMIR_HUMOR,
        )
        return self._mensaje_dormir()

    def pasar_turno(self) -> None:
        """El tiempo avanza automáticamente: baja el hambre, la energía y el humor."""
        self._modificar_stats(
            hambre  = self.TURNO_HAMBRE,
            energia = self.TURNO_ENERGIA,
            humor   = self.TURNO_HUMOR,
        )

    # ── Métodos abstractos (cada especie los implementa a su manera) ─────────

    @abstractmethod
    def jugar(self) -> str:
        """Acción de jugar. Cada especie tiene su propio comportamiento y costo de stats."""
        pass

    @abstractmethod
    def _mensaje_alimentar(self) -> str:
        """Mensaje personalizado que se muestra al alimentar a esta especie."""
        pass

    @abstractmethod
    def _mensaje_dormir(self) -> str:
        """Mensaje personalizado que se muestra al hacer dormir a esta especie."""
        pass

    @abstractmethod
    def sonido_caracteristico(self) -> str:
        """Sonido único de la especie, usado al presentar la mascota al inicio."""
        pass

    # ── Estado general ───────────────────────────────────────────────────────

    def get_estado(self) -> dict:
        """Devuelve un diccionario con todos los stats actuales de la mascota."""
        return {
            "nombre":  self._nombre,
            "hambre":  self._hambre,
            "energia": self._energia,
            "humor":   self._humor,
            "vivo":    self.esta_vivo(),
        }
