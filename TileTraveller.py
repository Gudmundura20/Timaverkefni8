# Við ætlum fyrst að gera 4 föll, 1 fyrir hverja átt
# Gerum fall sem gefur upp hvaða áttir eru í boði 
# Gerum svo annað fall fyrir meldingu þegar farið er í átt sem er ekki leyfð
# Gerum fall fyrir hreyfingu á milli gólfflísa (for loop)
# Gerum fall sem að gefur meldingu um að leikurinn hafi klárast (victory)
# Föllin eiga við hnitakerfi (x,y) svo þau taka x og y arguments

# grid = 3x, 3y
import math
def get_dir():
        (x):
            x = int(input("Give direction West or East: "))
    y = int(input("Give direction North or South: "))
    return x, y

def get_grid():
    x1, y1 = 1, 1
    x2, y2 = 2, 2
    x3, y3 = 3, 3
    return x, y
    
    
def mv_n():
    '''Fara norður um einn frá pos í framköllunar scope''' 
    x += 1
    print(directions) # frá nýja tile í pos x+1, y
    
def mv_s():
    '''Fara suður um einn frá pos í framköllunar scope'''
    y -= 1
    print(directions) # x, y-1


starting_pos_x = x1
starting_pos_y = y1
get_dir(x)
get_dir(y)

# if pos_xy = x1, y1:
   # print("You can travel N(orth).")

# íhuga func sem tekur input, biðja um dir og túlka það
# skiptir máli hvar þú ert staddur, hvaða áttir eru gildar