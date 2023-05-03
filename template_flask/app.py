from flask import render_template
from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html', name='Alessandro')

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="MC_PANINI"
)
mycursor = mydb.cursor()


@app.route('/units')
def unitList():
    mycursor.execute("Select * FROM MC_Unit")
    myresult = mycursor.fetchall()
    return render_template('MC_GG.html', units=myresult)
