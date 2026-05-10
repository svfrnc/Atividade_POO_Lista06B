from Cliente.login import login, loginDAO
from Admin.Cliente import Cliente, ClienteDAO

class View:
    @staticmethod
    def criar_conta(nome, senha, email, fone):
        c = Cliente(0, nome, senha, email, fone)
        ClienteDAO.inserir(c)
    
    @staticmethod
    def login(email, senha) -> bool:
        logado = loginDAO.logado(email, senha)
        return logado