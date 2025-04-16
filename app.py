from flask import Flask, url_for
import sqlite3






app = Flask(__name__)


db=None

def abrirconexion():
    db = sqlite3.connect("instance/datos.sqlite")
    db.row_factory = sqlite3.Row
    return db

def cerrarconexion():
    global db
    if db is not None:
        db.close()
        db=None
       
@app.route("/usuarios")
def obtenergente():
    global db
    conexion = abrirconexion()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM usuarios')
    resultado = cursor.fetchall()
    cerrarconexion()
    fila = [dict(row) for row in resultado]
    return str(fila)


@app.route("/")
def hello_world():
    
    url_hamburguesa = url_for("COMIDA_condimentos", condimentos="chedar")
    url_papas = url_for("acompañamiento")
    url_dados = url_for("dado", caras=6)
    url_sumar = url_for("suma", n1=4, n2=9)
    url_logo = url_for("static", filename="img/rayo.png")
    
    return f"""
       <a href='{url_hamburguesa}'>HAMBUERGUESA</a>
       <a href='{url_papas}'>papas_fritas</a>
       <a href='{url_dados}'>dados</a>
       <a href='{url_sumar}'>sumar</a>
       <a href='{url_logo}'>logo</a>


"""




@app.route("/HAMBUERGUESA/<string:condimentos>")
def COMIDA_condimentos(condimentos):
    return f"<h2>amo las hamburgeesas {condimentos}</h2>"

@app.route("/papas_fritas")
def acompañamiento():
    return "<h2>papas fritas</h2>"



@app.route("/dados/<int:caras>")
def dado(caras):
    from random import randint
    numero = randint(1,caras)
    return f"<h2>dado de {caras}, salio {numero}!</h2>"



@app.route("/sumar/<int:n1>/<int:n2>")
def suma(n1,n2):
    suma = n1+n2
    return f"<h2>{n1} mas {n2} da {suma}</h2>"



