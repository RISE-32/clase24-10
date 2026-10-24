class Persona:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def saludar(self) -> str:
        return f'Hola {self.nombre}'

