## Projet : Arbre Binaire de Recherche
""" Groupe 2 : Alban, Lucas, Tuan """
##IMPORT
from BinTree import BinTree

## FONCTIONS

    ## DECORATEURS

def testABR(fonction):  #généraliser les assertions sur l'ABR
    def decorateur(*args): #création d'un décorateur pour faire toutes les assertions liées aux ABR
        assert estABR(args[0]), "!! A doit être un arbre binaire de recherche !!" #args[0] sera toujours l'arbre dans lequel on évolue
        if len(args) > 1:
            assert type(args[1]) == int, '!! Un  ABR est composé uniquement de nombres entiers !!'  #gestion du type, on travaille ici avec des nombres entiers uniquement
        result = fonction(*args)  #la fonction prendra les arguments qu'on lui mets, pas d'importance
        return result
    return decorateur

    ## FONCTIONS PRINCIPALES
def estABR(A:BinTree) -> bool:
    """ Renvoie True si A  est un arbre binaire de recherche, False sinon """
    #assertion
    assert type(A) is BinTree, "!! A doit être un arbre binaire !!"
    #Programme
    if A.estVide() or A.estFeuille(): #Un arbre vide est un abr par définition
        return True
    if not A.gauche().estVide() and A.gauche().maximum() > A.racine(): #Si une clé de l'ABR gauche est supérieur à la racine, ce n'est pas un abr
            return False
    if not A.droit().estVide() and A.droit().maximum() <= A.racine():
            return False
    return estABR(A.gauche()) and estABR(A.droit()) #on résoud à partir des abr droits et gauches 

@testABR
def rechercheCle(A:BinTree, n :int) -> bool:
    """ Renvoie True si la clé n est dans l'arbre A, False sinon """
    if A.estVide():
        return False #le cas élémentaire est un arbre vide. Si on tombe sur une vide, ça veut dire qu'on a fait toutes les clés possibles sans tomber sur celle recherchée
    if A.racine() == n: #Si la racine est le nombre cherché -> renvoie True, la valeur est bien dans l'arbre
        return True
    else:  #Dans les autres cas il faut parcourir récursivement l'arbre -> 2 cas possibles dans un ABR
        if n <= A.racine():  #1er cas, la valeur de n est inférieure ou égale à la racine -> elle se trouve donc dans le SAG
            return rechercheCle(A.gauche(), n) # Résolution à partir du SAG
        else: #dans tout les autres la valeur de n est strictement supérieure à celle de racine -> elle se trouve donc dans le SAD
            return rechercheCle(A.droit(), n) #Résolution à partir de SAD

@testABR
def insereCle(A:BinTree, n:int) -> BinTree:
    """ Renvoie un BinTree avec la clé insérée au bon endroit """
    if A.estVide(): #Si l'arbre est vide, on peut ajouter une clé sans contraintes
        return BinTree(n)
    if n <= A.racine(): #D'après la définition de l'ABR, si la valeur est <= à la racine, alors elle est dans la partie gauche de l'arbre
        return BinTree(A.racine(), insereCle(A.gauche(), n), A.droit())
    else: #dans tous les autres cas, elle est dans la partie droite de l'arbre
        return BinTree(A.racine(), A.gauche(), insereCle(A.droit(), n))

def creerABR(intList:list) -> BinTree:
    """ Renvoie un ABR à partir de la liste d'entiers passée en args """
    arbre = BinTree() #création d'un arbre vide dans lequel on insérera chaque valeur de intList
    while len(intList) != 0: #tant que la liste n'est pas vide
        temp = intList.pop() # initialisation d'une variable temporaire qui contient la valeur à insérer dans l'arbre
        arbre = insereCle(arbre, temp)
    return arbre

@testABR
def sommeCle(A:BinTree) -> int:
    """ Renvoie la somme des clés de l'ABR donné en args """
    if A.estVide(): #la somme des clés vaut 0 si il n'y a pas de clés
        return 0
    else:
        return A.racine() + sommeCle(A.gauche()) + sommeCle(A.droit())

## PROGRAMME PRINCIPAL

arbreBinaireRecherche = BinTree(30, BinTree(25, BinTree(18, BinTree(9)), BinTree(29, BinTree(26, BinTree(), BinTree(28)))), BinTree(41, BinTree(), BinTree(52, BinTree(48), BinTree(60))) ) #Arbre binaire de recherche
arbreBinaire = BinTree(30, BinTree(25, BinTree(18, BinTree(24)), BinTree(22, BinTree(26, BinTree(), BinTree(28)))), BinTree(41, BinTree(), BinTree(52, BinTree(48), BinTree(60)))) #Arbre binaire

## TESTS

    # Tests de l'ABR
print("Arbre Binaire de Recherche : ", "\n", " ")
print(arbreBinaireRecherche)
print(f"estABR(arbreBinaireRecherche) -> {estABR(arbreBinaireRecherche)}") # Renvoie True
print(f"rechercheCle(arbreBinaireRecherche, 28) -> {rechercheCle(arbreBinaireRecherche, 28)}") #Renvoie True
print(f"rechercheCle(arbreBinaireRecherche, 99) -> {rechercheCle(arbreBinaireRecherche, 99)}") #Renvoie True
arbreBinaireRechercheModif = insereCle(arbreBinaireRecherche, 22)
print(arbreBinaireRechercheModif) #Affiche L'ABR avec la modification
print(f"La somme des clés de arbreBinaireRechreche vaut {sommeCle(arbreBinaireRecherche)}")
print(f"La somme des clés de arbreBinaireRechrecheModif vaut {sommeCle(arbreBinaireRechercheModif)}")

    #Fin des tests
print("---------------------------")
    #Tests de création d'un ABR
intList = [11, 2, 7, 37, 27, 4, 5, 12]
notIntList = ["str", 4.67, 2, 8, 9, 0]
newArbre = creerABR(intList)
print(newArbre)
print(f"estABR(newArbre) -> {estABR(newArbre)}") # Renvoie True

    #Fin des tests
print("---------------------------")

    # Tests d'un BinTree quelconque
print("Arbre Binaire : ", "\n", " ")
print(arbreBinaire)
print(f"estABR(arbreBinaire) -> {estABR(arbreBinaire)}") #Renvoie False
    #Fin des tests
"""
    #Tests d'assertions
creerABR(notIntList)
insereCle(arbreBinaire)

"""
