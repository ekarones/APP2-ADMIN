import requests
from flask import Blueprint, render_template, request, redirect, url_for

bp_diseases = Blueprint("diseases", __name__, url_prefix="/diseases")
API_URL = "http://192.168.1.36:8000/diseases"

# Ruta principal de enfermedades
@bp_diseases.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Agregar una nueva enfermedad
        name = request.form.get("name")
        description = request.form.get("description")
        if name and description:
            data = {"name": name, "description": description}
            requests.post(API_URL, params=data)
        return redirect(url_for("diseases.index"))

    # Obtener todas las enfermedades
    response = requests.get(API_URL)
    diseases = response.json() if response.status_code == 200 else []
    
    return render_template("diseases.html", diseases=diseases)

# Ruta para eliminar una enfermedad
@bp_diseases.route("/delete/<int:id>", methods=["POST"])
def delete_disease(id):
    requests.delete(f"{API_URL}/{id}")
    return redirect(url_for("diseases.index"))
