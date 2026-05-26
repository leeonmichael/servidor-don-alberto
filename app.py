# --- CÓDIGO DEL SERVIDOR DON ALBERTO ---
print("Servidor GigaMoto Iniciado")

# FASE 3: Reparación de emergencia (Hotfix)
# Fix: Forzar formateo de placas a mayúsculas en producción
def api_peritajes(placa):
    placa_formateada = placa.upper()
    print(f"Placa procesada de forma segura: {placa_formateada}")
    return placa_formateada