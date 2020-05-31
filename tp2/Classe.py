#!/usr/bin/env python
#
# Author: Bourhime Amine
# Email : bourhime_amine@hotmail.fr
# Date  : 23/05/2020

class Classe:

    def __init__(self, idClasse, NomClasse):
        self.idClasse = idClasse
        self.NomClasse = NomClasse
        self.Etudiants = []

    def AddEtudiant(self, etudiant):
        self.Etudiants.append(etudiant)

    def UpdateEtudiant(self, etudiant):
        for idx, _etudiant in enumerate(self.Etudiants):
            if (_etudiant.id == etudiant.id):
                self.Etudiants[idx] = etudiant

    def DelEtudiant(self, id):
        for idx, _etudiant in enumerate(self.Etudiants):
            if (_etudiant.id == id):
                self.Etudiants.pop(idx)
    
    def ShowOne(self, id):
        for etudiant in self.Etudiants:
            if (etudiant.id == id):
                return etudiant
        return None

    def ShowAll(self):
        return self.Etudiants

    def filter(self, etudiant):
        pass

    def __str__(self):
        return self.idClasse + " " + self.NomClasse
