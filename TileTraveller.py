# Við ætlum fyrst að gera upplýsingar til notanda hvert hann getur farið:
#   Gerum fall sem gefur upp hvaða áttir eru í boði 
#   Gerum svo annað fall fyrir meldingu þegar farið er í átt sem er ekki leyfð
#   Notandi þarf að reyna að velja réttar leiðir til að komast á sigurflísina

# Gerum fall fyrir hreyfingu á milli gólfflísa: 
# Föllin eiga við hnitakerfi (x,y) svo þau taka x og y arguments
# grid = 3x, 3y

# íhuga func sem tekur input, biðja um dir og túlka það
# func sem túlkar gildar áttir frá staðsetningu :WIP

# lentum í github veseni, sagðir okkur að setja þetta komment
# https://github.com/Gudmundura20/Timaverkefni8


def game_end():
    '''exit program with built in func exit()'''
    return exit()

# fastar a, v = austur, vestur
def get_directions(n, s, a, v):   # Ef sett er inn n, s, a, v
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
    
def direction_direct(n, s, a, v):
    '''Notandi stýrir í átt'''
    direction = input("Direction: ")
    return direction
    
def direction_direct_func(direction, x, y):
    '''Hreyfing eftir input færir position x,y í nýja flís'''
    for direction in direction_direct(n, s, a, v): # iterates the input from direction_direct() for these statements
        if direction == 'n':  
            y += 1
        elif direction == 's':
            y -= 1
        
        elif direction == 'a':
            x += 1
        elif direction == 'v':
            x -= 1
        if direction.isupper() == True:
            direction.islower() == direction.isupper()
            
    return (x, y)

# Start of program  
x = 1
y = 1
n = 'n'
s = 's'
a = 'a'
v = 'v'

while x != 3 and y != 1:
    get_directions(n, s, a, v) # Hvaða áttir eru í boði
    direction_direct(n, s, a, v) # notandi velur átt
    direction_direct_func(direction, x, y)
