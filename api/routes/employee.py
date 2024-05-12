from flask import Blueprint, request

employee_bp = Blueprint('employee', __name__)


@employee_bp.post('/api/employees')
def create_employee():
    data = request.get_json()
    return data
