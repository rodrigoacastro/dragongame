
# coding: utf-8

# In[ ]:

# Jogo de matar o dragão

# Tutorial de orientacao a objetos: 
# https://docs.python.org/3/tutorial/classes.html

"""
Regras:

O dragão inicia com 3 cabeças e 3 caudas.

1) Se cortar 1 cabeca, nasce 1 (outra).
2) Se cortar 2 cabecas, nao nasce nem cabeca nem cauda.
3) Se cortar 1 cauda, nascem 2 caudas no lugar.
4) Se cortar duas caudas, nasce 1 cabeca.

5) Se sobrar apenas a cabeca, o jogador perde.

"""

"""
Rules:

The dragon begins with 3 heads and 3 tails.

1) If you cut 1 head, one grows (back).
2) If you cut 2 heads, no head or tail grows back.
3) If you cut 1 tail, 2 tails grow back.
4) If you cut 2 tails, 1 head grows back.

5) If only 1 head remains, the player loses and is devoured by the dragon.

"""


# In[1]:

# Jogo de matar o dragão

# Tutorial de orientacao a objetos: 
# https://docs.python.org/3/tutorial/classes.html

def show_rules(): 
    file = open("Rules.txt","r")
    for item in file:
        print(item)
    
def mostrar_regras(): 
    file = open("Regras.txt","r")
    for item in file:
        print(item)
    
#show_rules()
#mostrar_regras()


# In[2]:

# Creates class dragon (3 heads and 3 tails), with methods cut_head and cut_tail        


# In[3]:

class Dragon:
    
    def __init__(self, heads, tails):
        self.heads = heads
        self.tails = tails      
       
    def cut_head (self):      
    #def cut_head (self,heads):
        if self.heads >= 1:
            self.heads -= 1
        else:
            print("Impossible to cut an ethereal head, try something else.")
        #return(heads)

    def cut_tail (self): 
    #def cut_tail (self,tails):
        if self.tails >= 1:
            self.tails -= 1
        else:
            print("Impossible to cut an ethereal tail, try something else.")
        #return(tails)
   
    def grow_head (self): 
    #def grow_head (self,heads):
        self.heads += 1
        #return(heads)

    def grow_tail (self):
    #def grow_tail (self,tails):
        self.tails += 1
        #return(tails)
    
    def cut1head (self):
        # nothing happens, the head regrows
        #self.heads = heads
        #self.tails = tails
        self.cut_head()
        self.grow_head()
        print("1 head was cut, but another grew in its place")
        
    def cut2heads (self):
        # nothing bad happens, no head or tail regrows
        for i in range(2):
            self.cut_head()
        print("2 heads were cut, and nothing bad happened. What a relief!")
            
    def cut1tail (self):
        self.cut_tail()
        # 2 tails grow back
        for i in range(2):
            self.grow_tail()
        print("1 tail was cut, but 2 tails grew in its place")
    
    def cut2tails (self):
        for i in range(2):
            self.cut_tail()
            # 1 extra head grows
        self.grow_head()
        print("2 tails were cut, but it caused an extra head to grow as well")


# In[4]:

# check data on the dragon (number of heads and tails)

def check_dragon(dragon):
        print("\nThe dragon has %i heads." %dragon.heads)
        print("The dragon has %i tails.\n" %dragon.tails)


# In[5]:

# check if number of heads is 1 (if so, it is game over)

def check_game_over(dragon):
    if dragon.heads > 1:
        print("Lucky, you are STILL alive, but not for long...")
    if dragon.heads is 1 and dragon.tails is 0:
        print("Too bad. You never the last head of the dragon devouring you after burning you whole. Try again!")
    else: # if the dragon is dead
        print("Congratulations, you have just killed the dragon! Now you can celebrate all night with your village!")


# In[6]:

# creating instance


# In[7]:

drag = Dragon(heads=3,tails=3)

print("Welcome to Dragongame")
check_dragon(drag)
print("Your objective is to kill the evil dragon, before he kills you and your whole village, Riverville")
print("\n")

show_rules()

print("To (try to) kill the evil dragon you can: \n1) cut 1 head; \n2) cut 2 heads; \n3) cut 1 tail; \n4) cut 2 tails.")
print("\nWhat will you do?")


# In[8]:

# testing cutting heads

#drag.cut_head()

#check_dragon(drag)
#drag.cut1head()

#check_dragon(drag)
#drag.cut2heads()

#check_dragon(drag)


# In[9]:

# test cutting tails

#check_dragon(drag)

#drag.cut1tail()

#check_dragon(drag)

#drag.cut2tails()

#check_dragon(drag)


# In[10]:

# check game over
# check_game_over(drag)


# In[11]:

# Game creation


# In[12]:

# Message to the player

print("To (try to) kill the evil dragon you can: \n1) cut 1 head; \n2) cut 2 heads; \n3) cut 1 tail; \n4) cut 2 tails.")
print("\nWhat will you do?")


# In[13]:

action = input("What will you do? Type 1 to 4 to select an option")

check_dragon(drag)

if action == 1:
    drag.cut1head()
elif action == 2:
    drag.cut2heads()
elif action == 3:
    drag.cut1tail()
elif action == 4:
    drag.cut2tails()
else:
    print("Choose an option:")
    
check_dragon(drag)


# In[14]:

drag.cut1head()
drag.cut2heads()
drag.cut2tails()
drag.cut1tail()
drag.cut2tails()


# In[ ]:

#drag.cut2heads()
drag.grow_tail()
check_dragon(drag)


# In[15]:

check_dragon(drag)
check_game_over(drag)
#drag.revive()


# In[ ]:

# TESTING new dragon
drag2 = Dragon(heads=7,tails=2)
check_dragon(drag2)


# In[ ]:

drag2.cut1head()
check_game_over(drag2)
drag.cut2heads()
check_game_over(drag2)
drag.cut2tails()
check_game_over(drag2)
drag.cut1tail()
check_game_over(drag2)
drag.cut2tails()
check_game_over(drag2)


# In[18]:

print(drag.heads)


# In[ ]:



