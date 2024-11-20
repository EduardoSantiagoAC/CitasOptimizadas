from flask import Flask, request, jsonify
from flask_cors import CORS
import pyodbc

app = Flask(__name__)
CORS(app)  


conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=SANTIAGO12;"
    "DATABASE=CitasMedicas;"
    "Trusted_Connection=yes;"
)

@app.route('/citas', methods=['POST'])
def registrar_cita():
    data = request.json
    cursor = conn.cursor()
    query = """
        INSERT INTO Citas (NombrePaciente, Edad, Sexo, Padecimiento, Especialidad)
        VALUES (?, ?, ?, ?, ?)
    """
    values = (data['nombre'], data['edad'], data['sexo'], data['padecimiento'], data['especialidad'])
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    return jsonify({"message": "Cita registrada exitosamente"}), 201

@app.route('/citas', methods=['GET'])
def obtener_citas():
    cursor = conn.cursor()
    query = "SELECT * FROM Citas ORDER BY FechaCreacion DESC"
    cursor.execute(query)
    citas = [
        {
            "id": row.Id,
            "nombre_paciente": row.NombrePaciente,
            "edad": row.Edad,
            "sexo": row.Sexo,
            "padecimiento": row.Padecimiento,
            "especialidad": row.Especialidad,
            "fecha_creacion": row.FechaCreacion.strftime('%Y-%m-%d %H:%M:%S')
        }
        for row in cursor.fetchall()
    ]
    cursor.close()
    return jsonify(citas)

if __name__ == '__main__':
    app.run(debug=True)
