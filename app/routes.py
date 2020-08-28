from app import app
from flask import request,render_template
from app.gameplay import Game,deck_pool
init_deck=[]
game = Game(deck_pool(),init_deck)

@app.route('/')
def test():
    return "test"

@app.route('/game',methods=['GET','POST'])
def gameplay():
    global game
    if request.method=='GET':
        game.refresh(end_round=True)
        return render_template('game.html',game=game)
    
    elif request.method=="POST":
        end_round = request.form.getlist('end')
        card_spell = request.form.getlist('card_id')
        if len(end_round)>0:
            game.refresh(end_round=True)
        else:
            game.refresh(card_spell=card_spell)
        
        return render_template('game.html',game=game)

