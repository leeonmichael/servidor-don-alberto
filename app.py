import os  
import datetime
from flask import Flask, jsonify, request

# Inicialización de la aplicación Flask
app = Flask(__name__)

# Base de datos simulada en memoria
peritajes = [
    {
        "id": 1,
        "vehiculo": "Yamaha Pulsar",
        "estado": "Revisión General",
        "fecha": str(datetime.datetime.now())
    }
]

# Ruta de inicio (Raíz)
@app.route('/')
def inicio():
    return jsonify({
        "servidor": "Servidor Don Alberto - GigaMoto",
        "status": "online",
        "hora_servidor": str(datetime.datetime.now())
    })

# Ruta para obtener todos los peritajes (GET)
@app.route('/api/peritajes', methods=['GET'])
def obtener_peritajes():
    return jsonify({
        "status": "online",
        "hora_servidor": str(datetime.datetime.now()),
        "peritajes": peritajes
    })

# Ruta para agregar un nuevo peritaje (POST)
@app.route('/api/peritajes', methods=['POST'])
def agregar_peritaje():
    nuevo_peritaje = request.get_json()
    if not nuevo_peritaje:
        return jsonify({"error": "No se enviaron datos válidos"}), 400
        
    peritajes.append(nuevo_peritaje)
    return jsonify({
        "mensaje": "Peritaje agregado exitosamente",
        "data": nuevo_peritaje
    }), 201

# Bloque de ejecución adaptado para la nube
if __name__ == '__main__':
    # Railway define el puerto en la variable de entorno 'PORT'. Si no existe, usa el 5000 por defecto local.
    puerto = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=puerto, debug=True)