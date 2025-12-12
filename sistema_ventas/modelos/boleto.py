import uuid

class Boleto:
    """
    Representa un boleto emitido.
    Atributos: id único (uuid), categoría, precio, cliente
    """
    def __init__(self, categoria, precio, cliente):
        self.id = str(uuid.uuid4())  # Se genera un identificador único
        self.categoria = categoria
        self.precio = precio
        self.cliente = cliente

    def emitir_boleto(self):
        """Devuelve un string con la información del boleto emitido"""
        return f"Boleto[{self.id[:8]}] - {self.categoria} - $ {self.precio} - Cliente: {self.cliente.full_name()}"

    def __str__(self):
        return self.emitir_boleto()
