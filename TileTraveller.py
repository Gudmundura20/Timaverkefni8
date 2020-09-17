# Við ætlum fyrst að gera 4 föll, 1 fyrir hverja átt
# Gerum fall sem gefur upp hvaða áttir eru í boði  #DONE
# Gerum svo annað fall fyrir meldingu þegar farið er í átt sem er ekki leyfð
# Gerum fall fyrir hreyfingu á milli gólfflísa (for loop)
# Gerum fall sem að gefur meldingu um að leikurinn hafi klárast (victory)
# Föllin eiga við hnitakerfi (x,y) svo þau taka x og y arguments
# grid = 3x, 3y
# lentum í github veseni í klukkutíma
x = 1
y = 1

# notandi gefur input fyrir áttirnar
def move_direction():
    n = input(" n ")
    s = input(" s ")
    e = input(" e ")
    v = input(" v ")


def move_direction(n, s, v, e):
    '''Hreyfing eftir input færir position x,y í nýjann ramma'''
    n = y + 1
    s = y - 1
    v = x - 1
    e = x + 1
    return y, x




#def tiles(): WIP
 #   n = move_y(n)
  #  s = move_y(s)
   # return y

    
    
    
def get_dir(n, s, a, v):   # ef sett er inn n, s, a, v fær notandi skilaboð
    ''' skilaboð til notanda um leifðar áttir'''
        beiðni = "Þú getur farið til: "
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
        if x == 3 and y == 1:
            beiðni += "Victory!"
        if x == 2 and y == 2:
            beiðni += "(W)est" or "(S)outh"
        if x == 2 and y == 1:
            beiðni += "(N)orth"
    print (beiðni + ".")  # breytan efst + leifðar áttir 
        



# íhuga func sem tekur input, biðja um dir og túlka það
# skiptir máli hvar þú ert staddur, hvaða áttir eru gildar