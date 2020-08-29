from app.static.STATIC import cards as card_list
from app.static.models import Card
import random

def deck_pool():

    return [1,2,1,2,1,2,1,2]

def build_card_list(listid):


class Game:

    def __init__(self):
        self.deck_pool = deck_pool
        self.deck = init_deck

        self.round=0

        #----资源-----
        self.temperature = -10
        self.fire_level = 0
        self.warm = 0
        self.population_idle=20
        self.population_labor=20
        self.population_total=20
        self.stock_coal=200
        self.capacity_coal=500
        self.consumption_coal=0
        self.production_coal=0
        self.stock_wood=100
        self.capacity_wood=200
        self.production_wood=0
        self.stock_steel=0
        self.capacity_steel=100
        self.production_steel=0
        self.stock_food=100
        self.capacity_food=200
        self.consumption_food=20
        self.production_food=0
        #--------------
        self.num_draw=3
        self.deck_hand = Hands()
        self.deck_grave = Deck()

    def draw_card(self,num):
        redraw = False
        if not num<len(self.deck):
            num = len(self.deck)
            redraw = True
        for i in range(num):
            card = card_list()[self.deck[0]]
            desp = "["+card[0]+"]"+card[1]+'-'+card[2]
            self.deck_hand.append({'hand_id':0,"card_id":self.deck[0],"description":desp})
            print("player draw card-ID:"+str(self.deck[0]))
            del self.deck[0]
        self.reindex_hand()
        if redraw:
            self.deck = self.deck_grave
            random.shuffle(self.deck)
            self.deck_grave = []       
    
    def spell_card(self,hand_card_id):
        card_id=self.deck_hand[hand_card_id]["card_id"]
        print("player used card-ID:"+str(card_id))
        rc = card_list()[card_id][3]
        self.stock_coal += rc[0]
        self.stock_wood += rc[1]
        self.stock_steel += rc[2]
        self.stock_food += rc[3]

        self.deck_grave.append(card_id)
        del self.deck_hand[hand_card_id]
        self.reindex_hand()

    def apply_rc(self,rc_stock=[0,0,0,0],rc_capacity=[0,0,0,0],rc_consum=[0,0,0,0],rc_prod=[0,0,0,0]):
        self.stock_coal+=rc_stock[0]
        self.stock_wood+=rc_stock[1]
        self.stock_steel+=rc_stock[2]
        self.stock_food+=rc_stock[3]
        self.capacity_coal+=rc_capacity[0]
        self.capacity_wood+=rc_capacity[1]
        self.capacity_steel+=rc_capacity[2]
        self.capacity_food+=rc_capacity[3]
        self.consumption_coal+=rc_consum[0]
        self.consumption_food+=rc_consum[3]
        self.production_coal+=rc_prod[0]
        self.production_wood+=rc_prod[1]
        self.production_steel+=rc_prod[2]
        self.production_food+=rc_prod[3]
    

    def endround_resources(self):
        c = self.stock_coal + (self.production_coal-self.consumption_coal)
        self.stock_coal = [c,self.capacity_coal][c>self.capacity_coal]
        f = self.stock_food + (self.production_food-self.consumption_food)
        self.stock_food = [f,self.capacity_food][f>self.capacity_food]
        w = self.stock_wood + (self.production_wood)
        self.stock_wood = [w,self.capacity_wood][w>self.capacity_wood]
        s = self.stock_steel + (self.production_steel)
        self.stock_steel = [s,self.capacity_steel][s>self.capacity_steel]

    def refresh(self,end_round=False,card_spell='Null'):
        if end_round:
            self.round+=1
            self.draw_card(self.num_draw)
            self.endround_resources()
        else:
            self.spell_card(card_spell)
    

class Deck:
    def __init__(self,card_list=[]):
        self.card_list=card_list
    def append(self,card):
        self.card_list.append(card)
    def draw(self,index):
        del self.card_list[index]
    def shuffle(self):
        random.shuffle(self.card_list)

class Hands:
    def __init__(self,card_list=[]):
        self.card_list=[]
        l = len(card_list)
        if l>0:
            for j in range(l):
                card={"index":j,"card":card_list[j]}
                self.card_list.append(card)
    def append(self,card):
        self.card_list.append({"index":len(self.card_list),"card":card})
    def reindex(self):
        for i in range(len(self.card_list)):
            self.card_list[i]["index"]=i
    def draw(self,index):
        if not self.card_list[index]["index"]==index:
            self.reindex()
        del self.card_list[index]
        self.reindex()
    def shuffle(self):
        random.shuffle(self.card_list)
        self.reindex

