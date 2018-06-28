from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'hola'
app.config['MYSQL_DB'] = 'sensor'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/', methods=['GET'])
def index():
    return jsonify({"saludo":"hola"})

@app.route('/sensor', methods=['POST'])
def sensor():
    data = request.get_json()
    statu = data['statu']
    voltage = data['voltage']
    time = data['time']

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO sensor(statu, voltage, time) VALUE(%s, %s, %s)", (statu, voltage, time))
    mysql.connection.commit()
    cursor.close()
    return jsonify({"statu":"ok"})

if __name__ == '__main__':
	app.secret_key='secret123'
	app.run(host= '0.0.0.0')
