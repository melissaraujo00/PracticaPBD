from flask import Flask
from routes.producto_routes import producto_bp

app = Flask(__name__)

# Registrar rutas
app.register_blueprint(producto_bp)

if __name__ == "__main__":
    app.run(debug=True, port=8080)

