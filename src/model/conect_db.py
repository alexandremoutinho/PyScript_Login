from mysql.connector import connect
import dados
cn = dados.get_crendenciais()

def mysql_connection():
	connection = connect(
        host = str(cn["host"][0]),
        user = str(cn['user'][0]),
        passwd = str(cn["senha"][0]),
        database = str(cn["banco"][0])
    )
	return connection



