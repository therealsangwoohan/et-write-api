from flask import Flask
from api.routes.employee import employee_bp

app = Flask(__name__)

app.register_blueprint(employee_bp)
