from flask import Flask, render_template, request

app = Flask(__name__)

class Game:
    def __init__(self, name, categoty, console):
        self.name = name
        self.category = categoty
        self.console = console


game_1 = Game('Super Mario', 'arcade', 'Super Nintendo')
game_2 = Game('God of War', 'action', 'X-Box')
game_3 = Game('Syphon Filter', 'action', 'Playstation')
game_list = [game_1, game_2, game_3]


@app.route('/')
def index():
    return render_template('lista.html', title='Games', game_list=game_list)


@app.route('/novo')
def novo():
    return render_template('novo.html', title='New game')


@app.route('/criar', methods=['POST'])
def criar():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']
    game = Game(name, category, console)
    game_list.append(game)
    return render_template('lista.html', title='Games', game_list=game_list)


app.run(debug=True)
