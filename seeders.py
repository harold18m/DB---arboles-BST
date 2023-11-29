from Arbol import BaseDeDatosBST
import random
import string
from Persona import Persona

def generar_codigo():
    caracteres = string.ascii_letters + string.digits
    codigo = ''.join(random.choice(caracteres) for _ in range(5))
    return codigo

def insertar_usuarios_prueba(bd, cantidad):
    nombres = ["John", "Jane", "Mike", "Sarah", "David"]
    apellidos = ["Doe", "Smith", "Johnson", "Brown", "Davis"]
    edades = [25, 30, 35, 40, 45]
    telefonos = ["1234567890", "9876543210", "5678901234", "0123456789", "8765432109"]

    for i in range(1, cantidad + 1):
        codigo = generar_codigo()
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        edad = int(random.choice(edades))
        telefono = random.choice(telefonos)
        persona = Persona(codigo, nombre, apellido, edad, telefono)
        print(persona.codigo, persona.nombre, persona.apellido, persona.edad, persona.telefono)
        bd.insertar(codigo, persona)
