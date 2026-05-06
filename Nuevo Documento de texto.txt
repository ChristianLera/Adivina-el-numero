# 🔥 Adivina el Número - Modo Calor 🔥

Un juego interactivo de adivinanza con interfaz gráfica moderna, donde debes encontrar un número secreto entre 1 y 100. El juego te guía con pistas visuales y una barra de "calor" que indica qué tan cerca estás del número objetivo.

## 🎮 Características

- Interfaz moderna con colores dinámicos
- Barra de progreso que muestra la cercanía al número secreto (0% a 100%)
- Sistema de pistas: te indica si tu número es "demasiado bajo" o "demasiado alto"
- Contador de intentos
- Mensajes de victoria personalizados según tu desempeño
- Botón para reiniciar el juego en cualquier momento

## 📋 Requisitos

- Python 3.6 o superior
- Tkinter (viene incluido con la mayoría de las instalaciones de Python)

## 🚀 Cómo ejecutar

### En Windows:
Haz doble clic en `ejecutar.bat` o ejecuta en la terminal:
```bash
python AdivinaElNumero.py
```

### En macOS/Linux:
Ejecuta en la terminal:
```bash
python3 AdivinaElNumero.py
```

## 🎯 Cómo jugar

1. Escribe un número entre 1 y 100 en la caja de texto
2. Presiona ENTER o haz clic en "COMPROBAR NÚMERO"
3. Observa la barra de calor: entre más verde y llena, más cerca estás
4. Sigue las pistas hasta adivinar el número secreto
5. ¡Intenta hacerlo en la menor cantidad de intentos posible!

## 🏆 Sistema de puntuación

- **1-5 intentos**: 🏆 ¡Increíble! Eres un genio
- **6-10 intentos**: 🎉 ¡Buen trabajo!
- **Más de 10 intentos**: 🎯 ¡Sigue practicando!

## 🛠️ Personalización

Puedes modificar el rango de números cambiando la línea en el código:
```python
self.secreto = random.randint(1, 100)  # Cambia 100 por el número máximo deseado
```

## 📁 Estructura del proyecto

```
AdivinaElNumero/
├── AdivinaElNumero.py   # Código principal del juego
├── ejecutar.bat          # Script de inicio para Windows
├── ejecutar.ps1          # Script de inicio para PowerShell
└── README.md             # Este archivo
```

## 👨‍💻 Christian Lera

Desarrollado con ❤️ usando Python y Tkinter
