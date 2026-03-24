class Presenter:
    """Actúa como puente entre la lógica y la pantalla."""

    def __init__(self, view, model):
        # Agregación: recibe instancias externas
        self.vista = view
        self.modelo = model

        # Suscripción a las señales de la vista
        self.vista.btnsuma.add_listener(self.fsuma)
        self.vista.btnresta.add_listener(self.fresta)
        self.vista.btnmult.add_listener(self.fmult)
        self.vista.btndiv.add_listener(self.fdiv)

    def fsuma(self):
        try:
            v1, v2 = self.vista.entrada()
            resultado = self.modelo.suma(v1, v2)
            self.vista.salida(resultado)
        except Exception as e:
            self.vista.mensaje('Error', str(e))

    def fresta(self):
        try:
            v1, v2 = self.vista.entrada()
            resultado = self.modelo.resta(v1, v2)
            self.vista.salida(resultado)
        except Exception as e:
            self.vista.mensaje('Error', str(e))

    def fmult(self):
        try:
            v1, v2 = self.vista.entrada()
            resultado = self.modelo.mult(v1, v2)
            self.vista.salida(resultado)
        except Exception as e:
            self.vista.mensaje('Error', str(e))

    def fdiv(self):
        try:
            v1, v2 = self.vista.entrada()
            resultado = self.modelo.div(v1, v2)
            self.vista.salida(resultado)
        except Exception as e:
            self.vista.mensaje('Error', str(e))
