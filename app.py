from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuración de la base de datos MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'         # Cambia según tu usuario MySQL
app.config['MYSQL_PASSWORD'] = ''         # Cambia según tu contraseña MySQL
app.config['MYSQL_DB'] = 'red_social'     # Cambia por el nombre de tu base de datos

mysql = MySQL(app)


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre_completo = request.form.get('nombre_completo')
        nombre_usuario = request.form.get('nombre_usuario')
        correo = request.form.get('correo')
        contrasena = request.form.get('contrasena')

        # Guardar datos en la base
        cursor = mysql.connection.cursor()
        cursor.execute("""
            INSERT INTO usuarios (nombre_completo, nombre_usuario, correo, contrasena)
            VALUES (%s, %s, %s, %s)
        """, (nombre_completo, nombre_usuario, correo, contrasena))
        mysql.connection.commit()
        cursor.close()
        return redirect('/registro')  # Puedes cambiar esto por otra página o mensaje

    return render_template('registro.html')

@app.route('/')
def home():
    return "Hola, Flask está funcionando!"

if __name__ == '__main__':
    app.run(debug=True)
