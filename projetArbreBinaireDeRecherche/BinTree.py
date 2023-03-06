



## Classe
        
class BinTree:
    
    """
    Classe BinTree
    - Attributs :
        * root : La racine root de type N (ou None)
        * left : Le sous-arbre gauche de type BinTree (ou None)
        * right : Le sous-arbre droit de type BinTree (ou None)
      Un arbre vide est représenté par un objet dont tous les attributs ont la valeur None
      
    - Condition : Un arbre est vide si et seulement si la racine est non définie
    
    - Méthodes :
        * Constructeur : BinTree(root,left,right)
        * estVide()
        * droit()
        * gauche()
        * racine()
        * estFeuille()
        * setGauche()
        * setDroit()
        * setRacine()
        * maximum()
        * minimum()
        * taille()
        * hauteur()
        * preFixe()
        * postFixe()
        * infixe
        * __str__()

    """
    ## Constructeur
    
    def __init__(self,root=None,left=None,right=None):
        """
        Constructeur de la classe BinTree (avec arguments optionnels, avec valeur None par défaut)
        """
        # Pré-conditions
        assert (isinstance(left,BinTree) or left==None), "L'arbre gauche doit être un BinTree ou None"
        assert (isinstance(right,BinTree) or right==None), "L'arbre droit doit être un BinTree ou None"
        
        self.root=root
        self.left=left
        self.right=right
        
        #  Axiome
        assert (self.estVide()==(self.root==None)), "Un arbre non vide a une racine"


    ## Méthodes
    
    def droit(self) -> all:
        """
        Renvoie le sous-arbre droit (un arbre vide si l'arbre droit vaut None)
        """
        if self.right==None:
            return type(self)()
        else :
            return self.right
    
    def gauche(self) -> all:
        """
        Renvoie le sous-arbre gauche (un arbre vide si l'arbre gauche vaut None).
        """
        if self.left==None:
            return type(self)()
        else :
            return self.left
    
    def racine(self) -> all:
        """
        Renvoie la valeur de la racine A de l'arbre, None si l'arbre est vide.
        """
        return self.root
    
    def estVide(self) -> bool: 
        """
        Renvoie True si l'arbre est vide.
        """
        return (self.root==None) and (self.left==None) and (self.right==None)
    
    
    
    def estFeuille(self) -> bool:
        """
        Renvoie True si l'arbre est une feuille.
        """
        return self.gauche().estVide() and self.droit().estVide()
        
    def setDroit(self,B) -> None:
        """
        L'arbre droit devient B.
        """
        assert not(self.estVide()), "On ne peut modifier modifier les sous_arbres de l'arbe vide"
        assert (isinstance(B,BinTree) or B==None), "L'argument doit être une instance de BinTree ou None"
        self.right=B
    
    def setGauche(self,B) -> None:
        """
        L'arbre gauche devient B.
        """
        assert not(self.estVide()), "On ne peut modifier les sous_arbres d'un arbe vide"
        assert (isinstance(B,BinTree) or B==None), "L'argument doit être une instance de BinTree ou None"
        self.left=B
        
    def setRacine(self,r) -> None:
        """
        La valeur de la racine devient r.
        """
        self.root=r
        
    ## Mesures  
    def maximum(self) -> int:
        """Donne le maximum de l'arbre si celui-ci comporte des noeuds"""
        if not self.estVide():
            maximum = self.infixe()[0]
            for elt in self.infixe():
                if elt > maximum:
                    maximum = elt
            return maximum
        else:
            return [] 
    def minimum(self):
        if not self.estVide():
            minimum = self.infixe()[0]
            for elt in self.infixe():
                if elt < minimum:
                    minimum = elt
            return minimum
        else:
            return []
    
    def taille(self)->int:
        """
        Renvoie la taille de l'arbre A
        """
        if self.estVide():
            return 0
        else :
            return 1+self.gauche().taille()+self.droit().taille()
            
    def hauteur(self):
        """
        Renvoie la hauteur de l'arbre A
        """
        if self.estVide():
            return -1
        else :
            return 1+max(self.gauche().hauteur(),self.droit().droit().hauteur())
        
    ## Algorithmes de parcours    
    def postFixe(self):
        """ Renvoie une liste des noeuds de l'arbre avec le parcours PostFixe"""
        if self.estVide():
            return []
        else:
            return self.gauche().postFixe() + self.droit().postfixe() + [self.racine()]
    def preFixe(self):
        """ Renvoie une liste des noeuds de l'arbre avec le parcours PreFixe """
        if self.estVide():
            return []
        else: 
            return [self.racine()] + self.gauche().preFixe() + self.droit().preFixe()
    def infixe(self):
        """ Renvoie une liste des noeuds de l'arbre avec le parcours Infixe """
        if self.estVide():
            return []
        else:
            return self.gauche().infixe() + [self.racine()] + self.droit().infixe()
    
    def BFS(self):
        """ Parcours en largeur de l'arbre avec l'algorithme BFS"""
        file = []
        res = []
        file.insert(0, self)
        while file != []:
            n = file.pop()
            res.append(n.racine())
            if not (n.gauche().estVide()):
                file.insert(0, n.gauche())
            if not(n.droit().estVide()):
                file.insert(0, n.droit())
        return res
    ## Impression
    def __str__(self,n=0,car=""):
        """
        Fournit une vue lisible de l'arbre.
        """
        if not(self.estVide()):
            self.droit().__str__(n+4,'/')
            print(n*" "+car,end=" ")
            print(self.racine())
            self.gauche().__str__(n+4,"\\")
        elif n==0:
            #Imprime "arbre_vide" si l'arbre est vide (lors de l'appel initial)
            print("Arbre_vide")
        
        #La fonction doit renvoyer une chaîne, mais l'impression est déjà gerée plus haut 
        return ""



             
        
