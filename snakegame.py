from PIL import Image
import random
end=100
def show_board():
    img=Image.open('sanke_Ladder.jpg')
    img.show()

def check_ladder(points):
    if(points==1):
        print('ladder')
        return 38
    elif(points==4):
        print('ladder')
        return 14    
    elif(points==9):
        print('ladder')
        return 31
    elif(points==21):
        print('ladder')
        return 42
    elif(points==28):
        print('ladder')
        return 84
    elif(points==51):
        print('ladder')
        return 67
    elif(points==71):
        print('ladder')
        return 91
    elif(points==80):
        print('ladder')
        return 100 
    else:
        #not a ladder
        return points

def check_snake(points):
    if (points==17):
        print('Snake')
        return 7
    elif(points==54):
        print('snake')
        return 34    
    elif(points==62):
        print('snake')
        return 19
    elif(points==64):
        print('snake')
        return 60      
    elif(points==87):
        print('snake')
        return 24
    elif(points==93):
        print('snake')
        return 73 
    elif(points==95):
        print('snake')
        return 75
    elif(points==98):
        print('snake')
        return 79
    else:
        #not a snake
        return points      

def reached_end(points):
    if points==end:
        return True
    else:
        return False    

def play():
    p1_name=input('player 1, pls your name:')
    p2_name=input('player 2, pls your name:')
    #Initial point of Player
    pp1=0
    pp2=0
    turn=0
    while(1):
        if(turn%2==0):
            #player 1 Turn
            print(p1_name,"Your turn")
            #ask player's Choice to continue
            c=int(input('press 1 to continue, 0 to quit:'))
            if(c==0):
                print(p1_name,'scored',pp1)
                print(p2_name,'scored',pp2)
                print('Quiting the game, Thanks for playing')
                break
            else:
                dice=random.randint(1,6)
                print('Dice showed:',dice)
                #add the point
                pp1=pp1+dice
                pp1=check_ladder(pp1)
                pp1=check_snake(pp1)
                print(p1_name,"your score:",pp1)
                #check if the player goes the beyond the board
                if(pp1>end):
                    pp1=end
                    print(p1_name,"your score:",pp1)
                
                if(reached_end(pp1)):
                    print(p1_name,'won')
                    break

        else:           
            #player 2 Turn
            print(p2_name,"Your turn")
            #ask player's Choice to continue
            c=int(input('press 1 to continue, 0 to quit:'))
            if(c==0):
                print(p1_name,'scored',pp1)
                print(p2_name,'scored',pp2)
                print('Quiting the game, Thanks for playing')
                break
            else:
                dice=random.randint(1,6)
                print('Dice showed:',dice)
                #add the point
                pp2=pp2+dice
                pp2=check_ladder(pp2)
                pp2=check_snake(pp2)
                print(p2_name,"your score:",pp2)
                #check if the player goes the beyond the board
                if(pp2>end):
                    pp2=end
                    print(p2_name,"your score:",pp2)
                
                if(reached_end(pp2)):
                    print(p2_name,'won')
                    break        
        turn=turn+1


show_board()
play()
