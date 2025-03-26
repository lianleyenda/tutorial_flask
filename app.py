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



@app.route("/papas_fritas")
def acompañamiento():
    return "<h2>papas fritas</h2>"

