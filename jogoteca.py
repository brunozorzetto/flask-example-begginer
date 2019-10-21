from flask import Flask, render_template

app = Flask(__name__)

class Game:
    def __init__(self, name, categoty, console):
        self.name = name
        self.category = categoty
        self.console = console


@app.route('/start')
def hello():
    game_1 = Game('Super Mario', 'arcade', 'Super Nintendo')
    game_2 = Game('God of War', 'action', 'X-Box')
    game_3 = Game('Syphon Filter', 'action', 'Playstation')

    game_list = [game_1, game_2, game_3]

    return render_template('lista.html', title='Games', game_list=game_list)

app.run()
