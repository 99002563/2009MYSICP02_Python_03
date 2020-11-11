import random
import time
from IPython.display import clear_output

color = ('RED','GREEN','BLUE','YELLOW')
rank = ('0','1','2','3','4','5','6','7','8','9','Skip','Reverse','Draw2','Draw4','Wild')
ctype = {'0':'number','1':'number','2':'number','3':'number','4':'number','5':'number','6':'number',
            '7':'number','8':'number','9':'number','Skip':'action','Reverse':'action','Draw2':'action',
            'Draw4':'action_nocolor','Wild':'action_nocolor'}

class Card:
    
    def __init__(self,color,rank):
        self.rank = rank
        if ctype[rank]=='number':
            self.color = color
            self.cardtype = 'number'
        elif ctype[rank]=='action':
            self.color = color
            self.cardtype = 'action'
        else:
            self.color = None
            self.cardtype = 'action_nocolor'
            
            
    def __str__(self):
        if self.color == None:
            return self.rank
        else:
            return self.color+" "+self.rank

 #Funciton to randomly select who starts first
def choose_first():
    if random.randint(0,1)==0:
        return 'Player'
    else:
        return 'Pc'
   
#Function to check if the card thrown by Player/PC is a valid card by comparing it with the top card
def single_card_check(top_card,card):
    if card.color==top_card.color or top_card.rank==card.rank or card.cardtype=='action_nocolor':
        return True
    else:
        return False
            
