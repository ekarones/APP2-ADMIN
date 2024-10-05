from flask import Flask, render_template
from .diseases import bp_diseases
from .advices import bp_advices

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp_diseases)
    app.register_blueprint(bp_advices)

    # Ruta para la página principal
    @app.route("/")
    def index():
        return render_template("index.html")

    return app
