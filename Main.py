#Emergence Project V1.0
#Date Created 29th December 2013
#No Idea what we are doing

#Create general program loop
Gameover = False;

while not Gameover:
    Player_Input = input("Press 'e' to exit"); #Gather user Input
    
    #Begin processing user input
    if Player_Input == 'e':
        Gameover = True;
