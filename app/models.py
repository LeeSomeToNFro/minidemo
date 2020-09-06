import pandas as pd

class Card:
    def __init__(self,id,type_card,human,name="null",description="null",human_rounds=1,autouse=False,effect_id=[],effect_param=[]):
        self.id=id
        self.type=type_card
        self.human=human
        self.human_rounds=human_rounds
        self.name=name
        self.description=description
        self.autouse=autouse
        self.effect_id=effect_id
        self.effect_param=effect_param
        

class City:
    def __init__(self):
        self.resource={}
        rc=pd.read_excel('app\static\config.xlsx',sheet_name='resource')
        for i in range(len(rc)):
            c = rc.iloc[i]
            self.resource[c['id']]=c['value']
    
    def endround_rc(self):
        self.resource[100]+=(self.resource[102]-self.resource[103])
        self.resource[200]+=(self.resource[202]-self.resource[203])
        self.resource[300]+=(self.resource[302]-self.resource[303])
        self.resource[400]+=(self.resource[402]-self.resource[403])
        [self.resource[100],self.resource[200],self.resource[300],self.resource[400]] =self.inbound(\
            [self.resource[100],self.resource[200],self.resource[300],self.resource[400]],\
                [self.resource[101],self.resource[201],self.resource[301],self.resource[401]])

    
    def inbound(self,a,b):
        result=[]
        for i in range(len(a)):
            temp = a[i]
            if a[i]<0:
                temp=0
            if a[i]>b[i]:
                temp=b[i]
            result.append(temp)
        return result

class Building:
    def __init__(self,id,human,human_rounds=1,btype="null",name="null",description="null",effect_id=[],effect_param=[],bounding_cards=[],bounding_num=[]):
        self.id=id
        self.human=human
        self.human_rounds=human_rounds
        self.type=btype
        self.name=name
        self.description=description
        self.effect_param=effect_param
        self.effect_id=effect_id
        self.bounding_cards=bounding_cards
        self.bounding_num=bounding_num

        


        

if __name__=="__main__":
    c=City()
    print(c.resource)