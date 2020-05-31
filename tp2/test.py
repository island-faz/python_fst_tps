#!/usr/bin/env python
#
# Author: Bourhime Amine
# Email : bourhime_amine@hotmail.fr
# Date  : 25/05/2020

from datetime import *
from Etudiant import Etudiant
from Classe import Classe
from Filiere import Filiere

f = Filiere("LICDA", "Licence Ing. en conception d'applications")
print("[+] Creating filiere: " + f.code)

etud_1 = Etudiant("Q1", "Bourhime", "Amine", date(1991, 7, 29), "0636113105", "mail@mail.fr", "Khouribga", f)
etud_2 = Etudiant("Q2", "Mourtaji", "Nizar", date(1995, 5, 5), "0605050505", "nizar@mail.fr", "Rabat", f)
etud_3 = Etudiant("Q3", "Mounaji", "Loubna", date(1993, 12, 15), "0601010101", "loubna@mail.fr", "Settat", f)
print("[+] Creating 3 Students")


classe = Classe("101010", "Classe 1")
print("[+] Creating Classe: " + classe.NomClasse)


print("[+] Adding Students to classe: " + classe.NomClasse)
classe.AddEtudiant(etud_1)
classe.AddEtudiant(etud_2)
classe.AddEtudiant(etud_3)


e1 = classe.ShowOne("Q2")
print("[+] Getting one student by id: [" + e1.__str__() + "]")


print("[+] Updating student phone number:")
e1.tel = "0666666666"
classe.UpdateEtudiant(e1)


print("[+] Getting list of students of classe")
list_etudiants = classe.ShowAll()
print(*list_etudiants, sep = "\n")

print("---------------------------------------")
print("[+] Deleting one student")
classe.DelEtudiant("Q3")

print("[+] Getting updated list")
list_etudiants = classe.ShowAll()
print(*list_etudiants, sep = "\n")
