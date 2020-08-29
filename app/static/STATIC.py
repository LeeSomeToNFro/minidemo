import pandas as pd

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

def deck_pool():
    return [100101,100102,100103]

def init_deck():
    return [100101,100101,100101,100102,100102,100103]


def to_list(r):
    s = str(r).split(',')
    return[int(s[0]),int(s[1]),int(s[2]),int(s[3])]

def generate_card_list(id_list):
    data = pd.read_excel('app\static\cards.xlsx',sheet_name='card',index_col='id')
    card_list=[]
    #print(id_list)
    for id in id_list:
        #print(id)
        c = data.loc[id]
        r_stock=to_list(c['r_stock'])
        print(r_stock)
        card=Card(id=id,card_type=c['type'],name=c['name'],description=c['description'],\
            human=c['human'],human_rounds=c['human_rounds'],buff_id=c['buff_id'],\
                autouse=c['autouse'],counts=c['counts'],r_stock=to_list(c['r_stock']),\
                    r_capacity=to_list(c['r_capacity']),r_consumption=to_list(c['r_consume']),\
                        r_production=to_list(c['r_prod']))
        card_list.append(card)
    return card_list


def buildings():
    return [

    ]


if __name__=="__main__":
    #print(cards().loc[100101])
    print(Card(id=111,card_type='null'))
    print(generate_card_list([100101])[0].autouse)

