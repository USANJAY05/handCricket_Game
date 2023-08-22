import random
print("Play with Sadi")
name=input("Enter your name: ")
machineName="Sadi:"
machineName1="Sadi"
RandomNo=random.randint(1,6)
oddOrEven=input("Odd OR Even:")
number=int(input("Enter a no between 1 to 6:"))

def humanTurn():
            humanPoints=0
            machinePoints=0
            print("your turn")
            #If choose batting then return batting
            while(True):
                
                humanNo=int(input(name+": "))
                if(humanNo>=1 and humanNo<=6):
                    machineNo=random.randint(1,6)
                    print(f"{machineName} {machineNo}")
                    if(machineNo!=humanNo):
                        humanPoints+=humanNo
                    else:
                        print("out")
                        print(f"{name}'s Score:{humanPoints}")
                        print(f"{machineName1}'s Target:{humanPoints+1}")
                        break
                else:
                     print("Enter 1 to 6")    
            print(f"{machineName1}'s turn")    
            while(humanPoints>=machinePoints):
                
                humanNo=int(input(name+": "))
                if(humanNo>=1 and humanNo<=6):
                    machineNo=random.randint(1,6)
                    print(f"{machineName} {machineNo}")
                    if(machineNo!=humanNo):
                        machinePoints+=machineNo
                        if(machinePoints<humanPoints):
                            print(f"{machineName1} need {humanPoints-machinePoints+1} to win")

                    else:
                        print(f"{machineName1} out")
                        break
                else:
                     print("Enter 1 to 6")    

            if(humanPoints>machinePoints):
                     print(f"You won With {humanPoints} points")   
            elif(humanPoints==machinePoints):
                 print("Match Drawn")         
            else:
                     print(f"You lose with {humanPoints} points")
                     print(f"{machineName1} Wins")      

def machinTurn():
            humanPoints=0
            machinePoints=0
            print(f"{machineName1}'s turn")
            while(True):
                
                humanNo=int(input(name+": "))
                if(humanNo>=1 and humanNo<=6):
                    machineNo=random.randint(1,6)
                    print(f"{machineName} {machineNo}")
                    if(machineNo!=humanNo):
                        machinePoints+=machineNo
                    else:
                        print(f"{machineName1} out")
                        print(f"{machineName1}'s Score:{machinePoints}")
                        print(f"{name}'s Target:{machinePoints+1}")
                        break
                else:
                     print("Enter 1 to 6")    
            print("your turn")    
            while(machinePoints>=humanPoints):
                humanNo=int(input(name+": "))
                if(humanNo<=6 and humanNo>=1):
                    machineNo=random.randint(1,6)
                    print(f"{machineName} {machineNo}")
                
                    if(machineNo!=humanNo):
                        humanPoints+=humanNo
                        if(machinePoints>humanPoints):                        
                            print(f"{name} need {machinePoints-humanPoints+1} to win")

                    else:
                        print("out")
                        break  
                else:
                    print("Enter 1 to 6")                       
            if(humanPoints>machinePoints):
                     print(f"You won with {humanPoints} points")   
            elif(humanPoints==machinePoints):
                 print("Match Drawn")         
            else:
                     print(f"You lose with {humanPoints} points")
                     print(f"{machineName1} wins.")    

if(number>=1 and number<=6):
#If odd then if condition will run
    if(oddOrEven=="odd"):
    #Check odd or even
        if((number+RandomNo)%2!=0):
            n=input("batting or bowling :")
            if(n=="batting"):
                humanTurn()
            else:
                machinTurn()
        else:
            if(random.randint(0,2)==1):        
                machinTurn()
            else:
                humanTurn()
    elif(oddOrEven=="even"):
        if((number+RandomNo)%2==0):
            n=input("batting or bowling :")
            if(n=="batting"):
                humanTurn()
            else:
                machinTurn()
        else:
            if(random.randint(0,2)==1):        
                machinTurn()
            else:
                humanTurn()
else:
     print("Enter Number between 1 to 6")                
