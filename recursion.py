#-*-coding:utf8;-*-

# PREAMBULE:
# La visée de ce script est de montrer que la recursion terminale n'est pas implémentée en python
# A priori, la mémoire devrait être libérée à chaque étape, on ne devrait pas avoir de problèmes
# Néanmoins, on observera que ce n'est pas le cas, sur mon android , le script est 
# interrompu par le système à l'étape 26 alors que normalement cette fonction devrait continuer à s'
# exécuter tant le plafond de recursion (situé par défaut à 997) n'est pas atteint, une exeption de type
# RuntimeError aurait alors due être levée

def uneBelleFonctionRecursiveTerminale(etape=0):
    """ fonction recursive terminale qui crée une grosse liste dans la mémoire,
        laquelle étant normalement libérée à chaque récursion""" 
        
    print("étape {0}: début".format(etape))
    uneGrosseListeQuiRemplitBienLaMemoire = [[['a' for i in range(0,1000)] for k in range(0,1000)] for j in range(0,10)]
    #Taille estimée de la liste: 10Mo
    print("terminé")
    
    return uneBelleFonctionRecursiveTerminale(etape+1) 
    #recursion terminale: la mémoire utilisée par notre fonction est libérée avant la recursion
    

uneBelleFonctionRecursiveTerminale()