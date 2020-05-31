#!/usr/bin/env python
#
# Author: Bourhime Amine
# Email : bourhime_amine@hotmail.fr
# Date  : 31/05/2020

import sys
import json
import requests
import sqlite3
from sqlite3 import Error

class Covid19:

    def create_connection(self, db_file):
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)


    def close_connection(self):
        if self.conn:
            self.conn.close()

    def create_table(self):
        sql_create_table = """CREATE TABLE IF NOT EXISTS covid19 (
        country text NOT NULL,
        flag text,
        cases integer NOT NULL,
        todayCases integer NOT NULL,
        deaths integer NOT NULL,
        todayDeaths integer NOT NULL,
        recovered integer NOT NULL,
        active integer NOT NULL,
        critical integer NOT NULL);"""
        if self.conn is not None:
            try:
                c = self.conn.cursor()
                c.execute(sql_create_table)
            except Error as e:
                print(e)


    def data_to_db(self):
        url = 'https://corona.lmao.ninja/v2/countries'
        try:
            x = requests.get(url)
        except Exception as e:
            print("Cannot retrieve data from url: " + str(e))
            return False

        if (x.status_code != 200): # getting data not ok
            print("Cannot retrieve data from: " + url)
            print("Error code: " + str(x.status_code))
            return False

        try:
            data = json.loads(x.text)
        except Exception as e:
            print("Unable to parse JSON: " + str(e))
            return False

        sql = '''INSERT INTO covid19(country, flag, cases, todayCases,
        deaths, todayDeaths, recovered, active, critical)
        VALUES(?,?,?,?,?,?,?,?,?) '''
        for row in data:
            tmp = (row['country'], row['countryInfo']['flag'], row['cases'],
                   row['todayCases'], row['deaths'], row['todayDeaths'], 
                   row['recovered'],row['active'], row['critical']) 
            cur = self.conn.cursor()
            cur.execute(sql, tmp)
        self.conn.commit()
        return True


    def showAll(self):
        sql = """SELECT * FROM covid19"""
        cur = self.conn.cursor()
        cur.execute(sql)
        recs = cur.fetchall()
        for row in recs:
            print(row)

    
    def showOne(self, country):
        sql = """SELECT * FROM covid19 WHERE country == ?"""
        cur = self.conn.cursor()
        cur.execute(sql, (country,))
        recs = cur.fetchall()
        print(recs)


if __name__ == '__main__':
    a = Covid19()
    a.create_connection("sqlite3.db")
    a.create_table()
    #a.data_to_db()
    #a.showAll()
    a.showOne("Italy")
    a.close_connection()
