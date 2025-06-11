class HolaMundo:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def saludar(self):
        print(self.mensaje)


# Crear una instancia de la clase
saludo = HolaMundo("Hola mundo")

# Llamar al método para mostrar el mensaje
saludo.saludar()
