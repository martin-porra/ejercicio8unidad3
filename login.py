class login():
    __tipo = ''

    def __init__(self, nivel='comun'):
        self.__tipo = nivel

    def login(self):
        user = input('Usuario: ')
        passwd = input('Contraseña: ')
        if user.lower() == 'uTesorero'.lower() and passwd == 'ag@74ck':
            self.__tipo = 'tesorero'
            print('Se ha logueado como ' + self.__tipo)
        elif user.lower() == 'uGerente'.lower() and passwd == 'ufC77#!1':
            self.__tipo = 'gerente'
            print('Se ha logueado como ' + self.__tipo)
        else:
            print('Usuario y/o contraseña no reconocidos.')
            print('sigue logueado como usuario comun')


    def getnivel(self):
        return self.__tipo