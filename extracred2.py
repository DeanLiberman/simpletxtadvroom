##Simple skeleton code to simulate moving between "rooms" freely.
## It seems I can "move" between rooms/functions easily enough, but getting something to come from each
## room seems tricky.

## In other words, say I want a secret room to appear after pressing five buttons, one in each room
## At the moment I am having difficulty doing/understanding that





def centerroom():
    print "You are in the center room. You can go up to the upper room."
    print "Down to the lower room."
    print "Left to the left room."
    print "Or right to the right room."
    
    choice = raw_input(">_")
    
    if choice == "left" or "LEFT" or "Left":
        leftroom()
    if choice == "right" or "RIGHT" or "Right":
        rightroom()
    if choice == "up" or "UP" or "Up":
        upperroom()
    if choice == "down" or "DOWN" or "Down":
        lowerroom()
    
        
    else:
        centerroom()
    
def lowerroom():
    print "You are in the lower room."
    print "There seems to be nothing of note here."
    print "You can go back up to the center room."
    
    choice = raw_input(">_")
    
    if choice == "up" or "UP" or "Up":
        centerroom()
    else:
        lowerroom()
        
        
def upperroom():
    print "You are in the upper room."
    print "You can go back down to the center room."
    
    choice = raw_input(">_>")
    
    if choice == "down" or "DOWN" or "Down":
        centerroom()
    else:
        upperroom()
        
def rightroom():
    print "You are in the right room."
    print "You can go back left to the center room."
    
    choice = raw_input(">_>")
    
    if choice == "left" or "Left" or "LEFT":
        counter+1
        centerroom()
    else:
        rightroom()
        
def leftroom():
    print "You are in the left room."
    print "You can go back right to the center room."
    
    choice = raw_input(">_<")
    
    if choice == "right" or "Right" or "RIGHT":
        centerroom()
    else:
        leftroom()
    
centerroom()

    
    
