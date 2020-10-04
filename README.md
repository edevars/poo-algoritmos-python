# Curso de POO y algoritmos en Python

En python todo es un objeto. Para poder crear clases en Python es necesario usar la palabra reservada `class`:

```python
class Hotel():
    # Constructor de la clase
    def __init__(self, nombre, habitaciones, huespedes, empleados):
        self.nombre = nombre
        self.habitaciones = habitaciones
        self.huespedes = huespedes
        self.empleados = empleados
```

Las clases nos sirven para representar objetos de nuestro mundo real como lo puede ser un auto, una lampara o una fiesta.