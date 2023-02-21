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
            assert type(args[1]) == int, '!!Un  ABR est composé uniquement de nombres entiers !!'  #gestion du type, on travaille ici avec des nombres entiers uniquement
        result = fonction(*args)  #la fonction prendra les arguments qu'on lui mets, pas d'importance
        return result
    return decorateur

    ## FONCTIONS PRINCIPALES

def estABR(A:BinTree) -> bool:
    """
    Entrée, A : objet BinTree
    Sortie : Booléen
    Renvoie True si A  est un arbre binaire de recherche False sinon
    """
    #assertion
    assert type(A) is BinTree, "!! A doit être un arbre binaire !!"

    #Programme
    # Il y a 5 possibilités à un arbre : vide, feuille, 1 SAG, 1 SAG, 1 SAG et 1 SAD
    if A.estVide() or A.estFeuille():# 2 premier cas :Arbre vide ou feuille -> feuille arbre de longueur 1, qui n'a qu'un noeud
        return True #un arbre vide ou une feuille est un arbre binaire de recherche on renvoie True
    if A.gauche().estVide() and not A.droit().estVide(): #3eme cas : Pas de SAG mais un SAD
        return A.droit().racine() > A.racine() and estABR(A.droit())  #comparaison de l'ABR et appel récursif à partir du SAD uniquement
    if A.droit().estVide() and not A.gauche().estVide(): #4eme cas : Pas de SAD mais un SAG
        return A.gauche().racine() <= A.racine() and estABR(A.gauche()) #comparaison de l'ABR et appel récursif à partir du SAG uniquement
    else: #5 cas possible : Présence d'un SAG et d'un SAD
        return (A.gauche().racine() <= A.racine() and A.droit().racine() > A.racine()) and (estABR(A.gauche()) and estABR(A.droit()))
        #comparaisons de l'ABR et appels récursifs des SAG et SAD

@testABR
def rechercheCle(A:BinTree, n :int) -> bool:
    """
    Entrée :
            A : Objet Bintree
            n : entier
    Sortie : Booléen
    Renvoie True si la clé n est dans l'arbre A, False sinon
    """
    #assertion
    assert type(n) is int , 'n doit être un entier !'
    #programme
    if A.estVide():
        return False #Si ojn tombe sur un arbre vide -> les arbres se sont echainés et à aucun moment la valeur d'une racine n'à été égale à la valeur cherchée, cette dernière n'est donc pas dans l'arbre
    if A.racine() == n: #Si la racine est le nombre cherché -> renvoie True, la valeur est bien dans l'arbre
        return True
    else:  #Dans les autres cas il faut parcourir récursivement l'arbre -> 2 cas possibles dans un ABR
        if n <= A.racine():  #1er cas, la valeur de n est inférieure ou égale à la racine -> elle se trouve donc dans le SAG
            return rechercheCle(A.gauche(), n) # Résolution à partir du SAG
        else: #dans tout les autres la valeur de n est strictement supérieure à celle de racine -> elle se trouve donc dans le SAD
            return rechercheCle(A.droit(), n) #Résolution à partir de SAD


@testABR
def insereCle(A:BinTree, n:int) -> BinTree:
    """
    Entrées :
            A : Objet Bintree
            n : entier
    Sortie : Objet BinTree
    Renvoie un BinTree avec
    """

    if A.estVide(): #Si l'arbre est vide, on peut ajouter une clé sans contraintes
        return BinTree(n)
    if n <= A.racine(): #D'après la définition de l'ABR, si la valeur est <= à la racine, alors elle est dans la partie gauche de l'arbre
        return BinTree(A.racine(), insereCle(A.gauche(), n), A.droit())
    else: #dans tous les autres cas, elle est dans la partie droite de l'arbre
        return BinTree(A.racine(), A.gauche(), insereCle(A.droit(), n))




def creerABR(intList:list) -> BinTree:
    """
    Entrée : intList : list d'entier
    Sortie : Bintree
    Renvoie un ABR à partir de la liste d'entiers passée en args
    """
    arbre = BinTree() #création d'un arbre vide dans lequel on insérera chaque valeur de intList
    while len(intList) != 0: #tant que la liste n'est pas vide
        temp = intList.pop() # initialisation d'une variable temporaire qui contient la valeur à insérer dans l'arbre
        arbre = insereCle(arbre, temp)
    return arbre

@testABR
def sommeCle(A:BinTree) -> int:
    """
    Entrée : A -> BinTree
    Sortie : int
    Renvoie la somme des clés de l'ABR donné en args
    """
    if A.estVide():
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
#creerABR(notIntList)
    #Fin des tests
print("---------------------------")

    # Tests d'un BinTree quelconque
print("Arbre Binaire : ", "\n", " ")
print(arbreBinaire)
print(f"estABR(arbreBinaire) -> {estABR(arbreBinaire)}") #Renvoie False
    #Fin des tests
