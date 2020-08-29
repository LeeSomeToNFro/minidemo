from app import app
from flask import request,render_template
from app.gameplay import Game,deck_pool

game = Game()

@app.route('/')
def test():
    return "test"

@app.route('/game',methods=['GET','POST'])
def gameplay():
    global game
    #print(game.deck_hand)
    if request.method=='GET':
        game.refresh(end_round=True)
        return render_template('game.html',game=game)
    
    elif request.method=="POST":
        end_round = request.form.getlist('end')
        card_spell = request.form.getlist('card_spell')
        #print(end_round)
        #print(card_spell)
        if len(end_round)>0:
            game.refresh(end_round=True)
        else:
            game.refresh(card_spell=int(card_spell[0]))
        
        return render_template('game.html',game=game)

