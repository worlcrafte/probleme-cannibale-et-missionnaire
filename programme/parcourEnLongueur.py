from Etat import Etat


def regle(etat, n, ajout, ajout2):
    if 0 <= etat.get_nbMg()+ajout <= n and 0 <= etat.get_nbCg()+ajout2 <= n:
        return ((((etat.get_nbMg() + ajout) >= (etat.get_nbCg() + ajout2)) or
                 (etat.get_nbMg()+ajout) == 0) and
                (((n-(etat.get_nbMg()+ajout)) <= 0 or
                  ((n-(etat.get_nbMg()+ajout)) >= (n-(etat.get_nbCg()+ajout2))))))
    else:
        return False


def expance(etat, p, n):
    result = []
    for mEmbarque in range(0, p+1):
        for cEmbarque in range((0, 1)[mEmbarque == 0], (1, p-mEmbarque+1)[p-mEmbarque+1 > 0]):
            if (not etat.get_boatPosition()):
                if regle(etat, n, mEmbarque, cEmbarque):
                    result.append(Etat(
                        etat.get_nbMg()+mEmbarque,
                        etat.get_nbCg()+cEmbarque,
                        not etat.get_boatPosition(),
                        etat,
                        etat.get_cout()+1
                    ))
            else:
                if regle(etat, n, -mEmbarque, -cEmbarque):
                    result.append(Etat(
                        etat.get_nbMg()-mEmbarque,
                        etat.get_nbCg()-cEmbarque,
                        not etat.get_boatPosition(),
                        etat,
                        etat.get_cout()+1
                    ))

    return result


def solution(etat):
    soluce = []
    soluce.append(etat)
    etatC = etat
    while not etatC.noneParent():
        etatC = etatC.get_parent()
        soluce.append(etatC)
    return soluce


def graph_Search(etat_Initiale, p, n):
    frontiere = []
    explore = []
    frontiere.append(etat_Initiale)
    etat_Final = Etat(0, 0, False, None, None)

    while True:

        if frontiere == []:
            return None
        elif frontiere[len(frontiere)-1] == etat_Final:
            return solution(frontiere[len(frontiere)-1])
        else:
            S = expance(frontiere[len(frontiere)-1], p, n)
            explore.append(frontiere.pop(len(frontiere)-1))
            for si in S:
                frontiere.append(si)
            for etat in explore:
                while etat in frontiere:
                    frontiere.remove(etat)


def main():
    n = int(input("Veillez renseigner le nombre n de missionnaire à faire traverser : "))
    p = int(input(
        "Veillez renseigner le nombre maximal de personne pouvant monter sur le bateau (au mininimum 2) : "))
    if (p < 2):
        print("veillez rentrer une valeur superieur à 2")
    else:
        print(str(p))
        solution = graph_Search(Etat(n, n, True, None, 0), p, n)
        if (solution != None):
            solution.reverse()
            for etat in solution:
                print("etat solution:", str(etat.get_nbMg()), str(
                    etat.get_nbCg()), ("droite ", "gauche ")[etat.get_boatPosition()], str(etat.get_cout()))
        else:
            print("Aucune solution trouvé")


main()
