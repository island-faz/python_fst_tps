#!/usr/bin/env python
#
# Author: Bourhime Amine
# Email : bourhime_amine@hotmail.fr
# Date  : 25/05/2020

import mysql.connector
from mysql.connector import Error

class Action:

    def __init__(self, _host, _user, _passwd):
        try:
            self.connection = mysql.connector.connect(host=_host, user=_user, passwd=_passwd)
            self.cursor = self.connection.cursor()
        except Error as e:
            self.connected = False
            print("Error while connecting to Mysql", e)
        finally:
            if (self.connection.is_connected()):
                print("Connected to Mysql")
                self.connected = True


    def create_db(self, db_name):
        if (self.connection.is_connected()):
            req_create_db = "CREATE DATABASE IF NOT EXISTS " + db_name
            req_use_db = "use " + db_name
            self.cursor.execute(req_create_db)
            self.cursor.execute(req_use_db)


    def close_connection(self):
        if (self.connection.is_connected()):
            self.cursor.close()
            self.connection.close()
            print("Mysql connection is closed")


    def create_tables(self):
        tmp = "CREATE TABLE IF NOT EXISTS "
        req_create_campus_table = tmp + "Campus(ville VARCHAR(64) PRIMARY KEY, adresse VARCHAR(255), tel VARCHAR(16), email VARCHAR(128), site VARCHAR(64))"
        req_create_filiere_table = tmp + "Filiere(code VARCHAR(16) PRIMARY KEY, nomfiliere VARCHAR(128))"
        req_create_etudiant_table = tmp + "Etudiant(cne VARCHAR(16) PRIMARY KEY, nom VARCHAR(16), prenom VARCHAR(16), frais FLOAT(8,2), tel VARCHAR(16), email VARCHAR(128), age INT(3), "
        req_create_etudiant_table = req_create_etudiant_table + "campus VARCHAR(64), filiere VARCHAR(16), FOREIGN KEY (campus) REFERENCES Campus(ville), FOREIGN KEY (filiere) REFERENCES Filiere(code))"
        if (self.connection.is_connected()):
            self.cursor.execute(req_create_campus_table)
            self.cursor.execute(req_create_filiere_table)
            self.cursor.execute(req_create_etudiant_table)


    def clear_tables(self):
        tables = ["Etudiant", "Filiere", "Campus"]
        tmp = "DELETE FROM "
        if (self.connection.is_connected()):
            for i in range(len(tables)):
                clear_req = tmp + tables[i]
                self.cursor.execute(clear_req)


    def insert_campus(self, ville, adresse, tel, email, site):
        _req = "INSERT INTO Campus(ville, adresse, tel, email, site) VALUES(%s, %s, %s, %s, %s)" 
        if (self.connection.is_connected()):
            self.cursor.execute(_req, (ville, adresse, tel, email, site))


    def insert_filiere(self, code, nomfiliere):
        _req = "INSERT INTO Filiere(code, nomfiliere) VALUES(%s, %s)"
        if (self.connection.is_connected()):
            self.cursor.execute(_req, (code, nomfiliere))


    def insert_student(self, cne, nom, prenom, frais, tel, email, age, campus, filiere):
        _req = "INSERT INTO Etudiant(cne, nom, prenom, frais, tel, email, age, campus, filiere) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        if (self.connection.is_connected()):
            self.cursor.execute(_req, (cne, nom, prenom, frais, tel, email, age, campus, filiere))


    def commit(self):
        if (self.connection.is_connected()):
            self.connection.commit()


    def exec_selection_query(self, query):
        if (self.connection.is_connected()):
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records
        return None
