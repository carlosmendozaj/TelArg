from flask import Flask, jsonify, request
from flask_cors import CORS
import csv
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return app.send_static_file('index.html')

def obtener_ultimo_id(csv_filename):
    last_id = 0
    try:
        with open(csv_filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['id'].isdigit():
                    last_id = int(row['id'])
    except FileNotFoundError:
        last_id = 0
    return last_id

@app.route('/guardar', methods=['POST'])
def guardar():
    try:
        respuesta = request.json['respuesta']
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        csv_filename = 'respuestas.csv'
        
        last_id = obtener_ultimo_id(csv_filename)
        new_id = last_id + 1  

        with open(csv_filename, 'a', newline='') as csvfile:
            fieldnames = ['id', 'timestamp', 'respuesta']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow({'id': new_id, 'timestamp': timestamp, 'respuesta': respuesta})
        
        return jsonify({'message': 'Respuesta almacenada con éxito'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
