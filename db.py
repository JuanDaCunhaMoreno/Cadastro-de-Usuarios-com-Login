#Conexão com MySQL
import mysql.connector

def conectar():
    return mysql.connector.connect(
        host= "localhost",
        user= "seu_usuario_mysql",
        password= "sua_senha_mysql",
        database= "sistema_login"
    )
