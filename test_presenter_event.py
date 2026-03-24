from presenter import Presenter
from Calculadora import Calculadora as Model
from MockView import MockView

if __name__ == "__main__":
    print("--- INICIANDO TEST DE MOCKING CON CLASE EVENT ---")

    # 1. Instanciamos las piezas (Lógica real + Interfaz simulada)
    modelo = Model()
    vista_falsa = MockView()

    # 2. Instanciamos el Presenter [5]
    # Si la refactorización fue exitosa, el Presenter usará .add_listener()
    # y NO fallará al no encontrar el método .connect() de Qt [6], [2]
    presentador = Presenter(vista_falsa, modelo)

    # 3. Simulamos la interacción del usuario
    print("Simulando que el usuario pulsa el botón de suma...")

    # Al emitir el evento agnóstico, se debe disparar la lógica del Presenter [2]
    vista_falsa.btnsuma.emit()

    print("--- TEST FINALIZADO ---")