class Cliente:
    """
    Representa a un cliente que compra boletos.
    Atributos: nombre, apellido, rut, email
    """
    def __init__(self, nombre, apellido, rut, email):
        # Validar que todos los campos sean obligatorios
        if not nombre or not apellido or not rut or not email:
            raise ValueError("Todos los datos del cliente son obligatorios.")
        self.nombre = nombre.strip()
        self.apellido = apellido.strip()
        self.rut = rut.strip()
        self.email = email.strip()

    def validar_email(self):
        """Valida que el email tenga formato básico correcto"""
        return "@" in self.email and "." in self.email and len(self.email) > 5

    def validar_rut(self):
        """Valida que el RUT tenga formato básico correcto"""
        return "-" in self.rut and len(self.rut) >= 8  # Al menos 8 caracteres incluyendo el guión

    def full_name(self):
        """Devuelve el nombre completo del cliente"""
        return f"{self.nombre} {self.apellido}"

    def __str__(self):
        return f"Cliente({self.full_name()}, RUT={self.rut}, Email={self.email})"