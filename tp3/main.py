#!/usr/bin/env python
#
# Author: Bourhime Amine
# Email : bourhime_amine@hotmail.fr
# Date  : 30/05/2020

from Action import Action

def print_seperator():
    print("--------------------------------------------------------")

def execute_req_n_show_data(sql):
    data = a.exec_selection_query(sql)
    for row in data:
        print(row)

if __name__ == '__main__':
    a = Action("localhost", "root", "root")
    a.create_db("FSTInscription")
    a.create_tables()
    a.clear_tables()
    a.insert_campus("Settat", "1 adresse test", "06 55 68 95 62", "it-learning-settat@gmail.com", "Site 1")
    a.insert_campus("Rabat", "2 adresse test", "06 55 6 55 01", "it-learning-rabat@gmail.com", "Site 2")
    a.insert_campus("Casablanca", "3 adresse test", "06 55 01 00 62", "it-learning-casa@gmail.com", "Site 3")
    a.insert_filiere("LICDA", "Licence Ing. conception d'application")
    a.insert_filiere("MICDA", "Master Ing. conception d'application")
    a.insert_filiere("LMIAGE", "Licence Methodes informatiques appliquees a la gestion des entreprises")
    a.insert_filiere("MMIAGE", "Master Methodes informatiques appliquees a la gestion des entreprises")
    a.insert_student("Q121212", "BOURHIME", "Amine", 30000, "06 36 11 31 05", "bourhime_amine@hotmaile.fr", 28, "Settat", "LICDA")
    a.insert_student("A151515", "BOUMAHRA", "AYOUBE", 30000, "06 00 00 00 00", "boumahra@hotmaile.fr", 25, "Settat", "LICDA")
    a.insert_student("S454545", "BIDRA", "BADER", 30000, "06 00 69 00 69", "bader_bidra@hotmaile.com", 23, "Settat", "LICDA")
    a.insert_student("D784552", "BERIADA", "HAMZA", 30000, "06 22 22 22 22", "bariada_hamza@hotmaile.com", 30, "Casablanca", "LICDA")
    a.insert_student("Q020103", "ZAKI", "Mouna", 50000, "06 00 00 00 00", "zaki_mouna@hotmaile.fr", 22, "Rabat", "MICDA")
    a.insert_student("D003693", "ALLAOUI", "ZINE DINE", 40000, "06 22 00 22 22", "allaoui_zine@hotmaile.com", 31, "Rabat", "MICDA")
    a.insert_student("A129824", "MOURTAJI", "Intissar", 50000, "06 00 00 00 00", "boumahra@hotmaile.fr", 25, "Settat", "MMIAGE")
    a.insert_student("S987602", "MOURIDE", "HOUSSAM", 50000, "06 00 69 10 00", "mourid_housam@hotmaile.com", 23, "Casablanca", "LMIAGE")
    a.insert_student("A121124", "WARDI", "OUSSAMA", 50000, "06 00 00 00 00", "wardi_ous@hotmaile.fr", 25, "Casablanca", "MMIAGE")
    a.insert_student("S980001", "MOUSSAID", "WAFAA", 50000, "06 00 69 10 11", "wafaa_mousaid@hotmaile.com", 19, "Casablanca", "LMIAGE")
    a.commit()
    print_seperator()
    print("List of All students: ")
    execute_req_n_show_data("select * from Etudiant where age >= 23")
    print_seperator()
    print("List of Campus where number of students is more than 100: ")
    execute_req_n_show_data("SELECT campus, COUNT(campus) FROM Etudiant GROUP BY campus HAVING COUNT(campus) > 100")
    print_seperator()
    print("List of All students (cne, nom, prenom, campus, filiere): ")
    execute_req_n_show_data("select cne, nom, prenom, campus, filiere from Etudiant")
    print_seperator()
    print("Number of Students (campus, students nbr): ")
    execute_req_n_show_data("SELECT campus, COUNT(campus) FROM Etudiant GROUP BY campus")
    print_seperator()
    a.close_connection()
