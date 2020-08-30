import pandas as pd
from app.models import Card

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
        #print(r_stock)
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

