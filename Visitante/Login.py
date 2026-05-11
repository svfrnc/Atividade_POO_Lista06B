from Admin.Cliente import Cliente, ClienteDAO

class Login:
    def __init__(self, email: str, senha: str):
        self.email = email
        self.senha = senha
    
    def __str__(self):
        return f"{self.email} - {self.senha}"

class LoginDAO:
    user_logado = False

    @classmethod
    def logado(cls, email, senha):
        ClienteDAO.abrir()

        for cliente in ClienteDAO.objetos:
            if (cliente.email == email) and (cliente.senha == senha):
                cls.user_logado = True
                return True
        
        cls.user_logado = False
        return False