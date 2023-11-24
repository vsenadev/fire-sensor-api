import sqlite3
from flask import Flask, request, jsonify
from datetime import datetime, timedelta


def create_database():
    conn = sqlite3.connect('fire-sensor.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensor (
            id INTEGER PRIMARY KEY,
            date TEXT
        )
    ''')
    conn.commit()
    conn.close()


def post_fire():
    conn = sqlite3.connect('fire-sensor.db')
    cursor = conn.cursor()
    current_date_time = datetime.now()
    formatted = "%d/%m/%Y %H:%M"
    current_date_time_formatted = current_date_time.strftime(formatted)

    cursor.execute("INSERT INTO sensor (date) VALUES (?)", (current_date_time_formatted,))
    conn.commit()
    conn.close()


def get_sensor_ocurrences():
    conn = sqlite3.connect('fire-sensor.db')
    cursor = conn.cursor()

    data_hora_atual = datetime.now()

    data_hora_10min_antes = data_hora_atual - timedelta(minutes=10)

    data_hora_10min_antes_str = data_hora_10min_antes.strftime("%d/%m/%Y %H:%M")

    cursor.execute("SELECT * FROM sensor WHERE date >= ?", (data_hora_10min_antes_str,))

    data = cursor.fetchall()

    conn.close()

    return data


app = Flask(__name__)


@app.route('/post', methods=['GET'])
def retrieve_data():
    create_database()
    post_fire()
    return jsonify({"status": "Informação de íncendio disparada"})


@app.route('/ocurrences', methods=['GET'])
def get_ocurrences():
    response = get_sensor_ocurrences()

    if response:
        return jsonify({"status": True})
    else:
        return jsonify({"status": False})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
