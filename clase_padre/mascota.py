"""
Módulo que define la clase base abstracta Mascota.
Toda mascota del juego hereda de esta clase.
"""

from abc import ABC, abstractmethod


class Mascota(ABC):
    """Clase base abstracta. Define el contrato de toda mascota."""

    # ── Stats iniciales ───────────────────────────────────────────────────────
    HAMBRE_INICIAL  = 60   # arranca con la panza a la mitad
    ENERGIA_INICIAL = 80   # arranca descansada
    HUMOR_INICIAL   = 60   # arranca contenta pero no eufórica

    # ── Efectos de alimentar ──────────────────────────────────────────────────
    # Comer llena la panza, da un poco de energía y mejora el humor.
    ALIMENTAR_HAMBRE  = 35
    ALIMENTAR_ENERGIA = 10
    ALIMENTAR_HUMOR   = 10

    # ── Efectos de dormir ─────────────────────────────────────────────────────
    # Dormir recupera mucha energía, pero la mascota gasta algo de panza estando quieta.
    DORMIR_HAMBRE  = -5
    DORMIR_ENERGIA = 40
    DORMIR_HUMOR   = 5

    # ── Efectos de pasar un turno (el tiempo avanza solo) ─────────────────────
    # Cada turno la mascota tiene más hambre, menos energía y se pone un poco más triste.
    TURNO_HAMBRE  = -8
    TURNO_ENERGIA = -6
    TURNO_HUMOR   = -4

    def __init__(self, nombre):
        """Inicializa la mascota con stats por defecto."""
        self._nombre  = nombre           # protegido — accesible desde las subclases
        self._hambre  = self.HAMBRE_INICIAL   # protegido — 100 = lleno, 0 = muerto de hambre
        self._energia = self.ENERGIA_INICIAL  # protegido — 100 = lleno de energía, 0 = agotado
        self._humor   = self.HUMOR_INICIAL    # protegido — 100 = feliz, 0 = miserable

    # ── Getters ──────────────────────────────────────────────────────────────

    @property
    def nombre(self):
        """Devuelve el nombre de la mascota."""
        return self._nombre

    @property
    def hambre(self):
        """Devuelve el nivel de hambre (100 = lleno, 0 = muerta de hambre)."""
        return self._hambre

    @property
    def energia(self):
        """Devuelve el nivel de energía (100 = llena de energía, 0 = agotada)."""
        return self._energia

    @property
    def humor(self):
        """Devuelve el nivel de humor (100 = feliz, 0 = miserable)."""
        return self._humor

    # ── Lógica interna ───────────────────────────────────────────────────────

    STAT_MINIMO = 0
    STAT_MAXIMO = 100

    def _limitar(self, valor):
        """Asegura que un stat no salga del rango 0-100."""
        if valor < self.STAT_MINIMO:
            return self.STAT_MINIMO
        if valor > self.STAT_MAXIMO:
            return self.STAT_MAXIMO
        return valor

    def _modificar_stats(self, hambre=0, energia=0, humor=0):
        """Modifica los stats sumando o restando los valores recibidos, sin salir del rango 0-100."""
        self._hambre  = self._limitar(self._hambre  + hambre)
        self._energia = self._limitar(self._energia + energia)
        self._humor   = self._limitar(self._humor   + humor)

    def esta_vivo(self):
        """Devuelve True si la mascota sigue viva. Muere si se le acaba el hambre o la energía."""
        sin_hambre  = self._hambre  <= 0
        sin_energia = self._energia <= 0
        return not sin_hambre and not sin_energia

    # ── Acciones comunes (con comportamiento por defecto) ────────────────────

    def alimentar(self):
        """Sube el hambre, energía y humor. Devuelve el mensaje de la especie."""
        self._modificar_stats(
            hambre  = self.ALIMENTAR_HAMBRE,
            energia = self.ALIMENTAR_ENERGIA,
            humor   = self.ALIMENTAR_HUMOR,
        )
        return self._mensaje_alimentar()

    def dormir(self):
        """Recupera mucha energía a costa de algo de hambre. Devuelve el mensaje de la especie."""
        self._modificar_stats(
            hambre  = self.DORMIR_HAMBRE,
            energia = self.DORMIR_ENERGIA,
            humor   = self.DORMIR_HUMOR,
        )
        return self._mensaje_dormir()

    def pasar_turno(self):
        """El tiempo avanza automáticamente: baja el hambre, la energía y el humor."""
        self._modificar_stats(
            hambre  = self.TURNO_HAMBRE,
            energia = self.TURNO_ENERGIA,
            humor   = self.TURNO_HUMOR,
        )

    # ── Métodos abstractos (cada especie los implementa a su manera) ─────────

    @abstractmethod
    def jugar(self):
        """Acción de jugar. Cada especie tiene su propio comportamiento y costo de stats."""
        pass

    @abstractmethod
    def _mensaje_alimentar(self):
        """Mensaje personalizado que se muestra al alimentar a esta especie."""
        pass

    @abstractmethod
    def _mensaje_dormir(self):
        """Mensaje personalizado que se muestra al hacer dormir a esta especie."""
        pass

    @abstractmethod
    def sonido_caracteristico(self):
        """Sonido único de la especie, usado al presentar la mascota al inicio."""
        pass

    # ── Estado general ───────────────────────────────────────────────────────

    def get_estado(self):
        """Devuelve un diccionario con todos los stats actuales de la mascota."""
        return {
            "nombre":  self._nombre,
            "hambre":  self._hambre,
            "energia": self._energia,
            "humor":   self._humor,
        }
