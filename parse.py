
'''
Bayan Berri, Donia Tung
Team DataBases 2.0
SoftDev2 pd7
K05--Import/Export Bank
2018-02-16
'''
from pymongo import MongoClient
import urllib2, json
'''setting up interactions with the database'''
client =MongoClient("lisa.stuy.edu",27017)
db = client ["teamDB"]
collection = db["pokedex"]

def read():
    data = urllib2.urlopen("https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json")
    string = data.read()
    dictionary = json.loads(string)#returns json object string into a dict
    for each in dictionary["pokemon"]:
        #print each
        db.collection.insert(each)

read();

def find_boroughs(borough):
   '''
   prints and returns all restaurants in a specified borough.
   '''
   dictionary = collie.find({"borough":borough})
   for each in dictionary:
      print each["name"]
   return dictionary

def by_zip(code):
   '''
   prints and returns all restaurants in a specified zip code.
   '''
   dictionary_zip=collie.find({"address.zipcode":code})
   for each in dictionary_zip:
      print each["name"]
   return dictionary_zip

def by_zip_grade(zc,grade):
   '''
   prints and returns all restaurants in a specified zipcode and with a specified grade.
   '''
   dictionary=collie.find({"$and":[{"address.zipcode":zc},{"grades.grade":grade}]})
   for each in dictionary:
      print each["name"]
   return dictionary

def by_zip_score(zc,threshold):
   '''
   prints and returns all restaurants in a specified zip code
   with a score below a specified threshold
   '''
   dictionary=collie.find({"$and":[{"address.zipcode":zc},{"grades.score":{"$lt":threshold}}]})
   for each in dictionary:
       print each["name"]
   return dictionary

def cleverness(borough, cuisine):
    '''
    based on the borough and cuisine inputted, returns a list of restaurants meeting the specs,
    shows their grade as well as their address, if you'd like to visit them!
    '''
    dictionary=collie.find({"$and":[{"borough":borough},{"cuisine": cuisine}]})
    for each in dictionary:
        addressdict = each["address"]
        gradesdict = each["grades"]
        print each["name"] + " Grade: " + gradesdict[0]["grade"]
        print addressdict["building"]+ " " + addressdict["street"] + " " + addressdict["zipcode"]
    return dictionary




cleverness("Manhattan", "Chinese")

'''
print "=====================BOROUGH==================\n"
find_boroughs("Manhattan")
print "=====================ZIP==================\n"
by_zip('11218')
print "=====================ZG==================\n"
by_zip_grade("11218","A")
print "===================ZS===================\n"
by_zip_score("11218",4)
'''
