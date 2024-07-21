#!/usr/bin/env python
# coding: utf-8

# In[1]:


gm_list = [['','',''],
           ['','',''],
           ['','','']]


# In[2]:


from sys import exit


# In[3]:


def p1_user_input():

    p1_row_num =''
    p1_column_num=''
    in_range=range(0,3)
    range_check=False

    try:
        while range_check == False:
            print("Enter number 0 1 or 2")
            p1_row_num=int(input("Enter the row number "))
            p1_column_num=int(input("Enter the column number "))
            if p1_row_num in in_range and p1_column_num in in_range:
                range_check=True
    except ValueError:
        print("\t**Please enter a valid number input**")
        p1_user_input()
    else:
        if gm_list[p1_row_num][p1_column_num]=='':
            gm_list[p1_row_num][p1_column_num]='X'
            print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
            for row in gm_list]))
        else:
            print("This place already holds a symbol\n\t**RE-ENTER**")
            p1_user_input()
    
    game_X()
    game_O()


# In[4]:


def p2_user_input():
    
    p2_row_num =''
    p2_column_num=''
    in_range=range(0,3)
    range_check=False
    
    try:
        while range_check == False:
            print("Enter number 0 1 or 2")
            p2_row_num=int(input("Enter the row number "))
            p2_column_num=int(input("Enter the column number"))
            if p2_row_num in in_range and p2_column_num in in_range:
                range_check=True
        
    except ValueError:
        print("\t**Please enter a valid number input**")
        p2_user_input()
    else:
        if gm_list[p2_row_num][p2_column_num]=='':
            gm_list[p2_row_num][p2_column_num]='O'
            print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
            for row in gm_list]))
        else:
            print("This place already holds a symbol\n\t**RE-ENTER**")
            p2_user_input()
    
    game_X()
    game_O()


# In[5]:


def game_X():
    #digonal
    
    if (gm_list[0][0]=="X" and  gm_list[1][1]=="X" and gm_list[2][2]=="X") or (gm_list[0][2]=="X" and  gm_list[1][1]=="X" and gm_list[2][0]=="X"):
        print('\n!!! X is winner!!!')
        print("\n****RESTART****")
        exit()
     
        
    #horizontal
    
    elif (gm_list[0][0]=="X" and  gm_list[0][1]=="X" and gm_list[0][2]=="X") or (gm_list[1][0]=="X" and  gm_list[1][1]=="X" and gm_list[1][2]=="X") or (gm_list[2][0]=="X" and  gm_list[2][1]=="X" and gm_list[2][2]=="X"):
        print('\n!!!X is winner!!!')
        print("\n****RESTART****")
        exit()
       
        
    #vertical
    
    elif (gm_list[0][0]=="X" and  gm_list[1][0]=="X" and gm_list[2][0]=="X") or (gm_list[0][1]=="X" and  gm_list[1][1]=="X" and gm_list[2][1]=="X") or (gm_list[0][2]=="X" and  gm_list[1][2]=="X" and gm_list[2][2]=="X"):
        print('\n!!!X is winner!!!')
        print("\n****RESTART****")
        exit()
        
    else:
        pass
    


# In[6]:


def game_O():
    #digonal
    
    if (gm_list[0][0]=="O" and  gm_list[1][1]=="O" and gm_list[2][2]=="O") or (gm_list[0][2]=="O" and  gm_list[1][1]=="O" and gm_list[2][0]=="O"):
        print('\n!!!O is winner!!!')
        print("\n****RESTART****")
        exit()
        
        
    #horizontal    
    
    elif (gm_list[0][0]=="O" and  gm_list[0][1]=="O" and gm_list[0][2]=="O") or (gm_list[1][0]=="O" and  gm_list[1][1]=="O" and gm_list[1][2]=="O") or (gm_list[2][0]=="O" and  gm_list[2][1]=="O" and gm_list[2][2]=="O"):
        print('\n!!!O is winner!!!')
        print("\n****RESTART****")
        exit()
        
    #vertical    
    
    
    elif (gm_list[0][0]=="O" and  gm_list[1][0]=="O" and gm_list[2][0]=="O") or (gm_list[0][1]=="O" and  gm_list[1][1]=="O" and gm_list[2][1]=="O") or (gm_list[0][2]=="O" and  gm_list[1][2]=="O" and gm_list[2][2]=="O"):
        print('\n!!!O is winner!!!')
        print("\n****RESTART****")
        exit()
        
              
    else:
        pass


# In[7]:


gm_list = [['','',''],
           ['','',''],
           ['','','']]
from sys import exit
def tic_tac_toe():
    for i in range(0,10):
        print('\nFOR PLAYER 1-X')
        p1_user_input()
        print('\nFOR PLAYER 2-O')
        p2_user_input()
    game_X()
    


# In[8]:


gm_list


# tic_tac_toe()

# In[9]:


tic_tac_toe()


# # 
