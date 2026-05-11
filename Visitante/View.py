from Visitante.Login import Login, LoginDAO
from Admin.Cliente import Cliente, ClienteDAO

class View:
    @staticmethod
    def criar_conta(nome, email, senha, fone):
        c = Cliente(0, nome, email, senha, fone)
        ClienteDAO.inserir(c)
    
    @staticmethod
    def login(email, senha) -> bool:
        logado = LoginDAO.logado(email, senha)
        return logado