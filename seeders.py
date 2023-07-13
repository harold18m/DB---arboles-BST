import random
from app import generar_codigo
from Persona import Persona
from Arbol import BaseDeDatosBST



def insertar_usuarios_prueba(cantidad):
    
    nombres = ["John", "Jane", "Mike", "Sarah", "David"]
    apellidos = ["Doe", "Smith", "Johnson", "Brown", "Davis"]
    edades = [25, 30, 35, 40, 45]
    telefonos = ["1234567890", "9876543210", "5678901234", "0123456789", "8765432109"]

    bd = BaseDeDatosBST()

    for i in range(1, cantidad + 1):
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        edad = random.choice(edades)
        telefono = random.choice(telefonos)
        persona = Persona(codigo, nombre, apellido, edad, telefono)
        codigo = generar_codigo()
        bd.insertar(codigo, persona)

