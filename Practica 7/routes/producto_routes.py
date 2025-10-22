from flask import Blueprint, request, jsonify
from controllers import producto_controller

producto_bp = Blueprint("producto_bp", __name__)

@producto_bp.route("/productos", methods=["GET"])
def listar():
    return jsonify(producto_controller.get_productos())

@producto_bp.route("/productos", methods=["POST"])
def crear():
    data = request.json
    return jsonify(producto_controller.add_producto(data))

@producto_bp.route("/productos", methods=["PUT"])
def actualizar():
    data = request.json
    return jsonify(producto_controller.update_producto(data))