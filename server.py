from flask import Flask, render_template, request, redirect
from users import User

app = Flask(__name__)

@app.route('/')
def index():
    users = User.muestra_usuarios()
    return render_template("index.html",users=users)

@app.route('/new')
def new():
    return render_template("new.html")

@app.route('/create', methods=['POST'])
def create():
    #Cuando se envía el form me manda a create, pero este /create nos redirigirá a la página de inicio /
    print(request.form)
    User.guardar(request.form)
    return redirect('/')

# @app.route('/update', methods=['POST'])
# def update():
#     User.actualizar(request.form)
#     return redirect('/')


if __name__=="__main__":
    app.run(debug=True)