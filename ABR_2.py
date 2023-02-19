## Projet : Arbre Binaire de Recherche
from BinTree import BinTree

## FONCTIONS
def estABR(A:BinTree) -> bool:
    """
    Entrée, A : objet BinTree
    Sortie : Booléen
    Renvoie True si A  est un arbre binaire de recherche False sinon
    """
    if A.estVide():
        return True
    if not A.gauche().estVide():
        return A.gauche().racine() <= A.racine() and estABR(A.gauche())
    if not A.droit().estVide():
        return A.droit().racine() > A.racine() and estABR(A.droit())
    else:
        return estABR(A.gauche()) and estABR(A.droit())

## PROGRAMME PRINCIPAL
arbreBinaire = BinTree(30, BinTree(25, BinTree(18, BinTree(9)), BinTree(29, BinTree(26, None, BinTree(28)))), BinTree(41, None, BinTree(52, BinTree(48), BinTree(60))) )
print(estABR(arbreBinaire))
## TESTS
print(arbreBinaire)
