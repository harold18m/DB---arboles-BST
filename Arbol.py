class Nodo:
    def __init__(self, clave, objeto):
        self.clave = clave
        self.objeto = objeto
        self.izquierdo = None
        self.derecho = None

class BaseDeDatosBST:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave, objeto):
        if self.raiz is None:
            self.raiz = Nodo(clave, objeto)
        else:
            self._insertar_recursivo(self.raiz, clave, objeto)

    def _insertar_recursivo(self, nodo, clave, objeto):
        if clave < nodo.clave:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(clave, objeto)
            else:
                self._insertar_recursivo(nodo.izquierdo, clave, objeto)
        elif clave > nodo.clave:
            if nodo.derecho is None:
                nodo.derecho = Nodo(clave, objeto)
            else:
                self._insertar_recursivo(nodo.derecho, clave, objeto)
        else:
            nodo.objeto = objeto

    def buscar(self, clave):
        return self._buscar_recursivo(self.raiz, clave)

    def _buscar_recursivo(self, nodo, clave):
        if nodo is None or nodo.clave == clave:
            return nodo.objeto
        if clave < nodo.clave:
            return self._buscar_recursivo(nodo.izquierdo, clave)
        return self._buscar_recursivo(nodo.derecho, clave)


    def eliminar(self, clave):
        self.raiz = self._eliminar_recursivo(self.raiz, clave)

    def _eliminar_recursivo(self, nodo, clave):
        if nodo is None:
            return nodo
        if clave < nodo.clave:
            nodo.izquierdo = self._eliminar_recursivo(nodo.izquierdo, clave)
        elif clave > nodo.clave:
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, clave)
        else:
            if nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo
            nodo.clave = self._minimo_valor(nodo.derecho)
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, nodo.clave)
        return nodo

    def _minimo_valor(self, nodo):
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual.clave
    
    def obtener_usuarios(self):
        usuarios = []
        self._obtener_usuarios_recursivo(self.raiz, usuarios)
        return usuarios

    def _obtener_usuarios_recursivo(self, nodo, usuarios):
        if nodo is not None:
            self._obtener_usuarios_recursivo(nodo.izquierdo, usuarios)
            usuarios.append(nodo.objeto)
            self._obtener_usuarios_recursivo(nodo.derecho, usuarios)
