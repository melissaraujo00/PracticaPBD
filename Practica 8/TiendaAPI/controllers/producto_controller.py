from models import producto_model

def get_productos():
    return producto_model.listar_productos()

def add_producto(data):
    return producto_model.crear_producto(data["nombre"], data["precio"])

def update_producto(data):
    return producto_model.actualizar_producto(data["productoID"], data["nombre"], data["precio"])