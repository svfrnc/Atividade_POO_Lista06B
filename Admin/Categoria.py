import json

class Categoria:
    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao
    def __str__(self):
        return f"{self.id} - {self.descricao}"
    
class CategoriaDAO:
    objetos = []

    @staticmethod
    def inserir(obj):
        CategoriaDAO.abrir()
        if len(CategoriaDAO.objetos) == 0: 
            id = 1
        else: 
            id = (max(CategoriaDAO.objetos, key = lambda x : x.id)).id + 1
        obj.id = id
        CategoriaDAO.objetos.append(obj)
        CategoriaDAO.salvar()

    @staticmethod
    def listar():
        CategoriaDAO.abrir()
        CategoriaDAO.objetos.sort(key = lambda x : x.descricao)
        return CategoriaDAO.objetos
    
    @staticmethod
    def listar_id(id):
        CategoriaDAO.abrir()
        for obj in CategoriaDAO.objetos:
            if obj.id == id: 
                return obj
        return None    
        
    @staticmethod
    def atualizar(obj):
        x = CategoriaDAO.listar_id(obj.id)
        if x != None:
            CategoriaDAO.objetos.remove(x)
            CategoriaDAO.objetos.append(obj)
            CategoriaDAO.salvar()

    @staticmethod
    def excluir(obj):
        x = CategoriaDAO.listar_id(obj.id)
        if x != None:
            CategoriaDAO.objetos.remove(x)
            CategoriaDAO.salvar()

    @staticmethod
    def salvar():
        with open("categorias.json", mode="w") as arquivo:
            json.dump(CategoriaDAO.objetos, arquivo, default = vars)
                         
    @staticmethod
    def abrir():
        CategoriaDAO.objetos = []
        try:
            with open("categorias.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)
                for obj in objetos_json:
                    c = Categoria(obj["id"], obj["descricao"])
                    CategoriaDAO.objetos.append(c)        
        except FileNotFoundError:
            CategoriaDAO.objetos = []