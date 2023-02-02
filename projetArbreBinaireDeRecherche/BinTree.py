class BinTree:
    """ Création d'une classe du type BinTree """

    def __init__(self, root = None, left = None, right = None):

        """ constructeur """

       # assert (isinstance(left, BinTree) or left == None), "L'Arbre doit etre vide ou de classe BinTree"
        #assert (isinstance(right, BinTree) or right == None), "L'Arbre doit etre vide ou de classe BinTree")

        self.__root = root
        self.__left = left
        self.__right = right

        #axiome
        assert (self.estVide()==(self.__root==None)), "Un arbre non vide a une racine"

    def __str__(self,n=0,car=""):
        """
        Fournit une vue lisible de l'arbre.
        """
        if not(self.estVide()):
            self.droit().__str__(n+4,'/')
            print(n*" "+car,end=" ")
            print(self.racine())
            self.gauche().__str__(n+4,'\\')
        elif n==0:
            #Imprime "arbre_vide" si l'arbre est vide (lors de l'appel initial)
            print("Arbre_vide")

        #La fonction doit renvoyer une chaîne, mais l'impression est déjà gerée plus haut
        return ""

    def estVide(self):
        """ L'Arbre est-il vide ? """
        return self.__root == None


    def gauche(self):
        """ Sous Arbre Gauche """
        if self.__left == None:
            return BinTree()
        return self.__left

    def droit(self):
        """ Sous Arbre Droit """
        if self.__right == None:
            return BinTree()
        return self.__right

    def racine(self):
        """  Racine """
        return self.__root

    def setGauche(self, var):
        """ Définiton du SAG """
        self.__left =  var
        return None

    def setDroit(self, var):
        """ Définition du SAD """
        self.__right = var
        return None

    def setRoot(self, r):
        """ Définition de la racine """
        self.__root = r
        return None

    def taille(self) -> int:
        if self.estVide():
            return 0
        else:
            return 1 + self.__right.taille() + self.__left.taille()

    def hauteur(self):
        if self.estVide():
            return -1
        elif self.__left.hauteur() >= self.__right.hauteur():
            return self.___left.hauteur() + 1
        else:
            return self.__right.hauteur() + 1

"""
tree = BinTree()
tree.setRoot('P')
tree.setGauche(BinTree('Y'))
tree.setDroit(BinTree('T'))
print(tree)
"""

pedigree = BinTree("Mango", BinTree("Domino", BinTree("Isaac"), BinTree("Douchka")),BinTree("Pinkie", BinTree("Tango", BinTree("Tim"), BinTree("Iris")))

def nombre_chiens_rec(tree:BinTree, n):
    if tree.estVide():
        return 0
    elif n == 0:
        return 1
    else:
        return nombre_chiens_rec(tree.gauche(), n - 1) + nombre_chiens_rec(tree.droit(), n - 1)

def nombre_chiens_iterative(tree:BinTree, n):

    liste = [tree]
    for i in range(n + 1):
        if i != n:
            temp = []
            for j in liste:
                if j.gauche().estVide():
                    sag = []
                if j.droit().estVide():
                    sad = []
                else:
                    sag = [j.gauche()]
                    sad = [j.droit()]
                temp += sag + sad
            liste = temp
        if i == n:
            temp = []
            for j in liste:
               temp += [j.racine()]
            liste = temp
    return len(liste)
var = 3

print(pedigree)
print(nombre_chiens_rec(pedigree, var))
print(nombre_chiens_iterative(pedigree, var))


print(pedigree.droit().gauche().gauche().racine())




