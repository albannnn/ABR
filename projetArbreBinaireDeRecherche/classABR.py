from BinTree import BinTree

class ABR(BinTree):
    def __estABR__(self):
        """ ABR test """
        if self.estVide() or self.estFeuille():
            return True
        if not self.gauche().estVide() and self.gauche().maximum() > self.racine():
            return False
        if not self.droit().estVide() and self.droit().minimum() <= self.racine():
            return False
        return self.gauche().__estABR__() and self.droit().__estABR__()
     
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
 
 
    def isInABR(self, n:int) -> bool:
        """
        Renvoie True si la clé n est dans l'arbre A, False sinon
        """
         
        #assertion
        assert type(n) is int , 'n doit être un entier !'
        #programme
        
        if self.racine() == n: #Si la racine est le nombre cherché -> renvoie True, la valeur est bien dans l'arbre
            return True
        if self.estVide() or self.estFeuille():
            return False #Si on tombe sur un arbre vide -> les arbres se sont echainés et à aucun moment la valeur d'une racine n'à été égale à la valeur cherchée, cette dernière n'est donc pas dans l'arbre
         
        else:  #Dans les autres cas il faut parcourir récursivement l'arbre -> 2 cas possibles dans un ABR
            if n <= self.racine():  #1er cas, la valeur de n est inférieure ou égale à la racine -> elle se trouve donc dans le SAG
                return self.gauche().isInABR(n) # Résolution à partir du SAG
            else: #dans tout les autres la valeur de n est strictement supérieure à celle de racine -> elle se trouve donc dans le SAD
                return self.droit().isInABR(n) #Résolution à partir de SAD
 
    def insereCle(self, n:int) -> None:
        """
        Renvoie un ABR avec la clé insérée au bon endroit
        """
        if self.racine() >= n:
            if self.gauche().estVide():
                self.setGauche(ABR(n))
            else:
                self.gauche().insereCle(n)
        else:
            if self.droit().estVide():
                self.setDroit(ABR(n))
            else:
                self.droit().insereCle(n)
        
    def sommeCle(self) -> int:
        """
        Renvoie la somme des clés de l'ABR donné en args
        """
        if self.estVide():
            return 0
        else:
            return self.racine() + self.gauche().sommeCle() + self.droit().sommeCle()
 

 
arbre = ABR(3, 
            ABR(1), 
            ABR(5))

arbre.insereCle(8) #8 est mtn dans l'abr

print(arbre)
print(arbre.isInABR(8)) #return True
print(arbre)
