#!/usr/bin/env python
#
# Author: Bourhime Amine
# Email : bourhime_amine@hotmail.fr
# Date  : 22/05/2020

import sys
import json
import requests
from json2html import *

def get_json(url):
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
    return data

def filter_countries(data, first_char):
    _data = []
    for country in data:
        if (first_char.upper() == country['country'][0]):
            _data.append(country)
    return _data

def dump_countries(data):
    i = 1
    for country in data:
        print(str(i) + " : " + country['country'])
        i = i + 1

def save_html_file(file_name, html_data):
    html_file = open(file_name, "w")
    html_file.write(html_data)
    html_file.close()
        
def get_global():
    url = 'https://corona.lmao.ninja/v2/all'
    data = get_json(url)
    if (data == False):
        return False
    out = json.dumps(data, indent=4)
    print(out)
    val = input("Would you like to export data into HTML format? type Y or yes to do so, any other key to exit: ")
    if (val.upper() == 'Y' or val.upper() == 'YES'):
        html = json2html.convert(json = out)
        save_html_file("test.html", html)
    return True
        
def get_local():
    url = 'https://corona.lmao.ninja/v2/countries'
    data = get_json(url)
    if (data == False):
        return False
    val = input("Please Input first letter of the country you're interested in: ")
    _data = filter_countries(data, val)
    if (len(_data) == 0):
        print("No countries found, exiting...")
        return False
    dump_countries(_data)
    val = int(input("Please choose the country you're interested in, any other key to exit : ")) - 1
    if (val >= len(_data) or val < 0):
        print("Invalid input, exiting...")        
        return False
    out = json.dumps(_data[val], indent=4)
    print(out)
    val = input("Would you like to export data into HTML format ? type Y or yes to do so, any other key to exit: ")
    if (val.upper() == 'Y' or val.upper() == 'YES'):
        html = json2html.convert(json = out)
        save_html_file("test.html", html)
    return True

welcome_msg = "This is a small script to inform users about Covid-19 situation"
input_msg = "Please enter 1 to get global situation or 2 to get situation by country, any other key to exit: "

def main():
    tmp = False
    print(welcome_msg)
    val = input(input_msg)
    if (val == "1"):
        tmp = get_global()
    elif (val == "2"):
        tmp = get_local()
    if (tmp == False):
        sys.exit(1)
    sys.exit(0)


if __name__ == '__main__':
    main()
