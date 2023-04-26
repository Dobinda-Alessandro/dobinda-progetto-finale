# save this as app.py
import mysql.connector
import pandas as pd

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()

#Create the DB (if not already exists)
mycursor.execute("CREATE DATABASE IF NOT EXISTS MC_PANINI")

#Create the table for the csv data (if not exists)
mycursor.execute("""
  CREATE TABLE IF NOT EXISTS MC_PANINI.MC_Unit (
    nome_panino VARCHAR(60),
    costo VARCHAR(60),
    calorie VARCHAR(60),
    voto_gusto VARCHAR(60),
  );""")

#Delete data from the table Clsh_Unit
mycursor.execute("DELETE FROM MC_PANINI.MC_Unit")
mydb.commit()

#Read data from a csv file
Mc_data = pd.read_csv('./tabella_mc.csv', index_col=False, delimiter = ',')
Mc_data = Mc_data.fillna('Null')
print(Mc_data.head(15))

#Fill the table
for i,row in Mc_data.iterrows():
    cursor = mydb.cursor()
    #here %S means string values 
    sql = "INSERT INTO MC_PANINI.MC_Unit VALUES (%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Record inserted")
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * FROM MC_PANINI.MC_Unit")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)