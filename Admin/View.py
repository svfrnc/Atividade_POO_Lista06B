from Admin.Cliente import Cliente, ClienteDAO
from Admin.Produto import Produto, ProdutoDAO
from Admin.Categoria import Categoria, CategoriaDAO
from Cliente.Carrinho import Carrinho, CarrinhoDAO

class View:
    #CLIENTE
    @staticmethod
    def cliente_listar():
        return ClienteDAO.listar()
    
    @staticmethod
    def cliente_inserir(nome, email, senha, fone):
        c = Cliente(0, nome, email, senha, fone)
        ClienteDAO.inserir(c)

    @staticmethod
    def cliente_atualizar(id, nome, email, senha, fone):
        c = Cliente(id, nome, email, senha, fone)
        return ClienteDAO.atualizar(c)
    
    @staticmethod
    def cliente_excluir(id):
        c = Cliente(id, " ", " ", " ", " ")
        return ClienteDAO.excluir(c)
    
    #CATEGORIA
    @staticmethod
    def categoria_listar():
        return CategoriaDAO.listar()
    
    @staticmethod
    def categoria_inserir(desc):
        cat = Categoria(0, desc)
        return CategoriaDAO.inserir(cat)
    
    @staticmethod
    def categoria_atualizar(desc):
        cat = Categoria(0, desc)
        return CategoriaDAO.atualizar(cat)
    
    @staticmethod
    def categoria_excluir(obj):
        cat = Categoria(obj, " ")
        return CategoriaDAO.excluir(cat)
    
    #PRODUTO
    @staticmethod
    def produto_listar():
        return ProdutoDAO.listar()
    
    @staticmethod
    def produto_inserir(descricao, preco, estoque, idCategoria):
        prod = Produto(0, descricao, preco, estoque, idCategoria)
        return ProdutoDAO.inserir(prod)
    
    @staticmethod
    def produto_atualizar(id, descricao, preco, estoque, idCategoria):
        prod = Produto(id, descricao, preco, estoque, idCategoria)
        return ProdutoDAO.atualizar(prod)
    
    @staticmethod
    def produto_excluir(id):
        prod = Produto(id, " ", " ", " ", " ")
        return ProdutoDAO.excluir(prod)
    
    @staticmethod
    def listar_vendas():
        return CarrinhoDAO.listar_compras()



