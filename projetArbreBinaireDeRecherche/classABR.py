from BinTree import BinTree

class ABR(BinTree):
    def __estABR__(self):
        """ ABR test """
        if self.estVide() or self.estFeuille():
            return True
        if self.gauche().estVide() and not self.droit().estVide():
            return self.droit().racine() > self.racine() and self.droit().__estABR__()
        if self.droit().estVide() and not self.gauche().estVide():
            return self.gauche().racine() <= self.racine() and self.gauche().__estABR__()
        else:
            return(
                    self.gauche().racine() <= self.racine()
                and self.droit().racine() > self.racine()
                and self.gauche().__estABR__()
                and self.droit().__estABR__()
                )
     
    def __init__(self, root = None, left = None, right = None):
        BinTree.__init__(self, root, left, right)
        #ABR Test
        if not self.__estABR__():
            raise ValueError("Les valeurs de l'arbre ne permettent pas la création d'un arbre binaire de recherche")
         
    ## Impression : surcharge de la méthode str car on change les carctères entre les racines par > et <= 
    def __str__(self,n=0,car=""):
        """
        Fournit une vue lisible de l'arbre.
        """
        if not(self.estVide()):
            self.droit().__str__(n+4,'<')
            print(n*" "+car,end=" ")
            print(self.racine())
            self.gauche().__str__(n+4,'>=')
        elif n==0:
            #Imprime "arbre_vide" si l'arbre est vide (lors de l'appel initial)
            print("Arbre_vide")
 
        #La fonction doit renvoyer une chaîne, mais l'impression est déjà gerée plus haut
        return ""
 
 
    def __isInABR__(self, n:int) -> bool:
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
        if self.estVide():
            return False #Si ojn tombe sur un arbre vide -> les arbres se sont echainés et à aucun moment la valeur d'une racine n'à été égale à la valeur cherchée, cette dernière n'est donc pas dans l'arbre
        if self.racine() == n: #Si la racine est le nombre cherché -> renvoie True, la valeur est bien dans l'arbre
            return True
         
        else:  #Dans les autres cas il faut parcourir récursivement l'arbre -> 2 cas possibles dans un ABR
            if n <= self.racine():  #1er cas, la valeur de n est inférieure ou égale à la racine -> elle se trouve donc dans le SAG
                return self.gauche().isInABR(n) # Résolution à partir du SAG
            else: #dans tout les autres la valeur de n est strictement supérieure à celle de racine -> elle se trouve donc dans le SAD
                return self.droit().isInABR(n) #Résolution à partir de SAD
 
    def insereCle(self, n:int) :
        """
        Renvoie un ABR avec la clé insérée au bon endroit
        """
 
        if self.estVide(): #Si l'arbre est vide, on peut ajouter une clé sans contraintes
            return ABR(n)
        if n <= self.racine(): #D'après la définition de l'ABR, si la valeur est <= à la racine, alors elle est dans la partie gauche de l'arbre
            return ABR(self.racine(),self.gauche().insereCle(n), self.droit())
        else: #dans tous les autres cas, elle est dans la partie droite de l'arbre
            return ABR(self.racine(), self.gauche(), self.droit().insereCle(n))
         
    def __sommeCle__(self) -> int:
        """
        Entrée : A -> BinTree
        Sortie : int
        Renvoie la somme des clés de l'ABR donné en args
        """
        if self.estVide():
            return 0
        else:
            return self.racine() + self.gauche().__sommeCle__() + self.droit().__sommeCle__()
 
     
 
arbre = ABR(3, ABR(1), ABR(5))
arbre = arbre.insereCle(2)

print(arbre)