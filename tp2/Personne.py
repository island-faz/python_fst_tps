#!/usr/bin/env python
#
# Author: Bourhime Amine
# Email : bourhime_amine@hotmail.fr
# Date  : 23/05/2020

from datetime import *

class Personne:

    def __init__(self, id, nom, prenom, datenaissance, tel, email, ville):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.datenaissance = datenaissance
        self.tel = tel
        self.email = email
        self.ville = ville

    def __str__(self):
        return self.id + " " + self.nom + " " + self.prenom

    def CalculerAge(self):
        age = date.today() - self.datenaissance
        age = str(int(age.days / 365))
        return (age + " ans")
