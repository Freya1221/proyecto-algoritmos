class Products ():
    def __init__(self, name, quantity, price, stock, tipo_producto):
        self.name = name 
        self.quantity = quantity
        self.price = price
        self.stock = stock 
        self.tipo_producto = tipo_producto 

    def show(self):
        print(f'''
NAME: {self.name}
QUANTITY: {self.quantity}
PRICE: {self.price}
STOCK: {self.stock}
TIPO_PRODUCTO: {self.tipo_producto}
''')
    