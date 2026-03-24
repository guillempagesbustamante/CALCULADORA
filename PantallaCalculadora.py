from PySide6 import QtWidgets, QtCore
from Event import Event
from ui_calculadora import Ui_Calculadora as form_class


class Pantalla(QtWidgets.QMainWindow, form_class):
    """
    Clase básica que carga la interfaz generada por QtDesigner.
    Utiliza herencia múltiple para extender QMainWindow [7], [8].
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Definición de señales para el Presenter [14], [15]
        self.btnsuma = Event()
        self.btnresta = Event()
        self.btnmult = Event()
        self.btndiv = Event()

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
        if not self.verifica():
            return
        boton = self.sender()
        if boton.text() == '+':
            self.btnsuma.emit()
        if boton.text() == '-':
            self.btnresta.emit()
        if boton.text() == '*':
            self.btnmult.emit()
        if boton.text() == '/':
            self.btndiv.emit()

    def verifica(self):
        """Verifica que los campos de entrada no estén vacíos."""
        if not self.entrada1.text() or not self.entrada2.text():
            self.mensaje('Error', 'Ambos campos de entrada deben ser llenados.')
            return False
        if not self.entrada1.text().isnumeric() or not self.entrada2.text().isnumeric():
            self.mensaje('Error', 'Ambos campos de entrada deben ser numéricos.')
            return False
        return True


if __name__ == "__main__":
    import sys
    from presenter import Presenter
    from Calculadora import Calculadora

    app = QtWidgets.QApplication(sys.argv)
    # 1. Instanciar los componentes [25]
    modelo = Calculadora()
    pantalla = Pantalla()

    # 2. Conectarlos mediante el Presenter (Agregación) [26], [20]
    presentador = Presenter(pantalla, modelo)

    pantalla.show()
    sys.exit(app.exec())
