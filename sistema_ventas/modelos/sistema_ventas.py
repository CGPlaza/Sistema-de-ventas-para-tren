from tren import Tren

# Constantes de precios por categoría de tren
PRECIO_PRIMERA = 20000   # Precio por asiento en Primera Clase
PRECIO_SEGUNDA = 15000   # Precio por asiento en Segunda Clase
PRECIO_ECONOMICA = 10000 # Precio por asiento en Clase Económica

class SistemaVentas:
    """
    Controlador principal del sistema de ventas.
    Maneja los trenes y coordina las operaciones de negocio.
    """
    def __init__(self):
        self.trenes = [
            Tren("Primera Clase", 15, PRECIO_PRIMERA),
            Tren("Segunda Clase", 25, PRECIO_SEGUNDA),
            Tren("Clase Economica", 30, PRECIO_ECONOMICA),
        ]

    def obtener_tren_por_categoria(self, categoria):
        """Devuelve un tren según su categoría"""
        for t in self.trenes:
            if t.categoria.lower() == categoria.lower():
                return t
        return None

    def vender_boleto(self, categoria, cliente):
        """Vende un boleto en la categoría indicada, validando cliente"""
        tren = self.obtener_tren_por_categoria(categoria)
        if not tren:
            raise ValueError("Categoría no encontrada.")
        if not cliente.validar_email():
            raise ValueError("Email inválido.")
        if not cliente.validar_rut():
            raise ValueError("RUT inválido.")
        return tren.vender_boleto(cliente)

    def devolver_boletos_por_rut(self, rut):
        """Devuelve todos los boletos asociados a un RUT"""
        encontrados = False
        for t in self.trenes:
            if t.devolver_boletos_por_rut(rut) > 0:
                encontrados = True
        return encontrados

    def consulta_boletos_por_rut(self, rut):
        """Devuelve una lista de boletos asociados a un RUT"""
        resultados = []
        for t in self.trenes:
            for b in t.boletos_vendidos:
                if b.cliente.rut == rut:
                    resultados.append(b)
        return resultados

    def total_ventas_por_categoria(self):
        """Devuelve un diccionario con las ventas totales por categoría"""
        return {t.categoria: t.total_recaudado() for t in self.trenes}

    def total_boletos_vendidos(self):
        """Devuelve el total de boletos vendidos en todos los trenes"""
        return sum(len(t.boletos_vendidos) for t in self.trenes)

    def total_recaudado(self):
        """Devuelve el total recaudado en todos los trenes"""
        return sum(t.total_recaudado() for t in self.trenes)

    def porcentaje_ventas_por_categoria(self):
        """Devuelve el porcentaje de ventas por categoría"""
        total = self.total_boletos_vendidos()
        if total == 0:
            return {t.categoria: 0.0 for t in self.trenes}
        return {t.categoria: (len(t.boletos_vendidos) / total) * 100 for t in self.trenes}

    def cierre_de_caja(self):
        """Devuelve un resumen con el cierre de caja"""
        return {
            "total_recaudado": self.total_recaudado(),
            "ventas_por_categoria": self.total_ventas_por_categoria(),
            "porcentaje_ventas": self.porcentaje_ventas_por_categoria(),
            "total_boletos": self.total_boletos_vendidos()
        }

    # ==== MÉTODOS NUEVOS QUE DEBES AGREGAR ====
    def vender(self, cliente, categoria, cantidad):
        """Vende múltiples boletos de una vez"""
        tren = self.obtener_tren_por_categoria(categoria)
        if not tren:
            return None
        
        boletos_vendidos = []
        for _ in range(cantidad):
            if tren.disponibilidad() > 0:
                boleto = tren.vender_boleto(cliente)
                boletos_vendidos.append(boleto)
            else:
                break
        return boletos_vendidos

    def devolver(self, id_boleto):
        """Devuelve un boleto por ID (no por RUT)"""
        for tren in self.trenes:
            for boleto in tren.boletos_vendidos:
                if boleto.id == id_boleto:
                    tren.boletos_vendidos.remove(boleto)
                    return True
        return False

    def consultar_boletos(self):
        """Muestra todos los boletos vendidos"""
        for tren in self.trenes:
            for boleto in tren.boletos_vendidos:
                print(boleto)

    def totalizar_ventas(self):
        """Muestra ventas por categoría"""
        for tren in self.trenes:
            print(f"{tren.categoria}: {len(tren.boletos_vendidos)} boletos, ${tren.total_recaudado()}")

    def porcentaje_ventas(self):
        """Muestra porcentajes de ventas"""
        total = self.total_boletos_vendidos()
        if total == 0:
            print("No hay ventas registradas.")
            return
        
        for cat, porcentaje in self.porcentaje_ventas_por_categoria().items():
            print(f"{cat}: {porcentaje:.2f}%")

    def cierre_caja(self):
        """Muestra cierre de caja completo"""
        cierre = self.cierre_de_caja()
        print(f"Total recaudado: ${cierre['total_recaudado']}")
        print(f"Total boletos: {cierre['total_boletos']}")
        print("Ventas por categoría:")
        for cat, monto in cierre['ventas_por_categoria'].items():
            print(f"  {cat}: ${monto}")