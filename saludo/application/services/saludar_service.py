from saludo.domain.persona import Persona
from saludo.application.ports.saludar_use_case import SaludarUseCase


class SaludarService(SaludarUseCase):
    def ejecutar(self, nombre: str) -> str:
        persona = Persona(nombre=nombre)
        return persona.saludar()

