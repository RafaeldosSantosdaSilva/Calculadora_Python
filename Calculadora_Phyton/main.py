from flask import Flask, request, render_template
from oper import Soma, Sub, Div, Mult

#necessário instalar a bliblioteca flask
#terminal: pip install flask

app = Flask(__name__, template_folder="./src/views")

@app.route("/results", methods=["POST"])
def resultado():

    if (request.method == "POST"):
        val1 = request.form["value1"]
        val2 = request.form["value2"]
        ope = request.form["op"]

    if(ope=="soma"):

     return Soma (val1,val2)

    elif(ope=="sub"):

        return Sub(val1,val2)

    elif(ope=="mult"):
        return Mult(val1,val2)

    else:
        return Div(val1,val2)



@app.route("/")
def calculadora():
    return render_template("index.html"), 200

@app.errorhandler(404)
def not_found(error):
    return "Essa página não existe"

app.run(port=8080, debug=True)