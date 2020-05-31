#!/usr/bin/env python
#
# Author: Bourhime Amine
# Email : bourhime_amine@hotmail.fr
# Date  : 23/05/2020

class Filiere:

    def __init__(self, code, nom):
        self.code = code
        self.nom = nom

    def __str__(self):
        return (self.nom + " (" + self.code + ")")
