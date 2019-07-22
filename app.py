import sqlite3
from flask import Flask, render_template

app = Flask(__name__)
app.Debug = True


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login', method=['POST'])
def login():
    return render_template('login.html')


@app.route('/operator')
def operator():
    con = sqlite3.connect(r'.\db\visitResult.db')
    c = con.cursor()
    sql = "SELECT * FROM response_result"
    resultlist = c.execute(sql).fetchall()
    c.close()
    return render_template('operator.html', resultlist=resultlist)


if __name__ == '__main__':
    app.run()
