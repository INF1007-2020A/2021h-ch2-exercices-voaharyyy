#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    # TODO completer la fonction ici
    for k in range(len(mot)) :
        lettre = mot[k]
        positionMin = ord(lettre)
        if positionMin >= 97 :
            positionMaj = positionMin-32
            lettre = chr(positionMaj)
            mot = mot.replace(mot[k], lettre)
    return mot


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
