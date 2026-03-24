import sys

from PySide6 import QtWidgets

# Importamos tu clase Vista y el Modelo (aunque el Mock no use el modelo real)
from PantallaCalculadora import Pantalla


class MockPresenter:
    """
    Objeto simulado que sustituye al Presenter real.
    Su función es verificar que la Vista emite las señales del contrato [5], [3].
    """

    def __init__(self, view):
        self.view = view
        # Nos conectamos a la señal de la vista según el contrato [6]
        self.view.btnsuma.connect(self.al_recibir_suma)
        print("MOCK: Presenter conectado a la señal 'btnsuma' de la Vista.")
        self.view.btnresta.connect(self.al_recibir_resta)
        print("MOCK: Presenter conectado a la señal 'btnresta' de la Vista.")
        self.view.btnmult.connect(self.al_recibir_mult)
        print("MOCK: Presenter conectado a la señal 'btnprod' de la Vista.")
        self.view.btndiv.connect(self.al_recibir_div)
        print("MOCK: Presenter conectado a la señal 'btndiv' de la Vista.")

    def al_recibir_suma(self):
        """Este método se ejecuta cuando la Vista emite la señal btnsuma"""
        print("\n[OK] MOCK: El Presenter ha recibido la señal de SUMA desde la interfaz.")

        # Para probar el flujo completo, el Mock puede "ordenar" a la vista
        # que muestre un valor ficticio [7]
        print("MOCK: Ordenando a la vista mostrar el resultado de prueba '99.999'...")
        self.view.salida(99.999)

    def al_recibir_resta(self):
        """Este método se ejecuta cuando la Vista emite la señal btnsuma"""
        print("\n[OK] MOCK: El Presenter ha recibido la señal de SUMA desde la interfaz.")

        # Para probar el flujo completo, el Mock puede "ordenar" a la vista
        # que muestre un valor ficticio [7]
        print("MOCK: Ordenando a la vista mostrar el resultado de prueba '99.999'...")
        self.view.salida(55.555)

    def al_recibir_mult(self):
        """Este método se ejecuta cuando la Vista emite la señal btnsuma"""
        print("\n[OK] MOCK: El Presenter ha recibido la señal de SUMA desde la interfaz.")

        # Para probar el flujo completo, el Mock puede "ordenar" a la vista
        # que muestre un valor ficticio [7]
        print("MOCK: Ordenando a la vista mostrar el resultado de prueba '99.999'...")
        self.view.salida(33.333)

    def al_recibir_div(self):
        """Este método se ejecuta cuando la Vista emite la señal btnsuma"""
        print("\n[OK] MOCK: El Presenter ha recibido la señal de SUMA desde la interfaz.")

        # Para probar el flujo completo, el Mock puede "ordenar" a la vista
        # que muestre un valor ficticio [7]
        print("MOCK: Ordenando a la vista mostrar el resultado de prueba '99.999'...")
        self.view.salida(22.222)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # Instanciamos la vista real que el estudiante B ha diseñado
    vista = Pantalla()

    # Instanciamos el Mock en lugar del Presenter real
    tester = MockPresenter(vista)

    vista.show()
    print("Iniciando prueba de interfaz... Pulsa el botón '+' en la calculadora.")
    sys.exit(app.exec())
