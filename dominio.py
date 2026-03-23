from abc import ABC, abstractmethod


class Mascota(ABC):
    """Clase base abstracta. Define el contrato de toda mascota."""

    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__hambre = 50      # 0 = lleno, 100 = muerto de hambre
        self.__energia = 80     # 0 = agotado, 100 = lleno de energía
        self.__humor = 60       # 0 = miserable, 100 = feliz

    # ── Getters ──────────────────────────────────────────────────────────────

    @property
    def nombre(self):
        return self.__nombre

    @property
    def hambre(self):
        return self.__hambre

    @property
    def energia(self):
        return self.__energia

    @property
    def humor(self):
        return self.__humor

    # ── Lógica interna ───────────────────────────────────────────────────────

    def _modificar_stats(self, hambre=0, energia=0, humor=0):
        """Modifica stats respetando el rango 0-100."""
        self.__hambre  = max(0, min(100, self.__hambre  + hambre))
        self.__energia = max(0, min(100, self.__energia + energia))
        self.__humor   = max(0, min(100, self.__humor   + humor))

    def esta_vivo(self) -> bool:
        return self.__hambre < 100 and self.__energia > 0

    # ── Acciones comunes (con comportamiento por defecto) ────────────────────

    def alimentar(self):
        self._modificar_stats(hambre=-30, energia=10, humor=10)
        return self._mensaje_alimentar()

    def dormir(self):
        self._modificar_stats(hambre=10, energia=40, humor=5)
        return self._mensaje_dormir()

    def pasar_turno(self):
        """El tiempo avanza: sube el hambre, baja la energía."""
        self._modificar_stats(hambre=10, energia=-8, humor=-5)

    # ── Métodos abstractos (cada especie los implementa a su manera) ─────────

    @abstractmethod
    def jugar(self) -> str:
        pass

    @abstractmethod
    def _mensaje_alimentar(self) -> str:
        pass

    @abstractmethod
    def _mensaje_dormir(self) -> str:
        pass

    @abstractmethod
    def sonido_caracteristico(self) -> str:
        pass

    # ── Estado general ───────────────────────────────────────────────────────

    def get_estado(self) -> dict:
        return {
            "nombre":  self.__nombre,
            "hambre":  self.__hambre,
            "energia": self.__energia,
            "humor":   self.__humor,
            "vivo":    self.esta_vivo(),
        }
