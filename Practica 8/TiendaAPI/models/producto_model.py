from flask import current_app

def listar_productos():
    productos = list(current_app.mongo.db.productos.find())
    for p in productos:
        p["_id"] = str(p["_id"])
    return productos

def crear_producto(nombre, precio):
    producto = {"nombre": nombre, "precio": precio}
    current_app.mongo.db.productos.insert_one(producto)
    return {"mensaje": "Producto creado correctamente"}

def actualizar_producto(id, nombre, precio):
    from bson import ObjectId
    result = current_app.mongo.db.productos.update_one(
        {"_id": ObjectId(id)},
        {"$set": {"nombre": nombre, "precio": precio}}
    )
    if result.matched_count:
        return {"mensaje": "Producto actualizado correctamente"}
    else:
        return {"mensaje": "Producto no encontrado"}