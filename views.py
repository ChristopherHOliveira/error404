from flask import Blueprint
import re

views = Blueprint(__name__,'views')

usuarios = []       # lista de objetos 'usuários' (representação do BD):
tickets = []        # lista de objetos 'tickets' (representação do BD):

@views.route('/')
def home():
    return 'Home page'

class Usuario():                                                    # classe Usuário
    def __init__(self, nome, email, username, senha, perfil):       # parametros a serem passados como atributos do usuário
        self.nome = nome
        self.email = email
        self.username = username
        self.senha = senha
        self.perfil = perfil

    def cadastrar_usuario(nome, email, username, senha, perfil):           # método que cadastra usuário
        if Usuario.valida_email(email) == True:                            # testando se e-mail é válido
            usuarios.append(Usuario(nome, email, username, senha, perfil)) # passando o objeto usuário criado para a lista de usuários (BD)
        else:
            print(f'{email} é um email inválido')

    def valida_email(email_teste):                                 # método que valida email
        regex_mail = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'           
        if(re.search(regex_mail,email_teste)):  
            return True                                            # e retorna True se o email é um e-mail válido   
        else:  
            return False

    @views.route('/login/<username>/<senha>')
    def valida_login(username, senha):                                   # método que valida login
        for usuario in usuarios:                                         # verificando em cada usuário cadastrado
            if usuario.username == username and usuario.senha == senha:  # se há um respectivo usuário e senha cadastrados
                return '<h1>Usuário e senha corretos</h1>'
                # acessar tela principal
            else:
                return '<h1>Usuário ou senha incorretos</h1>'
                # permanecer na tela de login e exibir mensagem de erro

    @views.route('/usuarios')
    def exibir_usuarios():                          # método que exibe todos os usuários cadastrados
        out_usuarios = []                           # criando lista pra output
        for usuario in usuarios:                    # para cada usuário cadastrado
            out_usuarios.append(usuario.__dict__)   # adicionando na lista de output em formato dicionário 
        return {'Usuarios': out_usuarios}           # retornando a lista de output



class Ticket(): # classe Ticket
    def __init__(self, titulo, descricao, prioridade):      # atributos do ticket
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade

    def cadastrar_ticket(titulo, descricao, prioridade):                    # método para cadastrar ticket
        tickets.append(Ticket(titulo, descricao, prioridade))      # passando o objeto ticket criado para a lista

    def pesquisar_ticket():
        pass
    
    @views.route('/tickets')      # rota para exibir todos os tickets cadastrados
    def exibir_tickets():
        out_tickets = []
        for ticket in tickets:
            out_tickets.append(ticket.__dict__)
        return {'Tickets': out_tickets}

    @views.route('/tickets/pesq/<termo>')      # rota para pesquisar ticket que contenha determinado termo
    def pesquisar_ticket(termo):             # método que recebe o termo a ser pesquisado como parâmetro
        out_tickets = []                     # lista vazia para receber os tickets que contem o termo em questão
        for ticket in tickets:                                                  # loop em todos os tickets cadastrados
            if termo in ticket['titulo'] or termo in ticket['descricao']:       # verificando se algum ticket contem o termo no título / descrição
                out_tickets.append(ticket)                                      # adicionando o ticket encontrado na lista de output
        return {'Tickets': out_tickets}      # retornando resultado da pesquisa
        

# teste: cadastrando usuários e adicionando na lista 'usuarios':
Usuario.cadastrar_usuario('Zohan', 'zohan@error404.com', 'z.salam', 'zoh123', 'admin')
Usuario.cadastrar_usuario('Chris', 'emailerrado#provedor.com', 'c.olive', 'chr123', 'logistica')
Usuario.cadastrar_usuario('Erica', 'erica@error404.com', 'e.olive', 'eri123', 'vendas')
Usuario.cadastrar_usuario('João', 'joao@error404.com', 'j.silva', 'joa123', 'marketing')

# teste: criando ticket e adicionando na lista 'tickets':
# deve ser substituido por inputs de usuarios
Ticket.cadastrar_ticket('erro de codigo de produto', 'bla bla bla bla', 3)
Ticket.cadastrar_ticket('criação de material', 'lalalalala', 2)
Ticket.cadastrar_ticket('criação de usuário', 'xxxxxxxxxx', 3)
Ticket.cadastrar_ticket('sistema fora do ar', 'loremihvbsdhv', 1)

# imprimindo os objetos 'usuários' criados, na forma de dicionário:
#for usuario in usuarios:
#    print(usuario.__dict__)

# imprimindo os objetos 'tickets' criados, na forma de dicionário:
# for ticket in tickets:
#    print(ticket)