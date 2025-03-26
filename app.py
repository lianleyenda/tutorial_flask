from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
       <a href='/HAMBUERGUESA'>HAMBUERGUESA</a>
       <a href='/papas_fritas'>papas_fritas</a>
       

"""


@app.route("/HAMBUERGUESA")
def COMIDA():
    return "<h2>amo las hamburgeesas</h2>"

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



