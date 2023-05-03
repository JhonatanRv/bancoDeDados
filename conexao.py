import mysql.connector

def conectar():
  mydb = mysql.connector.connect(
    host="basedados.cqhtrkp0i9p9.us-east-1.rds.amazonaws.com",
    user="admin",
    password="aulanoiteFaculdade",
    database="aula"
  )
  return mydb