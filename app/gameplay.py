from app.static.CARDS import cards as card_list

def deck_pool():

    return []



class Game:

    def __init__(self,deck_pool,init_deck):
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
        self.deck_hand = []
        self.deck_grave = []

    def draw_card(num):
        if num<len(self.deck):
            for i in range(num):
                self.deck_hand.append(self.deck[0])
                del self.deck[0]
        else:
            for i in self.deck:
                self.deck_hand.append(i)
            self.deck = self.deck_grave
            self.deck_grave = []
    
    def spell_card(card_id):
        [self.stock_coal,self.stock_wood,self.stock_steel,self.stock_food] += card_list[card_id][3]



    def endround_resources():
        c = self.stock_coal + (self.production_coal-self.consumption_coal)
        self.stock_coal = [c,self.capacity_coal][c>self.capacity_coal]
        f = self.stock_food + (self.production_food-self.consumption_food)
        self.stock_food = [f,self.capacity_food][f>self.capacity_food]
        w = self.stock_wood + (self.production_wood)
        self.stock_wood = [w,self.capacity_wood][w>self.capacity_wood]
        s = self.stock_steel + (self.production_steel)
        self.stock_steel = [s,self.capacity_steel][s>self.capacity_steel]

    def refresh(self,end_round=False,card_spell='0'):
        if end_round:
            self.round+=1
            draw_card(self.num_draw)
            endround_resources()
        else:
            print(card_spell)
    
