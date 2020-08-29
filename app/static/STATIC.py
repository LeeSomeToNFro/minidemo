import pandas as pd
from models import Card

def cards():
    data = pd.read_excel('app\static\cards.xlsx',sheet_name='card')
    
    return data


def buildings():
    return [

    ]


if __name__=="__main__":
    print(cards())

