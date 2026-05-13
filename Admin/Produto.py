import json
class Produto:
    def __init__(self, id: int, descricao: str, preco: float, estoque: int, idCategoria: int ):
        self.id = id
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        self.idCategoria = idCategoria
    def __str__(self) -> str:
        return f"{self.id} - {self.descricao} - {self.preco} - {self.estoque} - {self.idCategoria}"
    
class ProdutoDAO:
    objetos: list[Produto] = []

    @staticmethod
    def inserir(obj: Produto) -> None:
        ProdutoDAO.abrir()
        if len(ProdutoDAO.objetos) == 0:
            id = 1
        else:
            id = (max(ProdutoDAO.objetos, key = lambda x : x.id)).id + 1
        obj.id = id
        ProdutoDAO.objetos.append(obj)
        ProdutoDAO.salvar()
    
    @staticmethod
    def listar() -> list[Produto]:
        ProdutoDAO.abrir()
        ProdutoDAO.objetos.sort(key = lambda x : x.descricao)
        return ProdutoDAO.objetos
    
    @staticmethod
    def listar_id(id: int) -> Produto | None:
        ProdutoDAO.abrir()
        for obj in ProdutoDAO.objetos:
            if obj.id == id:
                return obj
        return None
    
    @staticmethod
    def atualizar(obj: Produto) -> None:
        x = ProdutoDAO.listar_id(obj.id)
        if x != None:
            ProdutoDAO.objetos.remove(x)
            ProdutoDAO.objetos.append(obj)
            ProdutoDAO.salvar() 

    @staticmethod
    def excluir(obj: Produto) -> None:
        x = ProdutoDAO.listar_id(obj.id)
        if x != None:
            ProdutoDAO.objetos.remove(x)
            ProdutoDAO.salvar()

    @staticmethod
    def salvar() -> None:
        with open("produtos.json", mode = "w") as arquivo:
            json.dump(ProdutoDAO.objetos, arquivo, default = vars)

    @staticmethod
    def abrir() -> None:
        ProdutoDAO.objetos = []
        try:
            with open("produtos.json", mode = "r") as arquivo:
                objetos_json = json.load(arquivo)
                for obj in objetos_json:
                    p = Produto(obj["id"], obj["descricao"], obj["preco"], obj["estoque"], obj["idCategoria"])
                    ProdutoDAO.objetos.append(p)
        except FileNotFoundError:
            ProdutoDAO.objetos = []