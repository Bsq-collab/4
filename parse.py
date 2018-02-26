
'''
Bayan Berri, Donia Tung
Team DataBases 2.0
SoftDev2 pd7
K05--Import/Export Bank
2018-02-16
'''

'''
Our dataset is the PokemonGO-Pokedex json. It can be found here:
https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json
It contains a dictionary with one key-- "Pokemon". each set within the value is a list of attributes such as the pokedex number, pokemon name, type, and an image link of each pokemon. for example the first list of the value in the pokedex is bulbasaur the second is ivysaur and so on.

In order to import this data we used the function insert_many because the dictionary's "root" is just one key. and there are subdictionaries within that value.

'''


from pymongo import MongoClient
import json

'''setting up interactions with the database'''
client =MongoClient("lisa.stuy.edu",27017)
db = client ["teamDB"]#creates new database on lisa
collection = db["pokedex"]


#Creating database
def read_json():
    if collection.count()==0:
        print "UPLOADING"
        js=open("pokedex.json","r")
        pokedex=json.loads(js.read())
        js.close()

        p=pokedex["pokemon"]
        collection.insert_many(p)
    else:
        print "not gonna do anything bc ur code works :) "

def find_name(poke_name):
    '''
    prints and returns pokemon by given name
    '''
    ret=collection.find({"name":poke_name})
    for each in ret:
        print each
    return ret

def by_number(poke_number):
    '''
    prints and returns pokemon by given id number
    '''
    ret=collection.find({"id":poke_number})
    for each in ret:
        print each
    return ret

def by_type(poke_type):
    '''
    prints and returns pokemon by given type
    '''
    ret=collection.find({"type":poke_type})
    for each in ret:
        print each
    return ret

def by_type_id(poke_type,poke_num):
    '''
    prints all the pokemon that are less than pokenum and have type of poke_type
    '''
    ret=collection.find({"$and":[{"id":{"$lt":poke_num}},{"type":poke_type}]})
    for each in ret:
        print each
    return ret

read_json()#commented out bc the table already exists
'''print "\n\n\n============BY NAME===========\n\n\n"
find_name("Bulbasaur")
print "\n\n\n============BY Type===========\n\n\n"
by_type("Fire")
print"==========By Number====== "
by_number(45)
print"========type/ID=========="
by_type_id("Fire",45)'''
