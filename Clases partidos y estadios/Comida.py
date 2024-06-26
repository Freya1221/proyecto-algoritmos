from Products import Products

class Comida (Products):
    def __init__(self, name, quantity, price, stock, tipo_producto, tipo_bebida):
        super().__init__(name, quantity, price, stock, tipo_producto)
        self.tipo_bebida = tipo_bebida
