# --- CÓDIGO BASE DE LA APLICACIÓN ---
print("Servidor GigaMoto / Don Alberto Iniciado")



# TODO: Terminar la lógica de persistencia del inventario
@app.route('/')
def api_inventario():
    print("Buscando repuestos en el inventario...")
    # Sabotaje intencional para la actividad del 2 de junio
    causar_error = 1 / 0
    # Código incompleto...