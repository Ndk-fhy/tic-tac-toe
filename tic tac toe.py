import random

def initgrille():
    grill = []
    for i in range(3):
        grill.append([])
        for j in range(3): 
            grill[i].append(" ")
            
    return grill

# print(initgrille())


def affiche(grille):
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            print(grille[i][j],end="")
        print()
d=[[ ' ',' ',' '], [ ' ', ' ',' '], [' ',' ',' ']]
# d=[[ '.','.','.'], [ '.','.','.'], [ '.','.','.']]
# print(d[0][0])
# print(affiche(d))


def victoire(grille,joeur):
    test=True
    for i in range(len(grille)):
        if (grille[i][0] == joeur and grille[i][1]==joeur and grille[i][2]== joeur):
            test= False
    
    for j in range(len(grille)):
        if ( grille[0][j] == joeur and grille[1][j]==joeur and grille[2][j]==joeur):
            test= False
    
    if (grille[0][0] == joeur and grille[1][1] == joeur and grille[2][2] == joeur):
        test = False
    if (grille[0][2] == joeur and grille[1][1] == joeur and grille[2][0] == joeur):
        test = False
            
    return test

# print(victoire([[0, 0 ,1], [ 0, 0, 0], [ 1, ' ', 1]],0))

def sep(num):
    uni=num%10
    dec=num//10
    return dec,uni

# print(sep(12))

def casevalide(grille,i,j):
    test=  False
    if(grille[i][j] !=" "):
        test=True
    return test
        
def jouercoupjoeur(grille,joueur):
    num=int(input("taper l'emplacement"))
    i,j=sep(num)
    valide=casevalide(grille,i,j)
    while valide:
        num=int(input("taper l'emplacement"))
        i,j=sep(num)
        valide=casevalide(grille,i,j)
        
    grille[i][j]=joueur
    return grille


def main():
    j1='x'
    j2='o'
    grille=initgrille()
    cond=True
    cpt=random.randrange(1,2)
    while cond:
        print(cpt)
        if (cpt % 2 != 0):
            grille=jouercoupjoeur(grille,j1)
            affiche(grille)
            cond=victoire(grille,j1)
            
        else :
            grille=jouercoupjoeur(grille,j2)
            affiche(grille)
            cond=victoire(grille,j2)
            
        cpt+=1
    if (cpt % 2 == 0):
        print("J1 gagne")
    else:
        print("J2 gagne")
    return None

print(main())

