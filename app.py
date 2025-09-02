# app.py (ya está correcto)

from flask import Flask, render_template, request
# Esta línea ahora funcionará porque existe data.py y exporta la variable 'tarjetas'
from data import tarjetas 

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    categoria_seleccionada = request.form.get("categoria", "Todas")
    
    # Extraer categorías únicas de la lista de tarjetas
    # El uso de set() es eficiente para obtener valores únicos
    categorias = sorted(set(t["categoria"] for t in tarjetas))
    
    # Filtrar por categoría si se selecciona una
    if categoria_seleccionada != "Todas":
        tarjetas_filtradas = [t for t in tarjetas if t["categoria"] == categoria_seleccionada]
    else:
        tarjetas_filtradas = tarjetas

    return render_template(
        "index.html",
        categorias=categorias,
        categoria_seleccionada=categoria_seleccionada,
        tarjetas=tarjetas_filtradas
    )

if __name__ == "__main__":
    app.run(debug=True)