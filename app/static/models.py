class Card:
    def __init__(self,id,card_type,name="Null",description="Null",r_stock=[0,0,0,0],\
        r_capacity=[0,0,0,0],r_production=[0,0,0,0],r_consumption=[0,0,0,0],buff_id=0,\
            tier=1,autouse=False,human=0,human_rounds=1,counts=0):
        self.id=id
        self.type=card_type
        self.name=name
        self.description=description
        self.r_stock=r_stock
        self.r_capacity=r_capacity
        self.r_production=r_production
        self.r_consumption=r_consumption
        self.buff_id=buff_id
        self.tier=tier
        self.autouse=autouse
        self.counts=counts
        self.human=human
        self.human_rounds=human_rounds