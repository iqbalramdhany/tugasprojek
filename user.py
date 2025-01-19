from flask import Flask, render_template, request, redirect, url_for, Blueprint, flash
import pymysql.cursors
from conn import connection

user = Blueprint ('user', __name__)

@user.route('/')
def index():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
    return render_template('users.html', users=users)

@user.route('/users.add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        group_id = request.form['group_id']
        is_enabled = True

        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO users (name, username, password, group_id, is_enabled) VALUES (%s, %s, %s, %s, %s)",
                           (name, username, password, group_id, is_enabled))
            connection.commit()

        flash('User baru berhasil dibuat')
        return redirect(url_for('user.add'))
    return render_template('users_add.html')

@user.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
        user = cursor.fetchone()
    
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        group_id = request.form['group_id']
        is_enabled = request.form['is_enabled']
        if is_enabled.lower() in (1,'1','True'):
            is_enabled = 1
        elif is_enabled.lower() in (0,'0','False'):
            is_enabled = 0

        with connection.cursor() as cursor:
            cursor.execute("UPDATE users SET name = %s, username = %s, password = %s, group_id = %s, is_enabled = %s WHERE id = %s",
                           (name, username, password, group_id, is_enabled, id))
            connection.commit()
        #return redirect(url_for('user.add'))
    
    return render_template('users_edit.html', user=user)

@user.route('/delete/<int:id>')
def delete(id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM users WHERE id = %s", (id,))
        connection.commit()
    return redirect(url_for('users'))
