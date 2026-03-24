from PySide6.QtCore import QObject, Signal

from Calculadora import Calculadora
from presenter import Presenter


# Objeto simulado (Mock) que cumple el contrato de la Vista pero no tiene
# interfaz gráfica ni lógica real,
# solo imprime lo que se le pide y devuelve valores predefinidos.
class MockView(QObject):
    btnsuma = Signal()  # Solo suma soportada para el esqueleto
    btnresta = Signal()  # Solo suma soportada para el esqueleto
    btnmult = Signal()  # Solo suma soportada para el esqueleto
    btndiv = Signal()  # Solo suma soportada para el esqueleto

    def entrada(self):
        print("MOCK: Presenter solicita entradas. Enviando (10, 5)...")
        return 10.0, 5.0

    def salida(self, valor):
        print(f"MOCK: La vista recibió el resultado: {valor}")

    def mensaje(self, titulo, texto):
        print(f"MOCK ERROR: {titulo}: {texto}")

    def verifica(self):
        return True

if __name__ == "__main__":
    print("Iniciando prueba de Mocking del Presenter...")

    # Instanciamos los componentes (Vista simulada y Modelo real)
    vista_falsa = MockView()
    modelo_real = Calculadora()

    # El Presenter cree que está hablando con la ventana real
    p = Presenter(vista_falsa, modelo_real)

    # Simulamos que el usuario pulsó el botón de suma en la GUI
    print("Simulando click en botón suma...")
    vista_falsa.btnsuma.emit()
    vista_falsa.btnresta.emit()
    vista_falsa.btnmult.emit()
    vista_falsa.btndivemit()
