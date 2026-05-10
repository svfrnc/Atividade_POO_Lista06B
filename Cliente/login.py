from Admin.Cliente import Cliente, ClienteDAO
class login:
    def __innit__(self, email, senha):
        self.email = email
        self.senha = senha
    def __str__(self):
        return f"{self.email} - {self.senha}"

class loginDAO:
    user_logado = False
    
    @classmethod
    def logado(cls, email, senha) -> bool:
        ClienteDAO.abrir()
        for cliente in ClienteDAO.objetos:
            if (cliente.email == True) and (cliente.senha == true):
                cls.user_logado = True
                return True
            
        cls.user_logado = False
        return False