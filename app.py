from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuración de la base de datos MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'         # Cambia según tu usuario MySQL
app.config['MYSQL_PASSWORD'] = ''         # Cambia según tu contraseña MySQL
app.config['MYSQL_DB'] = 'red_social_universitaria'  # Nombre correcto de la base de datos

mysql = MySQL(app)

@app.route('/registro', methods=['GET', 'POST'])
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        correo = request.form.get('correo')
        contrasena = request.form.get('contrasena')
        carrera = request.form.get('carrera')
        foto_perfil = request.form.get('foto_perfil')  # puede estar vacío

        cursor = mysql.connection.cursor()
        cursor.execute("""
            INSERT INTO usuarios (nombre, correo, contraseña, carrera, foto_perfil)
            VALUES (%s, %s, %s, %s, %s)
        """, (nombre, correo, contrasena, carrera, foto_perfil))
        mysql.connection.commit()
        cursor.close()

        return redirect('/registro')

    return render_template('registro.html')


@app.route('/')
def home():
    return "Hola, Flask está funcionando!"

if __name__ == '__main__':
    app.run(debug=True)
