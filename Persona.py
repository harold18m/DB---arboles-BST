class Persona:
    def __init__(self, codigo, nombre,apellido,edad,telefono):
        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono

    def __str__(self):
        return f"Código = {self.codigo}\n, Persona: {self.nombre}\n, Apellido: {self.apellido}\n, Edad: {self.edad}\n, Telefono: {self.telefono}"