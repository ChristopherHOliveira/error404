from flask import Flask

app = Flask(__name__)

usuarios = []       # lista onde serão armazenados os objetos 'usuários' (representação do BD):
tickets = []        # lista onde serão armazenados os objetos 'tickets' (representação do BD):

class Usuario():                                                    # classe Usuário
    def __init__(self, nome, email, username, senha, perfil):       # atributos do usuário
        self.nome = nome
        self.email = email
        self.username = username
        self.senha = senha
        self.perfil = perfil

    def cadastrar_usuario(nome, email, username, senha, perfil):                # método para cadastrar usuário
        usuarios.append(Usuario(nome, email, username, senha, perfil).__dict__) # passando o objeto usuário criado para a lista, já no formato dicionário

    @app.route('/usuarios')     # rota para exibir todos os usuários cadastrados
    def exibir_usuarios():
        return {'Usuarios': usuarios}

class Ticket(): # classe Ticket
    def __init__(self, titulo, descricao, prioridade):      # atributos do ticket
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade

    def cadastrar_ticket(titulo, descricao, prioridade):                    # método para cadastrar ticket
        tickets.append(Ticket(titulo, descricao, prioridade).__dict__)      # passando o objeto ticket criado para a lista, já no formato dicionário

    def pesquisar_ticket():
        pass
    
    @app.route('/tickets')      # rota para exibir todos os tickets cadastrados
    def exibir_tickets():
        return {'Tickets': tickets}

    @app.route('/tickets/pesq/<termo>')      # rota para pesquisar ticket que contenha determinado termo
    def pesquisar_ticket(termo):             # método que recebe o termo a ser pesquisado como parâmetro
        out_tickets = []                     # lista vazia para receber os tickets que contem o termo em questão
        for ticket in tickets:                                                  # loop em todos os tickets cadastrados
            if termo in ticket['titulo'] or termo in ticket['descricao']:       # verificando se algum ticket contem o termo no título / descrição
                out_tickets.append(ticket)                                      # adicionando o ticket encontrado na lista de output
        return {'Tickets': out_tickets}      # retornando resultado da pesquisa
        

# teste: cadastrando usuários e adicionando na lista 'usuarios':
Usuario.cadastrar_usuario('Zohan', 'zohan@error404.com', 'z.salam', 'zoh123', 'admin')
Usuario.cadastrar_usuario('Chris', 'chris@error404.com', 'c.olive', 'chr123', 'logistica')
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

if __name__ == "__main__":
    app.run(debug=True)