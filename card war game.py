#!/usr/bin/env python
# coding: utf-8

# In[16]:


import random 

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace')

values = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 
            'nine':9, 'ten':10, 'jack':11, 'queen':12, 'king':13, 'ace':14}


# In[17]:


class Cards():
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
        
    def __str__(self):
        return self.rank +' of ' + self.suit


# In[18]:


class Deck():
    
    def __init__(self):
        
        self.all_cards =[]
        
        #create a deck of 52 cards
        for suit in suits:
            for rank in ranks:
                created_card = Cards(suit,rank)
                self.all_cards.append(created_card)
    
    #shuffle the cards list
    def shuffle(self):
        random.shuffle(self.all_cards)     
    
    #grab one of the card from list
    def grab_card(self):
        return self.all_cards.pop()


# In[19]:


class Player():
    
    def __init__(self,name):
        self.name = name
        self.all_cards =[]
        
    def remove(self):
        return self.all_cards.pop(0)
    
    def add(self,new_card):
        if type(new_card)==type([]):
            self.all_cards.extend(new_card)
        else:
            self.all_cards.append(new_card)
            
    def __str__(self):
        return f" {self.name} has total {len(self.all_cards)} cards ."
    


# In[20]:


# split cards between two players

player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add(new_deck.grab_card())
    player_two.add(new_deck.grab_card())


# In[21]:


game_on = True


# In[23]:


round_no = 0
while game_on == True :
        
        round_no +=1
        print(f'\n**ROUND:{round_no}**')
        
        
        if len(player_one.all_cards)==0:
            print("\n Player one is out of cards !! \n \t**PLAYER TWO WINS!!**")
            game_on = False
            break
        if len(player_two.all_cards)==0:
            print("\n Player two is out of cards !! \n \t**PLAYER ONE WINS!!**")
            game_on = False
            break
        
        player_one_cards= [] #current cards
        player_one_cards.append(player_one.remove())
        
        
        player_two_cards= [] #current cards
        player_two_cards.append(player_two.remove())
        
        at_war = True
        
        while at_war:
            
            print(f"Player_1 : {player_one_cards[-1]}")
            print(f"Player_2 : {player_two_cards[-1]}")
            #if player one wins round
            if player_one_cards[-1].value > player_two_cards[-1].value:
                print("player one wins the round")
                player_one.add(player_one_cards)
                player_one.add(player_two_cards)
                
                at_war = False
            
            #if player two wins round
            elif player_one_cards[-1].value < player_two_cards[-1].value:
                print("player two wins the round")
                player_two.add(player_one_cards)
                player_two.add(player_two_cards)
                
                at_war = False
                
            #war situation 
            else:
                print("\n\t**WAR!**\n")
                if len(player_one.all_cards) < 10:
                    print("Player one do not have sufficient cards")
                    print("\t**PLAYER TWO WINS**")
                    game_on = False
                    break
                    
                elif len(player_two.all_cards) < 10:
                    print("Player two do not have sufficient cards")
                    print("\t**PLAYER ONE WINS**")
                    game_on = False
                    break
                    
                else:
                    for i in range(10):
                        player_one_cards.append(player_one.remove())
                        player_two_cards.append(player_two.remove())                        


# In[ ]:




