from flask import Flask, render_template, request, redirect
from seeders import generar_codigo
from seeders import insertar_usuarios_prueba
from Persona import Persona
from Arbol import BaseDeDatosBST

app = Flask(__name__)

bd = BaseDeDatosBST()


@app.route('/')
def index():
    usuarios = bd.obtener_usuarios()
    return render_template('index.html', usuarios=usuarios)

@app.route('/seeders')
def seeders():
    insertar_usuarios_prueba(bd, 5)
    return redirect('/')

@app.route('/insertar', methods=['POST'])
def insertar():
    codigo = generar_codigo()
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    edad = int(request.form['edad'])
    telefono = request.form['telefono']
    persona = Persona(codigo, nombre, apellido, edad, telefono)
    bd.insertar(codigo, persona)

    return redirect('/')

@app.route('/editar', methods=['POST'])
def actualizar():
    codigo = request.form['codigo']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    edad = int(request.form['edad'])
    telefono = request.form['telefono']
    bd.editar_persona(codigo, nombre, apellido, edad, telefono)

    return redirect('/')

@app.route('/buscar', methods=['POST'])
def buscar():
    clave = request.form['clave']
    persona = bd.buscar(clave)

    if persona is not None:
        return str(persona)
    else:
        return 'Nodo no encontrado'

@app.route('/eliminar', methods=['POST'])
def eliminar():
    clave = request.form['codigo']
    bd.eliminar(clave)
    return redirect('/')

if __name__ == '__main__':
    app.debug = True
    app.run()
    