# 🐾 Tamagotchi — Simulador de mascotas

Juego de consola en Python donde adoptás una mascota virtual y la mantenés viva tomando decisiones cada turno. Si no la alimentás ni descansás a tiempo, muere.

---

## Cómo correrlo

```bash
python main.py
```

> Requiere Python 3.10 o superior.

---

## Estructura del proyecto

```
Challenge1/
├── main.py              # Punto de entrada
├── game.py              # Motor del juego (loop, turnos, fin de partida)
├── ui_consola.py        # Todo lo que se imprime y se lee por consola
├── clase_padre/
│   └── mascota.py       # Clase base abstracta con stats y acciones comunes
└── clases_hijas/
    ├── perro.py         # Implementación específica del Perro
    ├── gato.py          # Implementación específica del Gato
    └── robot.py         # Implementación específica del Robot
```

---

## Arquitectura y decisiones de diseño

### Separación de responsabilidades

El proyecto sigue el principio de **separación de responsabilidades**: cada módulo hace una sola cosa.

| Módulo | Responsabilidad |
|---|---|
| `main.py` | Arrancar el programa, nada más |
| `game.py` | Controlar el flujo: turnos, acciones, fin de partida |
| `ui_consola.py` | Mostrar e imprimir — no toca ningún estado del juego |
| `mascota.py` | Definir qué es una mascota y cómo cambian sus stats |
| `perro/gato/robot.py` | Comportamiento específico de cada especie |

### Herencia y abstracción (POO)

`Mascota` es una **clase abstracta** (hereda de `ABC`). Esto significa que no se puede instanciar directamente — solo existe para definir el contrato que deben cumplir todas las mascotas.

```
Mascota (abstracta)
├── Perro
├── Gato
└── Robot
```

Los métodos abstractos que cada subclase **debe** implementar son:
- `jugar()` — cada especie juega diferente
- `_mensaje_alimentar()` — mensaje personalizado al comer
- `_mensaje_dormir()` — mensaje personalizado al dormir
- `sonido_caracteristico()` — el sonido único de la especie

Las acciones comunes (`alimentar`, `dormir`, `pasar_turno`) están implementadas en la clase base porque son iguales para todos, excepto el Robot que sobreescribe `alimentar()`.

---

## Lógica del juego

### El loop principal

Cada iteración del loop es un **turno**:

```
1. El jugador elige una acción
2. Se ejecuta la acción → modifica los stats → se muestra el estado
3. Se revisa si la mascota murió
4. Si sigue viva → el tiempo avanza (pasar_turno)
5. Repetir
```

El estado se muestra automáticamente después de cada acción (alimentar, jugar, dormir). El tiempo que avanza automáticamente (`pasar_turno`) representa el paso del tiempo: la mascota tiene más hambre, menos energía y se pone más triste sin importar lo que haga el jugador.

### Despacho de acciones

Las acciones `alimentar`, `jugar` y `dormir` se llaman dinámicamente con `getattr`, evitando un if/elif por cada una:

```python
if accion in ("alimentar", "jugar", "dormir"):
    resultado = getattr(self.__mascota, accion)()
    Consola.mostrar_resultado(resultado)
    Consola.mostrar_estado(self.__mascota.get_estado())
```

Esto significa que agregar una nueva acción no requiere modificar este método, solo agregar el método a la clase `Mascota`.

### Los stats

Cada mascota tiene tres estadísticas, todas en el rango **0 a 100**:

| Stat | 100 significa | 0 significa |
|---|---|---|
| Hambre | Llena / con batería | Muerta de hambre |
| Energía | Llena de energía | Agotada |
| Humor | Feliz | Miserable |

### Condición de muerte

La mascota muere si **el hambre llega a 0** o **la energía llega a 0**. El humor bajo no mata, pero refleja el estado emocional.

```python
def esta_vivo(self):
    sin_hambre  = self._hambre  <= 0
    sin_energia = self._energia <= 0
    return not sin_hambre and not sin_energia
```

---

## Tabla de stats y balance

### Stats iniciales

| Stat | Valor |
|---|---|
| Hambre | 60 |
| Energía | 80 |
| Humor | 60 |

### Efecto de cada acción

| Acción | Hambre | Energía | Humor |
|---|---|---|---|
| Alimentar | +35 | +10 | +10 |
| Dormir | −5 | +40 | +5 |
| Pasar turno (automático) | −8 | −6 | −4 |

### Efecto de jugar (varía por especie)

| Mascota | Hambre | Energía | Humor |
|---|---|---|---|
| Perro | −10 | −15 | +25 |
| Gato | −5 | −10 | +15 |
| Robot | 0 | −18 | +20 |

> El Robot sobreescribe `alimentar()`: en vez de comida, se carga con más efecto que las otras mascotas (+40 hambre, +20 energía, +15 humor).

### Diferencias entre mascotas

- **Perro**: el más costoso de mantener. Jugar lo gasta mucho, pero sube el humor más que los demás.
- **Gato**: el más equilibrado. Jugar tiene bajo costo y es ideal para partidas largas.
- **Robot**: no le afecta el hambre al jugar. Cargarlo es más eficiente que alimentar a los otros, pero jugar drena más energía.

---

## Interfaz de usuario

`Consola` es una clase de métodos estáticos — nunca guarda estado, solo imprime y lee. Esto la mantiene completamente desacoplada de la lógica del juego.

La barra de progreso visual cambia de símbolo según el nivel (valor alto = bueno en todos los stats):

| Rango | Símbolo | Significa |
|---|---|---|
| 60–100 | `█` | Bien |
| 30–59 | `▓` | Regular |
| 0–29 | `░` | Mal |

---

## Flujo completo resumido

```
main.py
  └── Game.iniciar()
        ├── Consola.bienvenida()
        ├── Consola.pedir_tipo_mascota() → instancia Perro / Gato / Robot
        ├── Consola.pedir_nombre()
        └── Game.__loop_principal()
              └── por cada turno:
                    ├── Consola.pedir_accion()
                    ├── Game.__procesar_accion()
                    │     ├── mascota.alimentar() / jugar() / dormir()
                    │     └── Consola.mostrar_estado()
                    ├── Game.__determinar_fin()
                    └── mascota.pasar_turno()
```
