from flask import render_template
from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html', name='Alessandro Dobinda')

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="MC_PANINI"
)
mycursor = mydb.cursor()


@app.route('/panini')
def unitList():
    mycursor.execute("Select * FROM MC_Unit")
    myresult = mycursor.fetchall()
    return render_template('MC_GG.html', panini=myresult)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="MC_PANINI"
)
mycursor = mydb.cursor()

@app.route('/Big_Mac')
def panino_Big_Mac():
    mycursor.execute("SELECT * FROM MC_Unit ")
    myresult = mycursor.fetchall()
    return render_template('Big_Mac.html', Big_Mac=myresult)