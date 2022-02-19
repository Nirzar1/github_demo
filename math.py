# add implementation
def add(x,y):
    return x+y  # onBug123
    
# subtract implementation
def subtract(x,y):
    return x-y  # on Master 
    
# multiply implementation
def multiply(x,y):
    return x*y  # on Bug456
    
# divide implementation
def divide(x,y):
    if y == 0 :     #on Bug789
        return DIVIDE BY_0_ERROR
    else :
        return x/y  
