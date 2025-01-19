from flask import Flask, render_template, request, redirect, url_for ,flash
from user import user 

app = Flask(__name__)

app.secret_key ='QWERTYUIOP'

 
app.register_blueprint (user, url_prefix="/users")
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
