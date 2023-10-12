from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder='templates')

# Lista para almacenar las citas
lista_citas = []

# Ruta para la página principal
@app.route('/')
def mostrar_dashboard():
    return render_template('dashboard.html', citas=lista_citas)

# Ruta para agregar una cita
@app.route('/agregar_cita', methods=['POST'])
def agregar_cita():
    cita = request.form['cita']
    estado = "Pendiente"
    if cita:
        lista_citas.append({"cita": cita, "estado": estado})
    return redirect('/')

# Ruta para editar una cita
@app.route('/editar_cita/<int:index>', methods=['POST'])
def editar_cita(index):
    nueva_cita = request.form['nueva_cita']
    if nueva_cita:
        lista_citas[index]["cita"] = nueva_cita
    return redirect('/')

# Ruta para eliminar una cita
@app.route('/eliminar_cita/<int:index>')
def eliminar_cita(index):
    del lista_citas[index]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

