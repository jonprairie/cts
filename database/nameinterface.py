import sqlite3
import random

import cts.chess_federation.country       #temporary

conn = sqlite3.connect('database/names/names.db')
name_list = conn.execute('select firstname, lastname from fakenames').fetchall()

def GetRandomFirst(gender="male", country=""):
    first_name = random.choice(name_list)[0]
    return first_name

def GetRandomLast(gender="male", country=""):
    last_name = random.choice(name_list)[1]
    return last_name
    
def GetRandomCountry():
    countr = random.choice(cts.chess_federation.country.country_list)
    return countr
    
#Deprecated
def GetRandomFirst1(gender="male", country=""):
    first_name = ""
    while not first_name:
        rand_int = random.randrange(0, 50000)
        query = "select firstname from fakenames where id=" + str(rand_int)
        
        rand_name_record = conn.execute(query).fetchall()
        if rand_name_record:
            first_name = rand_name_record[0][0]
    return first_name
    
def GetRandomLast1(gender="male", country=""):
    last_name = ""
    while not last_name:
        rand_int = random.randrange(0, 50000)
        query = "select lastname from fakenames where id=" + str(rand_int)
      
        rand_name_record = conn.execute(query).fetchall()
        if rand_name_record:
            last_name = rand_name_record[0][0]
    return last_name
    