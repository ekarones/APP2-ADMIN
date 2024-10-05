import requests
from flask import Blueprint, render_template, request, redirect, url_for

bp_advices = Blueprint("advices", __name__, url_prefix="/advices")
API_URL = "http://192.168.1.36:8000/advices"

# Ruta principal de consejos
@bp_advices.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Agregar un nuevo consejo
        name = request.form.get("name_disease")
        description = request.form.get("description")
        if name and description:
            data = {"name_disease": name, "description": description}
            requests.post(API_URL, params=data)
        return redirect(url_for("advices.index"))

    # Obtener todos los consejos
    response = requests.get(API_URL)
    advices = response.json() if response.status_code == 200 else []
    
    return render_template("advices.html", advices=advices)

# Ruta para eliminar un consejo
@bp_advices.route("/delete/<int:id>", methods=["POST"])
def delete_advice(id):
    requests.delete(f"{API_URL}/{id}")
    return redirect(url_for("advices.index"))
