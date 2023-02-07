from Etat import Etat
import time

# regle permet de verifier que l'état calculer respecte bien les règles établis : qu'il n'y ai pas plus de Canibale que de mercenaire sur un côté de la rive (sauf s'il n'y a aucun mercenaire alors il n'y a aucun risque pour eux)


def rule(etat, n, ajout, ajout2):
    if 0 <= etat.get_nbMg()+ajout <= n and 0 <= etat.get_nbCg()+ajout2 <= n:
        return ((((etat.get_nbMg() + ajout) >= (etat.get_nbCg() + ajout2)) or
                 (etat.get_nbMg()+ajout) == 0) and
                (((n-(etat.get_nbMg()+ajout)) == 0 or
                  ((n-(etat.get_nbMg()+ajout)) >= (n-(etat.get_nbCg()+ajout2))))))
    else:
        return False

# expance permet d'expancer l'état courant. Il prend en entrée l'état courant, la capacité maximale du tableau, et le nombre total de mercerniares et cannibales (ici uniquement n car c 2 valeurs sont égaux ). Il retournera une liste contenant tous les états trouver par le programme respectant les règles établis.


def expance(etat, p, n):
    result = []
    for mEmbarque in range(0, p+1):
        for cEmbarque in range((0, 1)[mEmbarque == 0], (1, p-mEmbarque+1)[p-mEmbarque+1 > 0]):
            if (not etat.get_boatPosition()):
                # il es possible aussi de créer 2 variables temporaires et de modifier les informations contenus (+ ou - mais cela revient au même)
                if rule(etat, n, mEmbarque, cEmbarque):
                    result.append(Etat(
                        etat.get_nbMg()+mEmbarque,
                        etat.get_nbCg()+cEmbarque,
                        not etat.get_boatPosition(),
                        etat,
                        etat.get_cout()+1
                    ))
            else:
                if rule(etat, n, -mEmbarque, -cEmbarque):
                    result.append(Etat(
                        etat.get_nbMg()-mEmbarque,
                        etat.get_nbCg()-cEmbarque,
                        not etat.get_boatPosition(),
                        etat,
                        etat.get_cout()+1
                    ))

    return result

# solution prend en paramètre l'état finale trouver par l'algo. Il retournera un liste de tous les parents de la solution. (La racine à la variable parent def à None)


def solution(etat):
    soluce = []
    soluce.append(etat)
    etatC = etat
    while not etatC.get_parent() == None:
        etatC = etatC.get_parent()
        soluce.append(etatC)
    return soluce

# Application de l'algorithme graph-Search


def graph_Search(etat_Initiale, p, n):
    frontiere = []
    explore = []
    # Nous allons simuler une file, nous allons donc utiliser append qui rajoute l'objet en fin de file et l'état choisie à expancer sera celui en t^te de file (donc à la position 0)
    frontiere.append(etat_Initiale)
    etat_Final = Etat(0, 0, False, None, None)

    while True:

        if frontiere == []:
            return None
        elif frontiere[0] == etat_Final:
            return solution(frontiere[0])
        else:
            S = expance(frontiere[0], p, n)
            for si in S:
                frontiere.append(si)
            explore.append(frontiere.pop(0))
            # Supprime les états dans frontière qui sont présent dans eplorer (donc les étas déjà expancé)
            for etat in explore:
                # la fonction remove retourne une erreur lorsqu'elle ne trouve pas l'élément à supprimer dans la file. On va donc capter cette erreur pour éviter de faire "while etat in frontiere". Ce qui nous obligerais à chaque fois de parcourire la file pour s'avoir s'il y a un état correspondant à "etat".
                while True:
                    try:
                        frontiere.remove(etat)
                    except:
                        break


def main():
    n = int(input(
        "Veillez renseigner le nombre n de missionnaires|cannibale à faires traverser (minimum 3): "))
    p = int(input(
        "Veillez renseigner le nombre maximal de personne pouvant monter sur le bateau (au mininimum 2) : "))
    tic = time.perf_counter()
    if (p < 2 or n < 3):
        print("veillez rentrer une valeur correcte.")
    else:
        solution = graph_Search(Etat(n, n, True, None, 0), p, n)
        if (solution != None):
            solution.reverse()
            for etat in solution:
                print("etat solution:", str(etat.get_nbMg()), "M", str(
                    etat.get_nbCg()), "C", ("droite ", "gauche ")[etat.get_boatPosition()], str(etat.get_cout()))
        else:
            print("Aucune solution trouvé")
        toc = time.perf_counter()
        print(f"le programme c'est réaliser en {toc-tic:0.4f} secondes")


main()
