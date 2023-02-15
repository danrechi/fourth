import requests
from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(database="service_db",
                        user="postgres",
                        password="2104",
                        host="localhost",
                        port="5432")
cursor = conn.cursor()
cursor.execute("SELECT * FROM service.users")
a = list(cursor.fetchall())


@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')

@app.route('/login/', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    cursor.execute("SELECT * FROM service.users")
    records = list(cursor.fetchall())
    if not username or not password:
        return render_template('error.html')



    cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
    records = list(cursor.fetchall())
    if len(records) == 0:
        return render_template('wrong.html')

    return render_template('account.html', full_name=records[0][1], login=records[0][2], password=records[0][3])


