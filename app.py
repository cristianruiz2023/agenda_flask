from flask import Flask, render_template, request,redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#mysql conections
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'cris'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'app_flask'
mysql = MySQL(app)

#sessions
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM contact")
    data = cursor.fetchall()
    return render_template('index.html', contacts=data)

@app.route('/add_contact',methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO contact (fullname, phone, email) VALUES (%s, %s, %s)", (fullname, phone, email))
        mysql.connection.commit()
        flash('contact save success',)
        return redirect(url_for('index'))

@app.route('/edit')
def edit_contact():
    return 'Hello edit'

@app.route('/delete_contact')
def delete_contact():
    return 'Hello delete'



if __name__ == '__main__':
    app.run(port=8080, debug=True)