from flask import Flask, render_template, request, redirect, url_for
import pymysql.cursors

app = Flask(__name__)

# Konfigurasi koneksi ke database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='iqbaljackpot',
                             database='tugas',
                             cursorclass=pymysql.cursors.DictCursor)

@app.route('/')
def index():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM member")
        users = cursor.fetchall()
    return render_template('index.html', users=users)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        gender = request.form['gender']
        address = request.form['address']
        phone = request.form['phone']
        ig = request.form['ig']
        status = request.form['status']
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO member (name, email, gender, addres, phone, status) VALUES (%s, %s, %s, %s, %s, %s)",
                           (name, email, gender, address, phone, status))
            connection.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM member WHERE id = %s", (id,))
        user = cursor.fetchone()
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        gender = request.form['gender']
        address = request.form['address']
        phone = request.form['phone']
        ig = request.form['ig']
        status = request.form['status']
        with connection.cursor() as cursor:
            cursor.execute("UPDATE member SET name = %s, email = %s, gender = %s, addres = %s, phone = %s, status = %s WHERE id = %s",
                           (name, email, gender, address, phone, status, id))
            connection.commit()
        return redirect(url_for('index'))
    
    return render_template('edit.html', user=user)

@app.route('/delete/<int:id>')
def delete(id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM member WHERE id = %s", (id,))
        connection.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
