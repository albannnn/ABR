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
    def estFeuille(self):
        """ L'Arbre estb-il une feuille ?"""
        return self.gauche().estVide() and self.droit().estVide()

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






