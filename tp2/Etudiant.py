#!/usr/bin/env python
#
# Author: Bourhime Amine
# Email : bourhime_amine@hotmail.fr
# Date  : 23/05/2020

from Filiere import Filiere
from Personne import Personne

class Etudiant(Personne):

    def __init__(self, id, nom, prenom, datenaissance, tel, email, ville, filiere):
        Personne.__init__(self, id, nom, prenom, datenaissance, tel, email, ville)
        self.filiere = filiere

    def __str__(self):
        return super().__str__()
