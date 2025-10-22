from config import get_connection
import pyodbc

def listar_productos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC sp_listar_productos")
    columnas = [col[0] for col in cursor.description]
    resultados = [dict(zip(columnas, row)) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return resultados

def crear_producto(nombre, precio):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("EXEC sp_crear_producto ?, ?", (nombre, precio))
        conn.commit()
        cursor.close()
        conn.close()
        return {"mensaje": "Producto creado correctamente"}
    except pyodbc.Error as e:
        error_msg = str(e.args[1]) if len(e.args) > 1 else str(e)
        return {
            "mensaje": error_msg
        }

def actualizar_producto(id, nombre, precio):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("EXEC sp_actualizar_producto ?, ?, ?", (id, nombre, precio))
        conn.commit()
        cursor.close()
        conn.close()
        return {"mensaje": "Producto actualizado correctamente"}
    except pyodbc.Error as e:
        return {
            "mensaje": e.args[1]
        }