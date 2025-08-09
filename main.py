from fastapi import FastAPI, Query
import mysql.connector as sql
from dotenv import load_dotenv
import os

load_dotenv()
user = os.getenv('user')
password = os.getenv('password')
database = os.getenv('database')


APP = FastAPI(title="API de teste")

@APP.get('/retorno')
def acessar_db(Nome : str=Query(example="Valentino"), Sobrenome : str=Query(example="Rossi")):
    try:
        cnx = sql.connect(user=user, database=database, password=password)
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT idade, cpf FROM Atletas WHERE nome=%s AND sobrenome=%s",(Nome, Sobrenome))
    except:
        return{"Erro"}
    finally:
        return {"Dados":cursor}

@APP.post('/cadastro')
def acessar_db(Nome : str=Query(example="Valentino"), Sobrenome : str=Query(example="Rossi"), Idade : int = Query(example="20",ge=18), cpf : str = Query(example="00000000000",min_length=11)):
    try:
        cnx = sql.connect(user=user, database=database, password=password)
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("INSERT INTO Atletas (nome, sobrenome, idade, cpf) values (%s,%s,%s,%s)",(Nome, Sobrenome, Idade, cpf))
    except:
        return{"Erro"}
    finally:
        cnx.commit()
        cursor.close()
        cnx.close()
        return {"Atleta cadastrado!"}