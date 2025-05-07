from flask import Flask, url_for, render_template
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
    url_insert = url_for("insertar_usuario", nombre="Lian Leyenda", email="Leyenditas78@gmail.com" )
    url_borar = url_for("borrar_usuario", id=1)
    url_mostrar = url_for("mostrar_usuario", id=2)
    url_insert = url_for("cambiar_usuario", nombre="tomas", email="Quispe78@gmail.com" )
    url_todos = url_for("mostrar_td")
   
    
    return f"""
       <ul>
       <li><a href='{url_hamburguesa}'>HAMBUERGUESA</a></li>
       <li><a href='{url_papas}'>papas_fritas</a></li>
       <li><a href='{url_dados}'>dados</a></li>
       <li><a href='{url_sumar}'>sumar</a></li>
       <li><a href='{url_logo}'>logo</a></li>
       <li><a href='{url_insert}'>insertar usuarios</a></li>
       <li><a href='{url_borar}'>borrar usuarios</a></li>
       <li><a href='{url_mostrar}'>mostrar usuarios</a></li>
       <li><a href='{url_insert}'>cambiar usuarios</a></li>
      </ul>

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





db = None


def dict_factory(cursor, row):
  """Arma un diccionario con los valores de la fila."""
  fields = [column[0] for column in cursor.description]
  return {key: value for key, value in zip(fields, row)}


def abrirConexion():
   global db
   db = sqlite3.connect("instance/datos.sqlite")
   db.row_factory = dict_factory


def cerrarConexion():
   global db
   db.close()
   db = None


@app.route("/test-db-agregar/<string:nombre>/<string:email>")
def insertar_usuario(nombre,email):
    abrirConexion()
    db.execute("INSERT INTO usuarios(usuario, email) VALUES(?, ?)", (nombre, email))
    db.commit()
    cerrarConexion()
    return f"agregue el {nombre} y el {email}."

@app.route("/test-db-borrar/<int:id>")
def borrar_usuario(id):
    abrirConexion()
    db.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    db.commit()
    cerrarConexion()
    return f"El usuario con ID {id} fue borrado."

@app.route("/test-db-mostrar/<int:id>")
def mostrar_usuario(id):
    abrirConexion()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
    usuario = cursor.fetchall()
    cerrarConexion()

    if usuario:
        return f"{usuario}"
    else:
        return f"No se encontró un usuario con ID {id}"


@app.route("/test-db-cambiar/<string:nombre>/<string:email>")
def cambiar_usuario(nombre,email):
    abrirConexion()
    db.execute("UPDATE usuarios SET email = ? WHERE usuario = ?", (email,nombre ,))
    db.commit()
    cerrarConexion()
    return f"cambie el {nombre} y el {email}."


@app.route("/test-db-plantilla/<int:id>")
def mostrar_plantilla(id):
    abrirConexion()
    cursor = db.execute("SELECT id, usuario, email FROM usuarios WHERE id = ?", (id,))
    res = cursor.fetchone()
    cerrarConexion()
    usuario = None
    email = None
    if res != None:
        usuario = res['usuario']
        email = res['email']
    return render_template("index.html", id=id, usuario=usuario, email=email)


@app.route("/test-db-pt/<int:id>")
def mostrar_pt(id):
    abrirConexion()
    cursor = db.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
    res = cursor.fetchone()
    cerrarConexion()
    usuario = None
    email = None
    telefono = None
    direccion = None
    if res != None:
        usuario = res['usuario']
        email = res['email']
        telefono = res['telefono']
        direccion = res['direccion']
    return render_template("index2.html", id=id, usuario=usuario, email=email, telefono=telefono, direccion=direccion)

@app.route("/test-db-td")
def mostrar_td():
    abrirConexion()
    cursor = db.execute("SELECT * FROM usuarios")
    res = cursor.fetchall()
    cerrarConexion()
    return render_template("index3.html", usuarios=res)
