from flask import Flask
from flask_pymongo import PyMongo
from routes.producto_routes import producto_bp

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/TiendaSimple'
mongo = PyMongo(app)
app.mongo = mongo

# Registrar rutas
app.register_blueprint(producto_bp)

if __name__ == "__main__":
    app.run(debug=True, port=8080)

