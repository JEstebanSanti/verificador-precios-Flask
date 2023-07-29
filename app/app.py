from flask import Flask, render_template, request, jsonify
import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="jban",
    passwd ="",
    database="pos"
    )

app = Flask(__name__)

@app.route("/",  methods = (['POST', 'GET']))
def index():
    try:
        codigo = str(request.form.get("codigo"))
        query = "SELECT codigo, nombre, precio FROM productos WHERE codigo={}".format(codigo)
        cursor = db.cursor()
        cursor.execute(query)
        res = cursor.fetchall()
        for fila in res:
            producto= [{'codigo':fila[0], 'nombre':fila[1], 'precio':fila[2]}]
        return render_template('producto.html', producto=producto)    

    except:
        return render_template('index.html')


