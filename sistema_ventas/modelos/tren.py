from boleto import Boleto

class Tren:
    """
    Representa una categoría de tren con capacidad limitada y boletos vendidos.
    Atributos: categoría, capacidad, precio, lista de boletos vendidos
    """
    def __init__(self, categoria, capacidad, precio):
        self.categoria = categoria
        self.capacidad = capacidad
        self.precio = precio
        self.boletos_vendidos = []

    def disponibilidad(self):
        """Devuelve el número de asientos disponibles"""
        return self.capacidad - len(self.boletos_vendidos)

    def vender_boleto(self, cliente):
        """Vende un boleto si hay disponibilidad"""
        if self.disponibilidad() <= 0:
            return None
        boleto = Boleto(self.categoria, self.precio, cliente)
        self.boletos_vendidos.append(boleto)
        return boleto

    def devolver_boletos_por_rut(self, rut):
        """Devuelve (elimina) todos los boletos vendidos asociados a un RUT"""
        antes = len(self.boletos_vendidos)
        self.boletos_vendidos = [b for b in self.boletos_vendidos if b.cliente.rut != rut]
        return antes - len(self.boletos_vendidos)

    def total_recaudado(self):
        """Devuelve el total de dinero recaudado en este tren"""
        return sum(b.precio for b in self.boletos_vendidos)
