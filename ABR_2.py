## Projet : Arbre Binaire de Recherche
##IMPORT
from BinTree import BinTree

## FONCTIONS

def estABR(A:BinTree) -> bool:
    """
    Entrée, A : Objet BinTree
    Sortie : Booléen
    Renvoie True si A  est un arbre binaire de recherche False sinon
    """
    #assertion
    assert type(A) is BinTree, "A doit être un arbre binaire"

    #Programme
    # Il y a 5 possibilités à un arbre : vide, feuille, 1 SAG, 1 SAG, 1 SAG et 1 SAD
    if A.estVide() or A.estFeuille():# 2 premier cas :Arbre vide ou feuille -> feuille arbre de longueur 1, qui n'a qu'un noeud
        return True #un arbre vide ou une feuille est un arbre binaire de recherche on renvoie True
    if A.gauche().estVide() and not A.droit().estVide(): #3eme cas : Pas de SAG mais un SAD
        return A.droit().racine() > A.racine() and estABR2(A.droit())  #comparaison de l'ABR et appel récursif à partir du SAD uniquement
    if A.droit().estVide() and not A.gauche().estVide(): #4eme cas : Pas de SAD mais un SAG
        return A.gauche().racine() <= A.racine() and estABR2(A.gauche()) #comparaison de l'ABR et appel récursif à partir du SAG uniquement
    else: #5 cas possible : Présence d'un SAG et d'un SAD
        return (A.gauche().racine() <= A.racine() and A.droit().racine() > A.racine()) and (estABR2(A.gauche()) and estABR2(A.droit()))
        #comparaisons de l'ABR et appels récursifs des SAG et SAD

def rechercheCle(A:BinTree, n :int) -> bool:
    """
    Entrée :
            A : Objet Bintree
            n : entier
    Sortie : Booléen
    Renvoie True si la clé n est dans l'arbre A, False sinon
    """
    #assertions
    assert type(n) is int , 'n doit être un entier !'
    assert estABR(A), "A doit être un arbre binaire de recherche"

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

## PROGRAMME PRINCIPAL
arbreBinaire = BinTree(30, BinTree(25, BinTree(18, BinTree(9)), BinTree(29, BinTree(26, BinTree(), BinTree(28)))), BinTree(41, BinTree(), BinTree(52, BinTree(48), BinTree(60))) )

## TESTS
print(arbreBinaire)
print(estABR(arbreBinaire))
