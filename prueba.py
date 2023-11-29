from seeders import insertar_usuarios_prueba, generar_codigo
from Arbol import BaseDeDatosBST

bd = BaseDeDatosBST()
##insertar_usuarios_prueba(bd, 5)
print(bd.obtener_usuarios())
