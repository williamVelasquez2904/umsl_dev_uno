import mysql.connector

def obtener_conexion():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bdumsl"
    )
    return conn
