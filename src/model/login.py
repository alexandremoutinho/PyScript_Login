


dados_login ={

    "usuario": "app@acsystem.site",
    'senha':'teste'

}

user = Element('user')
pwd =Element ('pwd')
def valida_user(user,pwd):

    if(user==dados_login['usuario'] and pwd==dados_login['senha']):return True
    else: return False




print(valida_user('app@acsystem.site','teste'))