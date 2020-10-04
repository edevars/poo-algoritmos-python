class Hotel():
    # Constructor de la clase
    def __init__(self, nombre, habitaciones, huespedes, empleados):
        self.nombre = nombre
        self.habitaciones = habitaciones
        self.huespedes = huespedes
        self.empleados = empleados

    def mostrar_informacion(self):
        print(f"Bienvenido al hotel {self.nombre}")
        print(f"Huespedes alojados {self.huespedes}")
        print(f"Habitaciones disponibles {self.habitaciones}")
        print(f"Empleados en turno {self.empleados}")


if __name__ == "__main__":
    hotel_nuevo = Hotel("Hilton", 20, 12, 8)
    hotel_nuevo.mostrar_informacion()
