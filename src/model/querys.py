from conect_db import mysql_connection
conexao = mysql_connection()
cmd = conexao.cursor()



def valida_login(user,pwd):
	vl_login = False
	cmd.execute('Select * from usuario')
	lista_user = cmd.fetchall()
	for row in lista_user:
		usuario = str(row[2])
		senha = str(row[3])
		if(user in usuario):
			if(pwd==senha):
				vl_login=True
				
				break
	return vl_login


get_login = valida_login('admin@acsystem.site','admin@210719')

print(f'Usuaio e Senha {get_login}')