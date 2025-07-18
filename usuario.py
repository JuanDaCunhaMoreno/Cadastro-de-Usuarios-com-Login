from db import conectar
from utils import gerar_hash, verificar_senha

def cadastrar_usuario(nome, email, senha):
    conn = conectar()
    cursor = conn.cursor()

    senha_criptografada = gerar_hash(senha)

    try:
        cursor.execute(""""
            INSERT INTO usuarios (nome, email, senha_hash)
            VALUES (%s, %s, %s,)
            """, (nome, email, senha_criptografada.decode('utf-8')))
        conn.commit()
        print("✅ Usuário cadastrado com sucesso!")
    except Exception as e:
        print("❌ Erro ao cadastrar usuário:", e)
    finally:
        conn.close()

def login(email, senha):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT senha_hash FROM usuarios WHERE email = %s",(email))
    resultado = cursor.fetchone

    if resultado:
        senha_hash = resultado[0]
        if verificar_senha(senha, senha_hash):
            print("✅ Login realizado com sucesso!")
        else:
            print("❌ Senha incorreta!")
    else:
        print("❌ Usuário não encontrado!")
    conn.close()