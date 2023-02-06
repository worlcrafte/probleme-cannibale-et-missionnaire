
class Etat:

    def __init__(self, nbMg, nbCg, boatPosition, parent, cout):
        self.nbMg = nbMg
        self.nbCg = nbCg
        # ce sera un booleen Si sa valeur est égale à vraie alors la barque est à guache sinon elle est à droite
        self.boatPosition = boatPosition
        self.parent = parent
        self.cout = cout

    def get_nbMg(self):
        return self.nbMg

    def get_nbCg(self):
        return self.nbCg

    def get_boatPosition(self):
        return self.boatPosition

    def get_parent(self):
        return self.parent

    def get_cout(self):
        return self.cout

    # __eq__ (méthode "dunder/magique") permet de redéfinir la fonction ==. Cela nous sera utile pour vérifie si 2 états sont égaux. (fonctionne avec .remove() pour la comparaison d'état)
    # il est possible de redéfinir pour >, <, ... mais inutile pour notre cas.

    def __eq__(self, other):
        # on vérifie que les 2 objets sont de la même classes.
        if isinstance(other, Etat):
            return self.nbCg == other.nbCg and self.nbMg == other.nbMg and self.boatPosition == other.boatPosition
