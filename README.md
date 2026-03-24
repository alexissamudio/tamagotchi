# 🐾 Tamagotchi — Simulador de mascotas

Juego de consola en Python donde adoptás una mascota virtual y la mantenés viva. Cada turno elegís qué hacer: alimentarla, jugar, dormir o ver su estado. Si el hambre o la energía llegan a 0, la mascota muere.

---

## Demo

```
════════════════════════════════════════
   🐾  TAMAGOTCHI — Simulador de mascotas
════════════════════════════════════════

¿Qué mascota querés adoptar?
  1. Perro
  2. Gato
  3. Robot

Elegí (1/2/3): 1
¿Cómo se llama tu mascota? Rex

¡Rex ha llegado a tu vida! ¡Guau guau!

── Turno 1 ──────────────────────────
┌─────────────────────────────┐
│  ¿Qué hacemos?              │
│  1. Alimentar               │
│  2. Jugar                   │
│  3. Dormir                  │
│  4. Ver estado              │
│  5. Salir                   │
└─────────────────────────────┘
Opción: 2

  → Rex corre, salta y trae la pelota. ¡Cola en modo hélice!

┌─────────────────────────────────────┐
│  Estado de Rex                      │
├─────────────────────────────────────┤
│  Hambre   [████████··]  82%  │
│  Energía  [███████···]  71%  │
│  Humor    [█████████·]  93%  │
└─────────────────────────────────────┘
```

---

## Mascotas disponibles

| Mascota | Estilo de juego |
|---|---|
| 🐶 Perro | El más difícil. Jugar lo gasta mucho, pero sube el humor más rápido |
| 🐱 Gato | El más equilibrado. Bajo costo en todo, ideal para partidas largas |
| 🤖 Robot | No necesita comida para jugar. Cargarlo es más eficiente, pero jugar drena más energía |

---

## Cómo correrlo

**Requisitos:** Python 3.10 o superior

```bash
git clone https://github.com/alexissamudio/tamagotchi.git
cd tamagotchi
python main.py
```

---

## Cómo se juega

Cada turno elegís una acción. Después de cada acción el tiempo avanza automáticamente, bajando hambre, energía y humor. El objetivo es mantener los tres stats por encima de 0 el mayor tiempo posible.

| Acción | Efecto |
|---|---|
| Alimentar | Sube el hambre (+35), algo de energía y humor |
| Jugar | Sube el humor, pero baja hambre y energía |
| Dormir | Recupera mucha energía (+40), penaliza un poco el hambre |
| Ver estado | Muestra los stats sin gastar un turno |

**La mascota muere si el hambre o la energía llegan a 0.**

---

## Tecnologías

- Python 3.10+
- Programación orientada a objetos (herencia, clases abstractas)
- Sin dependencias externas
