# Við ætlum fyrst að gera upplýsingar til notanda hvert hann getur farið:
# Gerum fall sem gefur upp hvaða áttir eru í boði 
# Gerum svo annað fall fyrir meldingu þegar farið er í átt sem er ekki leyfð
# Notandi þarf að reyna að velja réttar leiðir til að komast á sigurflísina

# Gerum fall fyrir hreyfingu á milli gólfflísa (for loop)
# Föllin eiga við hnitakerfi (x,y) svo þau taka x og y arguments
# grid = 3x, 3y

# íhuga func sem tekur input, biðja um dir og túlka það
# skiptir máli hvar þú ert staddur, hvaða áttir eru gildar

# lentum í github veseni í klukkutíma sagðir okkur að setja þetta komment
# https://github.com/Gudmundura20/Timaverkefni8


def game_end():
    '''exit program with built in func exit()'''
    exit()

def get_dir(n, s, a, v):   # Ef sett er inn n, s, a, v
    '''skilaboð til notanda um leyfðar áttir'''
    beiðni= "You can travel: "
    if x == 1 and y == 1:
        beiðni += "(N)orth"
    if x == 1 and y == 2:
        beiðni += "(N)orth" or "(E)ast" or "(W)est"
    if x == 1 and y == 3:
        beiðni += "(E)ast" or "(W)est"
    if x == 2 and y == 3:
        beiðni += "(E)ast" or "(W)est"
    if x == 3 and y == 3:
        beiðni += "(W)est" or "(S)outh"
    if x == 3 and y == 2:
        beiðni += "(N)orth" or "(S)outh"
    if x == 2 and y == 2:
        beiðni += "(W)est" or "(S)outh"
    if x == 2 and y == 1:
        beiðni += "(N)orth"
    elif x == 3 and y == 1:
        beiðni = "Victory!"
        game_end() # exits program
    print (beiðni + ".")  # breytan efst + leyfðar áttir á ensku skv mimir output
    
# notandi gefur input fyrir áttirnar
def move_direction_input(n, s, a, v):
    n = input("n ")
    s = input("s ")
    a = input("e ")
    v = input("v ")
    return direction_func(n, s, a, v)
    
def direction_func(n, s, a, v):
    '''Hreyfing eftir input færir position x,y í nýjann ramma'''
    n = y +1
    
    s = y -1

    a = x +1

    v = x -1
    return x, y
      
x = 1
y = 1
n = 1
s = 1
a = 1
v = 1

while x != 3 and y != 1:
    get_dir(n, s, a, v) # Hvaða áttir eru í boði
    move_direction_input(n, s, a, v) # notandi velur átt
    direction_func(n, s, a, v) # notandi færist













    
    
    

        


