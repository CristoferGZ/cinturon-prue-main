from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista de eventos
events = []

# Ruta principal
@app.route('/')
def index():
    return render_template('fechas.html', events=events)

# Ruta para agregar un evento


# Ruta para eliminar un evento
@app.route('/delete/<int:event_id>')
def delete(event_id):
    del events[event_id]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
