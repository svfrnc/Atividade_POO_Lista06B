# from Cliente import Cliente, ClienteDAO
# from Categoria import Categoria, CategoriaDAO
# from Produto import Produto, ProdutoDAO
from Admin.View import View as AdminView
from Visitante.View import View as LoginView
class UI:
    @staticmethod
    def home():
        print ("Digite '1' para criar conta.")
        print ("Digite '2' para criar logar no sistema.")
        print ("Digite '0' para fechar o sistema.")
        resposta = int(input("Resposta: "))
        if resposta == 1:
            UI.criar_usuario()
        elif resposta == 2:
            UI.validacao()
        else:
            print("Fechando o sistema...")

    @staticmethod
    def criar_usuario():                           
        print("Cadastro de Clientes")
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        senha = input("Informe a senha: ")
        fone = input("Informe o fone: ")
        # c = View(0, nome, email, fone)
        AdminView.cliente_inserir(nome, email, senha, fone)
        UI.home()
    @staticmethod
    def validar_login():
        print("Insira o seu Email e Senha: ")
        email = input("digite o seu email: ")
        senha = input("insira a sua senha: ")

        if LoginView.login(email, senha):
            if (senha == "admin@email.com") and (senha == "12345"):
                print("admin logado com sucesso.")
                UI.main()
            else:
                print("login efetuado com sucesso.")
                UI.cliente_main()
        else:
            print ("enderço de email e/ou senha incorreto(s).")

    @staticmethod
    def main():
        op = 0
        while op != 13:
            op = UI.menu()
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()
            if op == 5: UI.categoria_inserir()
            if op == 6: UI.categoria_listar()
            if op == 7: UI.categoria_atualizar()
            if op == 8: UI.categoria_excluir()
            if op == 9: UI.produto_inserir()
            if op == 10: UI.produto_listar()
            if op == 11: UI.produto_atualizar()
            if op == 12: UI.produto_excluir()
    
    @staticmethod
    def cliente_main():
        op = 0
        while op != 6:
            op = UI.cliente_menu()
            if op == 1: UI.inserir_produto()
            if op == 2: UI.listar_produtos()
            if op == 3: UI.listar_compras()
            if op == 4: UI.visualizar_carrinho()
            if op == 5: UI.comprar_carrinho()


    @staticmethod
    def menu():
        print("----- Clientes -----")
        print("1-Inserir 2-Listar 3-Atualizar 4-Excluir")
        print("----- Categorias -----")
        print("5-Inserir 6-Listar 7-Atualizar 8-Excluir")
        print("----- Produtos -----")
        print("9-Inserir 10-Listar 11-Atualizar 12-Excluir")
        print("13-Fim")
        return int(input("Selecione uma opção: "))
    
#CLIENTE
    @staticmethod
    def cliente_menu():
        print("1 - Inserir produto")
        print("2 - Listar produtos")
        print("3 - Lisar Compras")
        print("4 - Visualizar Carrinho")
        print("5 - Comprar Carrinho")
        print("6 - Sair do Sistema")

        return int(input("Informe uma opção: "))
    
    @staticmethod
    def cliente_inserir():                           
        print("Cadastro de Clientes")
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        senha = input("Informe a senha: ")
        fone = input("Informe o fone: ")
        AdminView.cliente_inserir(nome, email, senha, fone)

    @staticmethod
    def cliente_listar():                            
        print("Listagem de Clientes")
        for c in AdminView.cliente_listar():
            print(c)

    @staticmethod
    def cliente_atualizar():                         
        UI.cliente_listar()
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        senha = input("Informe a nova senha: ")
        fone = input("Informe o novo fone: ")
        AdminView.cliente_atualizar(id, nome, email, senha, fone)

    @staticmethod
    def cliente_excluir():                           
        UI.cliente_listar()
        id = int(input("Informe o id do cliente a ser excluído: "))
        AdminView.cliente_excluir(id)

#CATEGORIA
    @staticmethod
    def categoria_inserir():                           
        print("Cadastro de Categorias")
        desc = input("Informe a descrição: ")
        AdminView.categoria_inserir(desc)

    @staticmethod
    def categoria_listar():                            
        print("Listagem de Categorias")
        for c in AdminView.categoria_listar():
            print(c)

    @staticmethod
    def categoria_atualizar():
        UI.categoria_listar()
        id = int(input("Informe o id da categoria a ser atualizado: "))
        desc = input("Informe a nova descrição: ")
        AdminView.categoria_atualizar(id, desc)

    @staticmethod
    def categoria_excluir():
        UI.categoria_listar()
        id = int(input("Informe o id da categoria a ser excluído: "))
        AdminView.categoria_excluir(id)

# PRODUTO
    @staticmethod
    def produto_inserir():
        print("Cadastro de Produtos")
        descricao = input("Informe a descrição: ")
        preco = float(input("Informe o preço: "))
        estoque = int(input("Informe a quantidade em estoque: "))
        idCategoria = int(input("Insira a categoria do produto: "))
        AdminView.categoria_inserir(descricao, preco, estoque, idCategoria)

    @staticmethod
    def produto_listar():
        print("Listagem de Produtos")
        for p in AdminView.produto_listar():
            print(p)
    
    @staticmethod
    def produto_atualizar():
        UI.produto_listar()
        id = int(input("Insira o id do produto a ser atualizado: "))
        descricao = input("Insira a nova descrição: ")
        preco = float(input("Insira o novo preço: "))
        estoque = int(input("Insira a nova quantidade em estoque: "))
        idCategoria = int(input("Insira o id da nova categoria do produto: "))
        AdminView.produto_atualizar(id, descricao, preco, estoque, idCategoria)
    
    @staticmethod
    def produto_excluir():
        UI.produto_listar()
        id = int(input("Insira o id do produto a ser excluído: "))
        AdminView.produto_excluir(id)


UI.home()