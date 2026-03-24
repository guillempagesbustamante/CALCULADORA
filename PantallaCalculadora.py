from PySide6 import QtWidgets, QtCore

from ui_calculadora import Ui_Calculadora as form_class


class Pantalla(QtWidgets.QMainWindow, form_class):
    """
    Clase básica que carga la interfaz generada por QtDesigner.
    Utiliza herencia múltiple para extender QMainWindow [7], [8].
    """
    # Definición de señales para el Presenter [14], [15]
    # TODO: El estudiante debe definir btnresta, btnmulti y btndivi
    btnsuma = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def entrada(self):
        """Retorna los valores de los QLineEdit convertidos a float [15, 16]."""
        # TODO: Añadir manejo de excepciones (ValueError)
        return float(self.entrada1.text()), float(self.entrada2.text())

    def salida(self, valor):
        """Muestra el resultado."""
        self.resultado.setText(f"{valor:0.3f}")

    def mensaje(self, prompt, txt):
        """Muestra errores en pantalla emergente."""
        QtWidgets.QMessageBox.critical(self, prompt, txt)

    def opera(self):
        """Identifica el botón y emite la señal correspondiente."""
        boton = self.sender()
        if boton.text() == '+':
            self.btnsuma.emit()
        # TODO: Implementar lógica para '-', '*' y '/'


if __name__ == "__main__":
    import sys
    from ..feature_presenter.Presenter import Presenter
    from Calculadora import Calculadora

    from PySide6 import QtWidgets

    app = QtWidgets.QApplication(sys.argv)
    # 1. Instanciar los componentes [25]
    modelo = Calculadora()
    pantalla = Pantalla()

    # 2. Conectarlos mediante el Presenter (Agregación) [26], [20]
    presentador = Presenter(pantalla, modelo)

    pantalla.show()
    sys.exit(app.exec())
